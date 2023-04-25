from unittest.mock import MagicMock

import pytest


@pytest.fixture
def schedule():
    from catfeeder.schedule import Schedule

    return Schedule()


@pytest.fixture
def event_manager():
    return MagicMock()
