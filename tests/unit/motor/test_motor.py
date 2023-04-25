def test_start_motor(motor):
    """
    GIVEN a motor
    WHEN the motor is started
    THEN the pin manager is called to write the pin to True
    """
    motor.start()
    motor.pin_manager.write_pin.assert_called_once_with(motor.pin_number, True)


def test_stop_motor(motor):
    """
    GIVEN a motor
    WHEN the motor is stopped
    THEN the pin manager is called to write the pin to False
    """
    motor.stop()
    motor.pin_manager.write_pin.assert_called_once_with(motor.pin_number, False)
