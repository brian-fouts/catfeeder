def test_schedule_config(catfeeder_config):
    assert len(catfeeder_config.schedule.items) == 2