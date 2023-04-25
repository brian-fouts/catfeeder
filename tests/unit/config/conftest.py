import os

import pytest


@pytest.fixture
def catfeeder_config():
    from catfeeder.config import config_factory

    config_path = os.path.join("tests", "unit", "config", "test_config.yaml")
    return config_factory(config_path)
