"""
Unit tests untuk Core Calculation Engine.
Semua test dirancang agar LULUS (passed) dengan pytest.
"""

import pytest
from src.app import app, add, subtract, multiply, divide, square_root, natural_log


# ─────────────────────────────────────────────
# Fixtures
# ─────────────────────────────────────────────

@pytest.fixture()
def client():
    """Flask test client."""
    app.config.update(TESTING=True)
    return app.test_client()


# ─────────────────────────────────────────────
# Unit tests: fungsi murni
# ─────────────────────────────────────────────

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 999) == 0

def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

def test_square_root_positive():
    assert square_root(144) == 12.0
    assert square_root(0) == 0.0

def test_square_root_negative_raises():
    with pytest.raises(ValueError, match="sqrt domain error"):
        square_root(-9)

def test_natural_log_positive():
    import math
    assert natural_log(1) == 0.0
    assert abs(natural_log(math.e) - 1.0) < 1e-9

def test_natural_log_zero_raises():
    with pytest.raises(ValueError, match="ln domain error"):
        natural_log(0)

def test_natural_log_negative_raises():
    with pytest.raises(ValueError, match="ln domain error"):
        natural_log(-5)


# ─────────────────────────────────────────────
# Integration tests: Flask HTTP endpoint
# ─────────────────────────────────────────────

def test_get_homepage(client):
    r = client.get("/")
    assert r.status_code == 200
    assert b"PIXEL CALC" in r.data

def test_http_add(client):
    r = client.post("/", data={"a": "10", "op": "add", "b": "5"})
    assert b"15.0" in r.data

def test_http_subtract(client):
    r = client.post("/", data={"a": "10", "op": "sub", "b": "4"})
    assert b"6.0" in r.data

def test_http_multiply(client):
    r = client.post("/", data={"a": "3", "op": "mul", "b": "4"})
    assert b"12.0" in r.data

def test_http_divide(client):
    r = client.post("/", data={"a": "10", "op": "div", "b": "2"})
    assert b"5.0" in r.data

def test_http_divide_by_zero(client):
    r = client.post("/", data={"a": "5", "op": "div", "b": "0"})
    assert b"Error" in r.data

def test_http_sqrt_positive(client):
    r = client.post("/", data={"a": "144", "op": "sqrt"})
    assert b"12.0" in r.data

def test_http_sqrt_zero(client):
    r = client.post("/", data={"a": "0", "op": "sqrt"})
    assert b"0.0" in r.data

def test_http_sqrt_negative(client):
    r = client.post("/", data={"a": "-9", "op": "sqrt"})
    assert b"Error" in r.data

def test_http_ln_positive(client):
    r = client.post("/", data={"a": "1", "op": "ln"})
    assert b"0.0" in r.data

def test_http_ln_zero(client):
    r = client.post("/", data={"a": "0", "op": "ln"})
    assert b"Error" in r.data

def test_http_ln_negative(client):
    r = client.post("/", data={"a": "-9", "op": "ln"})
    assert b"Error" in r.data
