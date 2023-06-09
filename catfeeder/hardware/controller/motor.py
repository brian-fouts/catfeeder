from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from catfeeder.config import CatfeederConfig
    from catfeeder.hardware.gpio.pin_manager import PinManager


class Motor:
    """Represents a motor that can be started and stopped"""

    def __init__(self, pin_number: int, pin_manager: "PinManager"):
        self.pin_number = pin_number
        self.pin_manager = pin_manager

    def start(self) -> None:
        self.pin_manager.write_pin(self.pin_number, True)

    def stop(self) -> None:
        self.pin_manager.write_pin(self.pin_number, False)


class MotorController:
    """Responsible for controlling the motor based on the schedule and the ticker"""

    def __init__(self, catfeeder_config: "CatfeederConfig", motor: Motor):
        self.catfeeder_config = catfeeder_config
        self.motor = motor
        self.tick_counter = 0

    def on_schedule_execute(self) -> None:
        self.motor.start()

    def on_ticker_incremented(self) -> None:
        self.tick_counter += 1
        if self.tick_counter >= self.catfeeder_config.motor.ticks_per_serving:
            self.motor.stop()
            self.tick_counter = 0


def motor_factory(pin_number: int, pin_manager: "PinManager") -> Motor:
    return Motor(pin_number, pin_manager)


def motor_controller_factory(catfeeder_config: "CatfeederConfig", motor: Motor) -> MotorController:
    return MotorController(catfeeder_config, motor)
