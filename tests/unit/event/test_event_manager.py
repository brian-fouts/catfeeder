from unittest.mock import MagicMock


def test_publish(event_manager):
    """
    GIVEN an event manager
        AND a callback subscribed to an event
    WHEN the event is published
    THEN 1 is returned from publish
        AND the callback is called with the correct arguments
    """
    callback = MagicMock()
    event_name = "test_event"
    args = (1, 2, 3)
    kwargs = {"a": 1, "b": 2, "c": 3}
    event_manager.subscribe(event_name, callback)
    assert event_manager.publish(event_name, *args, **kwargs) == 1
    callback.assert_called_once_with(*args, **kwargs)


def test_publish_no_subscribers(event_manager):
    """
    GIVEN an event manager
        AND no callbacks are subscribed
    WHEN the event is published
    THEN 0 is returned from publish
    """
    event_name = "test_event"
    assert event_manager.publish(event_name) == 0
