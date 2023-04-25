import pytest

from catfeeder.event import EventManager


@pytest.fixture
def event_manager():
    return EventManager()
