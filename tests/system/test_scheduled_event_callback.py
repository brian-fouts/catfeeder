from unittest.mock import MagicMock

def test_catfeeder_emits_schedule_event(catfeeder, patch_datetime_now):
    """
    GIVEN a CatFeeder
        AND a callback is registered for the EVENT_EXECUTE event
        AND the current time is the next scheduled time
    WHEN update is called on the CatFeeder
    THEN the callback is called
    """
    callback = MagicMock()
    catfeeder.event_manager.subscribe(catfeeder.schedule.EVENT_EXECUTE, callback)
    patch_datetime_now.set_now(catfeeder.schedule.next_time())
    catfeeder.update()
    callback.assert_called_once()