import pytest

from catfeeder.catfeeder import catfeeder_factory

@pytest.fixture
def catfeeder(gpio):
    return catfeeder_factory(gpio)