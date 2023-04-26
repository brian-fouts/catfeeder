import logging
from typing import List, Optional

from catfeeder.config import CatfeederConfig
from catfeeder.event import EventManager
from catfeeder.hardware.gpio.pin import InputPin, OutputPin


class PinManager:
    """Class to manage Rapsberry Pi GPIO pins"""

    def __init__(self, gpio):
        self.gpio = gpio
        self.gpio.setmode(self.gpio.BCM)
        self.input_pins = {}
        self.output_pins = {}

    def setup_input_pin(self, pin_number: int) -> None:
        """Setup all pins"""
        self.input_pins[pin_number] = InputPin(self.gpio, pin_number)
        self.input_pins[pin_number].setup()

    def setup_output_pin(self, pin_number: int) -> None:
        """Setup all pins"""
        self.output_pins[pin_number] = OutputPin(self.gpio, pin_number)
        self.output_pins[pin_number].setup()

    def update(self, event_manager: "EventManager") -> None:
        """Update all input pins"""
        for pin in self.input_pins.values():
            pin.update(event_manager)

    def read_pin(self, pin: int) -> bool:
        """Write a value to a pin"""
        return self.input_pins[pin].read()

    def write_pin(self, pin: int, value: bool) -> None:
        """Write a value to a pin"""
        self.output_pins[pin].write(value)

    def cleanup(self) -> None:
        """Cleanup GPIO"""
        self.gpio.cleanup()


def pin_manager_factory(gpio, catfeeder_config: CatfeederConfig) -> PinManager:
    pin_manager = PinManager(gpio)
    for pin in catfeeder_config.pin_manager.input_pins:
        pin_manager.setup_input_pin(pin)

    for pin in catfeeder_config.pin_manager.output_pins:
        pin_manager.setup_output_pin(pin)

    return pin_manager
