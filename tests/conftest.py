import logging
import os
from unittest.mock import MagicMock

import pytest


@pytest.fixture
def patch_datetime_now(monkeypatch):
    import datetime

    class PatchedDatetime(datetime.datetime):
        _now = datetime.datetime.now()

        @classmethod
        def now(cls):
            return cls._now

        @classmethod
        def set_now(cls, new_now):
            cls._now = new_now

    monkeypatch.setattr("datetime.datetime", PatchedDatetime)
    return PatchedDatetime


@pytest.fixture
def gpio():
    from catfeeder.hardware.gpio.io import GPIOEmulator

    return GPIOEmulator()


@pytest.fixture
def catfeeder_config():
    from catfeeder.config import config_factory

    config_path = os.path.join("tests", "data", "test_config.yaml")
    return config_factory(config_path)


@pytest.fixture
def pin_manager(gpio, catfeeder_config):
    from catfeeder.hardware.gpio.pin_manager import pin_manager_factory

    return pin_manager_factory(gpio, catfeeder_config)
