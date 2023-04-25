import pytest

@pytest.fixture
def pin_number():
    return 1


@pytest.fixture
def ticker(pin_number, pin_manager, event_manager):
    from catfeeder.ticker import ticker_factory
    return ticker_factory(pin_number, pin_manager, event_manager)