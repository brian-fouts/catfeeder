import datetime
from unittest.mock import MagicMock

def test_schedule_emits_event(event_manager, schedule, patch_datetime_now):
    """
    GIVEN an EventManager
        AND a callback is registered for the EVENT_EXECUTE event
        AND a Schedule that has been populated
        AND the current time is the next scheduled time
    WHEN update is called on the Schedule
    THEN the callback is called
    """
    callback = MagicMock()
    event_manager.subscribe(schedule.EVENT_EXECUTE, callback)
    patch_datetime_now.set_now(schedule.next_time())
    schedule.update(event_manager)
    callback.assert_called_once()