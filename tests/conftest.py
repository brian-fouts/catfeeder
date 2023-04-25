import logging
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


class GPIOPin:
    def __init__(self, mode: str):
        self.mode = mode
        self.value = False


class GPIOEmulator:
    OUT = "out"
    IN = "in"
    BCM = "bcm"

    def __init__(self):
        self._pins = {}

    def setmode(self, mode: str) -> None:
        logging.info(f"GPIOEmulator.setmode({mode})")

    def setup(self, pin: int, mode: str) -> None:
        logging.info(f"GPIOEmulator.setup({pin}, {mode})")
        self._pins[pin] = GPIOPin(mode)

    def output(self, pin: int, value: bool):
        logging.info(f"GPIOEmulator.output({pin}, {value})")
        self._pins[pin].value = value

    def input(self, pin: int) -> bool:
        logging.info(f"GPIOEmulator.input({pin})")
        return self._pins[pin].value

    def cleanup(self):
        logging.info(f"GPIOEmulator.cleanup()")
        self._pins = {}


@pytest.fixture
def gpio():
    return GPIOEmulator()


@pytest.fixture
def pin_manager(gpio):
    from catfeeder.gpio import pin_manager_factory

    return pin_manager_factory(gpio)
