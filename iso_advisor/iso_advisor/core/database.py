"""ذخیره‌ی تاریخچه‌ی ارزیابی‌ها در SQLite."""
import json
import sqlite3
from contextlib import closing
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "history.db"

SCHEMA = """CREATE TABLE IF NOT EXISTS assessments(
  id INTEGER PRIMARY KEY AUTOINCREMENT, created TEXT, org TEXT, sector TEXT,
  standard_id TEXT, percent REAL, level TEXT, mode TEXT, answers TEXT, plan TEXT)"""


def _conn(path=None):
    c = sqlite3.connect(path or DB_PATH)
    c.row_factory = sqlite3.Row
    c.execute(SCHEMA)
    return c


def save(org, sector, result, plan, mode, path=None) -> int:
    with closing(_conn(path)) as c:
        cur = c.execute(
            "INSERT INTO assessments(created,org,sector,standard_id,percent,level,mode,answers,plan) VALUES(?,?,?,?,?,?,?,?,?)",
            (datetime.now().strftime("%Y-%m-%d %H:%M"), org, sector, result["standard_id"], result["percent"],
             result["level"], mode, json.dumps(result["answers"], ensure_ascii=False), plan))
        c.commit()
        return cur.lastrowid


def list_all(path=None) -> list[dict]:
    with closing(_conn(path)) as c:
        return [dict(r) for r in c.execute("SELECT * FROM assessments ORDER BY id DESC")]


def clear(path=None):
    with closing(_conn(path)) as c:
        c.execute("DELETE FROM assessments")
        c.commit()
