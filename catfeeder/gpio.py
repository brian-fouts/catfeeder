class PinManager:
    """Class to manage Rapsberry Pi GPIO pins"""

    def __init__(self, gpio):
        self.gpio = gpio
        self.gpio.setmode(self.gpio.BCM)

    def setup_pin(self, pin: int, mode: str) -> None:
        """Setup a pin with a mode"""
        self.gpio.setup(pin, mode)

    def write_pin(self, pin: int, value: bool) -> None:
        """Write a value to a pin"""
        self.gpio.output(pin, value)

    def read_pin(self, pin: int) -> bool:
        """Read a value from a pin"""
        value = self.gpio.input(pin)
        return True if value else False

    def cleanup(self) -> None:
        """Cleanup GPIO"""
        self.gpio.cleanup()


def pin_manager_factory(gpio) -> PinManager:
    return PinManager(gpio)
