import os

import pytest


@pytest.fixture
def config():
    from catfeeder.config import config_factory

    config_path = os.path.join("tests", "data", "test_config.yaml")
    return config_factory(config_path)


@pytest.fixture
def catfeeder(config):
    from catfeeder.catfeeder import catfeeder_factory

    return catfeeder_factory(config)


@pytest.fixture
def gpio(catfeeder):
    return catfeeder.pin_manager.gpio
