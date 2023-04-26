from unittest.mock import MagicMock

import pytest


@pytest.fixture
def pin_number():
    return 1


@pytest.fixture
def event_manager():
    return MagicMock()


@pytest.fixture
def state_machine(pin_number):
    from catfeeder.hardware.gpio.state_machine import PinStateMachine

    return PinStateMachine(False, pin_number)
