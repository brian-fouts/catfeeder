import pytest

@pytest.mark.parametrize("pin_number", [1, 2, 3], ids=lambda p:p)
@pytest.mark.parametrize("pin_value", [True, False], ids=lambda v:v)
def test_pin_manager(pin_manager, pin_number, pin_value):
    """
    GIVEN a pin manager
        AND a pin number
        AND a pin value
    WHEN the pin is setup
        AND the pin is written to
        AND the pin is read from
    THEN the correct pin value is returned
    """
    pin_manager.setup_pin(pin_number, pin_manager.gpio.OUT)
    pin_manager.write_pin(pin_number, pin_value)
    assert pin_manager.read_pin(pin_number) == pin_value