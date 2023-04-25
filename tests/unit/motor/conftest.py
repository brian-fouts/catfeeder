from unittest.mock import MagicMock

import pytest

@pytest.fixture
def pin_number():
    return 1

@pytest.fixture
def pin_manager():
    from catfeeder.gpio import PinManager
    pin_manager = MagicMock(spec=PinManager)
    pin_manager.gpio = MagicMock()
    pin_manager.gpio.OUT = "out"
    return pin_manager

@pytest.fixture
def motor(pin_number, pin_manager):
    from catfeeder.motor import motor_factory
    return motor_factory(pin_number, pin_manager)