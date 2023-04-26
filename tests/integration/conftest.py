import os

import pytest


@pytest.fixture
def event_manager():
    from catfeeder.event import EventManager

    return EventManager()
