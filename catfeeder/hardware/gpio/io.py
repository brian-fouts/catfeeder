import logging


class GPIOPin:
    def __init__(self, mode: str):
        self.mode = mode
        self.value = False


class GPIOEmulator:
    OUT = "out"
    IN = "in"
    BCM = "bcm"

    def __init__(self):
        self._pins = {}

    def setmode(self, mode: str) -> None:
        logging.info(f"GPIOEmulator.setmode({mode})")

    def setup(self, pin: int, mode: str) -> None:
        logging.info(f"GPIOEmulator.setup({pin}, {mode})")
        self._pins[pin] = GPIOPin(mode)

    def output(self, pin: int, value: bool):
        logging.info(f"GPIOEmulator.output({pin}, {value})")
        self._pins[pin].value = value

    def input(self, pin: int) -> bool:
        logging.info(f"GPIOEmulator.input({pin})")
        return self._pins[pin].value

    def cleanup(self):
        logging.info(f"GPIOEmulator.cleanup()")
        self._pins = {}


def io_factory(type):
    if type == "emulator":
        return GPIOEmulator()
    elif type == "gpio":
        # This package can only be imported/installed on RaspberryPi
        try:
            import RPi.GPIO as GPIO  # type: ignore
        except ImportError:
            logging.error("Could not import RPi.GPIO. Are you running on a Raspberry Pi?")
            raise
        return GPIO
    else:
        raise TypeError(f"Invalid io type: {type}")
