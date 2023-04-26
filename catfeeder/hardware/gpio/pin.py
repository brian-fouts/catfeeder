from typing import Optional

from catfeeder.hardware.gpio.state_machine import PinStateMachine


class Pin:
    def __init__(self, gpio, pin_number: int, mode: int):
        self.gpio = gpio
        self.pin_number = pin_number
        self.mode = mode
        self.value = False

    def setup(self) -> None:
        self.gpio.setup(self.pin_number, self.mode)


class InputPin(Pin):
    def __init__(self, gpio, pin_number: int):
        super().__init__(gpio, pin_number, gpio.IN)
        self.fsm: PinStateMachine = None  # type: ignore

    def setup(self) -> None:
        super().setup()
        self.value = self.read()
        self.fsm = PinStateMachine(self.value, self.pin_number)

    def read(self) -> bool:
        return True if self.gpio.input(self.pin_number) else False

    def update(self, event_manager) -> None:
        value = self.read()
        self.fsm.update(value, event_manager)


class OutputPin(Pin):
    def __init__(self, gpio, pin_number: int):
        super().__init__(gpio, pin_number, gpio.OUT)

    def write(self, value: bool) -> None:
        self.value = value
        self.gpio.output(self.pin_number, value)
