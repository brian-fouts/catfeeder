import pytest


@pytest.fixture
def schedule(catfeeder_config):
    from catfeeder.schedule import schedule_factory
    return schedule_factory(catfeeder_config)