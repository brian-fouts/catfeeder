import os
import time

from catfeeder.config import CatfeederConfig
from catfeeder.event import EventManager
from catfeeder.hardware.controller.motor import motor_controller_factory, motor_factory
from catfeeder.hardware.gpio.io import io_factory
from catfeeder.hardware.gpio.pin_manager import PinManager, pin_manager_factory
from catfeeder.schedule import Schedule, schedule_factory


class Catfeeder:
    """Runs update loop for catfeeder"""

    def __init__(
        self,
        config: CatfeederConfig,
        schedule: Schedule,
        event_manager: EventManager,
        pin_manager: PinManager,
    ):
        self.config = config
        self.schedule = schedule
        self.event_manager = event_manager
        self.pin_manager = pin_manager
        self.running = False

    def update(self) -> None:
        """Update the catfeeder components"""
        self.schedule.update(self.event_manager)
        self.pin_manager.update(self.event_manager)

    def run(self) -> None:
        """Run the update loop"""
        self.running = True
        while self.running:
            try:
                self.update()
            except KeyboardInterrupt:
                self.running = False
            else:
                time.sleep(0.1)


def setup_motor(catfeeder_config, schedule, pin_manager, event_manager):
    """Setup motor controller and subscribe to events"""
    motor = motor_factory(catfeeder_config.pin_mapping.motor, pin_manager)
    motor_controller = motor_controller_factory(catfeeder_config, motor)
    event_manager.subscribe(schedule.EVENT_EXECUTE, motor_controller.on_schedule_execute)
    event_manager.subscribe(
        event_manager.get_pin_deactivated_event_name(catfeeder_config.pin_mapping.ticker),
        motor_controller.on_ticker_incremented,
    )


def catfeeder_factory(catfeeder_config) -> Catfeeder:
    """Create a Catfeeder from a config"""
    schedule = schedule_factory(catfeeder_config)
    event_manager = EventManager()
    gpio = io_factory(catfeeder_config.pin_manager.io)
    pin_manager = pin_manager_factory(gpio, catfeeder_config)
    setup_motor(catfeeder_config, schedule, pin_manager, event_manager)
    return Catfeeder(catfeeder_config, schedule, event_manager, pin_manager)
