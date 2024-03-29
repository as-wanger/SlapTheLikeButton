# you can put in test_slapping with other tests
# but create a file can be available everywhere
# fixture can avoid boilerplate setup and tear down code for tests
import pytest
import sys


@pytest.fixture
def capture_stdout(monkeypatch):  # automatically undone
    buffer = {"stdout": "", "write_calls": 0}

    def fake_write(s):
        buffer["stdout"] += s
        buffer["write_calls"] += 1

    monkeypatch.setattr(sys.stdout, 'write', fake_write)
    return buffer


@pytest.fixture(scope="session")  # scope="session" can cache the value
def db_conn():
    db = ...
    url = ...
    with db.connect(url) as conn:  # connection will be torn down after all tests finish
        yield conn  # this can run for every single test
