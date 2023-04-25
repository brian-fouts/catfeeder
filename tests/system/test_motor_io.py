from unittest.mock import MagicMock


def test_scheduled_event_starts_motor(catfeeder, patch_datetime_now, gpio):
    """
    GIVEN a CatFeeder
        AND a callback is registered for the EVENT_EXECUTE event
        AND the current time is the next scheduled time
    WHEN update is called on the CatFeeder
    THEN the GPIO pin for the motor is set to True
    """
    callback = MagicMock()
    catfeeder.event_manager.subscribe(catfeeder.schedule.EVENT_EXECUTE, callback)
    patch_datetime_now.set_now(catfeeder.schedule.next_time())
    catfeeder.update()
    assert gpio.input(catfeeder.config.pin_mapping.motor) == True


def test_ticker_stops_motor(catfeeder, patch_datetime_now, gpio):
    """
    GIVEN a CatFeeder
    AND the time is set to the next scheduled time
    WHEN the ticker increments the number of ticks per serving
    THEN the GPIO pin for the motor is set to False
    """
    patch_datetime_now.set_now(catfeeder.schedule.next_time())
    catfeeder.update()
    for _ in range(catfeeder.config.motor.ticks_per_serving):
        gpio.output(catfeeder.config.pin_mapping.ticker, True)
        catfeeder.update()
        gpio.output(catfeeder.config.pin_mapping.ticker, False)
        catfeeder.update()
    assert gpio.input(catfeeder.config.pin_mapping.motor) == False
