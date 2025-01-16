import pytest


@pytest.fixture()
def fixture42():
    yield 42
