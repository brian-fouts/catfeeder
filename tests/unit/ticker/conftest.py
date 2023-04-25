from unittest.mock import MagicMock

import pytest


@pytest.fixture
def pin_number():
    return 1


@pytest.fixture
def event_manager():
    return MagicMock()


@pytest.fixture
def state_machine(event_manager):
    from catfeeder.ticker import TickerStateMachine

    return TickerStateMachine(False, event_manager)
