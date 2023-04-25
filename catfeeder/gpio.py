class PinManager:
	def __init__(self, gpio):
		self.gpio = gpio
		self.gpio.setmode(self.gpio.BCM)

	def setup_pin(self, pin: int, mode: str) -> None:
		self.gpio.setup(pin, mode)

	def write_pin(self, pin: int, value: bool) -> None:
		self.gpio.output(pin, value)
	
	def read_pin(self, pin: int) -> bool:
		value = self.gpio.input(pin)
		return True if value else False

	def cleanup(self) -> None:
		self.gpio.cleanup()


def pin_manager_factory(gpio) -> PinManager:
    return PinManager(gpio)