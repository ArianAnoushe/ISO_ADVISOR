import tempfile
import unittest
from pathlib import Path
from unittest import mock

from core import assessor, database, i18n, llm_online, mode_manager, recommender, report


class TestRecommender(unittest.TestCase):
    def test_security_top_fa(self):
        r = recommender.recommend("شرکت نرم‌افزاری هستیم و نگران امنیت داده هستیم", "فناوری اطلاعات")
        self.assertEqual(r[0]["id"], "ISO27001")

    def test_security_top_en(self):
        r = recommender.recommend("We are a software company worried about data security and breaches", "فناوری اطلاعات", lang="en")
        self.assertEqual(r[0]["id"], "ISO27001")
        self.assertIn("Keyword", r[0]["reasons"][0])

    def test_universal_with_empty_text(self):
        self.assertTrue(any(x["id"] == "ISO9001" for x in recommender.recommend("", "تولیدی")))

    def test_percent_bounds(self):
        for x in recommender.recommend("امنیت داده اطلاعات هک نشت سرور", "فناوری اطلاعات"):
            self.assertTrue(0 <= x["match_percent"] <= 100)


class TestAssessor(unittest.TestCase):
    def test_all_yes_and_no(self):
        for lang in ("fa", "en"):
            std = recommender.load_kb(lang)[0]
            n = len(std["questions"])
            r = assessor.evaluate(std, ["بله"] * n, lang)
            self.assertEqual((r["percent"], r["gaps"]), (100, []))
            r0 = assessor.evaluate(std, ["خیر"] * n, lang)
            self.assertEqual((r0["percent"], len(r0["gaps"])), (0, n))

    def test_english_labels(self):
        std = recommender.load_kb("en")[0]
        r = assessor.evaluate(std, ["نسبی"] * len(std["questions"]), "en")
        self.assertEqual(r["level"], "Defined")
        self.assertIn("Action plan", assessor.offline_plan(r))

    def test_wrong_count(self):
        with self.assertRaises(ValueError):
            assessor.evaluate(recommender.load_kb()[0], ["بله"])

    def test_kb_valid(self):
        for lang in ("fa", "en"):
            for s in recommender.load_kb(lang):
                self.assertEqual(len(s["questions"]), 5)


class TestI18n(unittest.TestCase):
    def test_same_keys(self):
        self.assertEqual(i18n.STR["fa"].keys(), i18n.STR["en"].keys())

    def test_footer(self):
        self.assertIn("آرین و آرتینا", i18n.t("fa", "footer"))
        self.assertIn("Arian & Artina", i18n.t("en", "footer"))


class TestDatabaseAndReport(unittest.TestCase):
    def test_roundtrip(self):
        std = recommender.load_kb()[0]
        res = assessor.evaluate(std, ["نسبی"] * len(std["questions"]))
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "t.db"
            database.save("سازمان", "تولیدی", res, "plan", "offline", p)
            self.assertEqual(database.list_all(p)[0]["percent"], 50)
            database.clear(p)
            self.assertEqual(database.list_all(p), [])
        html = report.to_html("x", res, "plan", "offline", "fa")
        self.assertIn("آرین و آرتینا".encode(), html)
        self.assertIn(b'dir="ltr"', report.to_html("x", res, "plan", "offline", "en"))
        self.assertTrue(report.to_csv(res).startswith(b"\xef\xbb\xbf"))


class TestModes(unittest.TestCase):
    def test_modes(self):
        self.assertEqual(mode_manager.resolve_mode("auto", {"api_key": ""}, True)[0], "offline")
        self.assertEqual(mode_manager.resolve_mode("online", {"api_key": "k"}, False)[0], "offline")
        self.assertEqual(mode_manager.resolve_mode("auto", {"api_key": "k"}, True)[0], "online")
        self.assertEqual(mode_manager.resolve_mode("offline", {"api_key": "k"}, True)[0], "offline")

    def test_fallback_on_error(self):
        with mock.patch.object(llm_online, "_chat", side_effect=RuntimeError("boom")):
            res, used, note = mode_manager.smart_recommend("امنیت داده", None, "online", {"api_key": "k"}, "en")
        self.assertEqual(used, "offline")
        self.assertIn("boom", note)

    def test_online_parse(self):
        fake = 'x [{"id":"ISO27001","match_percent":90,"reason":"sec"},{"id":"BAD","match_percent":10}] y'
        with mock.patch.object(llm_online, "_chat", return_value=fake):
            res, used, _ = mode_manager.smart_recommend("x", None, "online", {"api_key": "k"}, "en")
        self.assertEqual((used, [r["id"] for r in res]), ("online", ["ISO27001"]))

    def test_groq_model_autoselect(self):
        self.assertEqual(llm_online.get_config("k", "https://api.groq.com/openai/v1", "grok-3-mini")["model"], "openai/gpt-oss-20b")


if __name__ == "__main__":
    unittest.main()
