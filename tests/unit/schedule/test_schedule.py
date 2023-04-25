import datetime


def test_next_time_today(schedule, patch_datetime_now):
    """
    GIVEN a schedule with an item at 8:00
    WHEN next_time is called at 7:59
    THEN the next time is today at 8:00
    """
    patch_datetime_now.set_now(datetime.datetime(2020, 1, 1, 7, 59))
    schedule.add(8, 0)
    assert schedule.next_time().year == 2020
    assert schedule.next_time().month == 1
    assert schedule.next_time().day == 1
    assert schedule.next_time().hour == 8
    assert schedule.next_time().minute == 0


def test_next_time_now(schedule, patch_datetime_now):
    """
    GIVEN a schedule with an item at 8:00
    WHEN next_time is called at 8:00
    THEN the next time is today at 8:00
    """
    patch_datetime_now.set_now(datetime.datetime(2020, 1, 1, 8, 0))
    schedule.add(8, 0)
    assert schedule.next_time().year == 2020
    assert schedule.next_time().month == 1
    assert schedule.next_time().day == 2
    assert schedule.next_time().hour == 8
    assert schedule.next_time().minute == 0

def test_next_time_tomorrow(schedule, patch_datetime_now):
    """
    GIVEN a schedule with an item at 8:00
    WHEN next_time is called at 8:01
    THEN the next time is tomorrow at 8:00
    """
    patch_datetime_now.set_now(datetime.datetime(2020, 1, 1, 8, 1))
    schedule.add(8, 0)
    assert schedule.next_time().year == 2020
    assert schedule.next_time().month == 1
    assert schedule.next_time().day == 2
    assert schedule.next_time().hour == 8
    assert schedule.next_time().minute == 0


def test_update_empty_schedule(schedule, event_manager):
    """
    GIVEN a schedule with no items
    WHEN update is called
    THEN publish is not called on the event manager
    """
    schedule.update(event_manager)
    event_manager.publish.assert_not_called()


def test_update_doesnt_publish(schedule, patch_datetime_now, event_manager):
    """
    GIVEN a schedule with an item at 8:00
    WHEN update is called at 7:59
    THEN publish is not called on the event manager
    """
    patch_datetime_now.set_now(datetime.datetime(2020, 1, 1, 8, 1))
    schedule.add(8, 0)
    schedule.update(event_manager)
    event_manager.publish.assert_not_called()

def test_update_publish(schedule, patch_datetime_now, event_manager):
    """
    GIVEN a schedule with an item at 8:00 is added before 8:00
    WHEN update is called at 8:00
    THEN publish is called on the event manager with "schedule:execute"
    """
    patch_datetime_now.set_now(datetime.datetime(2020, 1, 1, 7, 59))
    schedule.add(8, 0)
    patch_datetime_now.set_now(datetime.datetime(2020, 1, 1, 8, 0))
    schedule.update(event_manager)
    event_manager.publish.assert_called_with("schedule:execute")


def test_update_publish_called_once(schedule, patch_datetime_now, event_manager):
    """
    GIVEN a schedule with an item at 8:00
    WHEN update is called twice at 8:00
    THEN publish is called on the event manager once
    """
    patch_datetime_now.set_now(datetime.datetime(2020, 1, 1, 7, 59))
    schedule.add(8, 0)
    patch_datetime_now.set_now(datetime.datetime(2020, 1, 1, 8, 0))
    schedule.update(event_manager)
    schedule.update(event_manager)
    event_manager.publish.assert_called_once()