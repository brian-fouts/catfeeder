from unittest.mock import MagicMock


def test_ticker_emits_increment_event(ticker, pin_manager, event_manager):
    """
    GIVEN a ticker
        AND a callback is registered for the EVENT_TICKER_INCREMENTED event
    WHEN the ticker trasitions from activated to deactivated
    THEN the callback is called
    """
    callback = MagicMock()
    event_manager.subscribe(ticker.state_machine.EVENT_TICKER_INCREMENTED, callback)
    pin_manager.write_pin(ticker.pin_number, True)
    ticker.update()
    pin_manager.write_pin(ticker.pin_number, False)
    ticker.update()
    callback.assert_called_once()