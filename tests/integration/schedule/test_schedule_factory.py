def test_schedule_factory(schedule, catfeeder_config):
    """
    GIVEN a schedule that has been loaded from config
    WHEN the schedule is created
    THEN the number of items matches the config
    """
    assert len(schedule.items) == len(catfeeder_config.schedule.items)
