import pytest
from src.app import app

@pytest.fixture()
def client():
    app.config.update(TESTING=True)
    return app.test_client()

def test_sqrt_positive(client):
    r = client.post("/", data={"a": "144", "op": "sqrt"})
    assert b"12.0" in r.data

def test_sqrt_zero(client):
    r = client.post("/", data={"a": "0", "op": "sqrt"})
    assert b"0.0" in r.data

def test_sqrt_negative_is_domain_error(client):
    r = client.post("/", data={"a": "-9", "op": "sqrt"})
    assert b"domain error" in r.data.lower()
 # create tests for zro and non negative input checks in natural log.
def test_ln_neg_inpt(client):
    r = client.post("/", data={"a": "-9", "op": "ln"})
    assert b"domain error" in r.data.lower()

def test_ln_zero_inpt(client):
    r = client.post("/", data={"a": "0", "op": "ln"})
    assert b"domain error" in r.data.lower()