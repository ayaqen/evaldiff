import json, pytest
from main import score, load
from pathlib import Path

def write(tmp_path, name, data):
    p = tmp_path / name
    p.write_text(json.dumps(data))
    return str(p)

def test_all_unchanged():
    assert score({"a": "1"}, {"a": "1"}) == (0, 0, 1)

def test_improvement():
    assert score({"a": "1"}, {"a": "2"}) == (1, 0, 0)

def test_regression():
    assert score({"a": "2"}, {"a": "1"}) == (0, 1, 0)

def test_missing_key_in_candidate():
    assert score({"a": "1"}, {}) == (0, 1, 0)

def test_load(tmp_path):
    p = tmp_path / "run.json"
    p.write_text('{"x": "hello"}')
    assert load(str(p)) == {"x": "hello"}
