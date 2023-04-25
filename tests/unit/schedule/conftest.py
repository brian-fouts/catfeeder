import pytest
from unittest.mock import MagicMock


@pytest.fixture
def schedule():
    from catfeeder.schedule import Schedule
    return Schedule()

@pytest.fixture
def event_manager():
    return MagicMock()