import os

import pytest


@pytest.fixture
def config():
    from catfeeder.config import config_factory

    config_path = os.path.join("data", "config.yaml")
    return config_factory(config_path)


@pytest.fixture
def catfeeder(config, gpio):
    from catfeeder.catfeeder import catfeeder_factory

    return catfeeder_factory(config, gpio)
