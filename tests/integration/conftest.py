import os

import pytest


@pytest.fixture
def catfeeder_config():
    from catfeeder.config import config_factory

    config_path = os.path.join("tests", "integration", "test_config.yaml")
    return config_factory(config_path)


@pytest.fixture
def event_manager():
    from catfeeder.event import EventManager

    return EventManager()
