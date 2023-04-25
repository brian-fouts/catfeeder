import os
import time

from catfeeder.config import CatfeederConfig
from catfeeder.event import EventManager
from catfeeder.gpio import pin_manager_factory
from catfeeder.motor import motor_controller_factory, motor_factory
from catfeeder.schedule import Schedule, schedule_factory
from catfeeder.ticker import Ticker, ticker_factory


class Catfeeder:
    """Runs update loop for catfeeder"""

    def __init__(
        self,
        config: CatfeederConfig,
        schedule: Schedule,
        event_manager: EventManager,
        ticker: Ticker,
    ):
        self.config = config
        self.schedule = schedule
        self.event_manager = event_manager
        self.ticker = ticker
        self.running = False

    def update(self) -> None:
        """Update the catfeeder components"""
        self.schedule.update(self.event_manager)
        self.ticker.update()

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


def setup_motor(catfeeder_config, schedule, pin_manager, event_manager, ticker):
    """Setup motor controller and subscribe to events"""
    motor = motor_factory(catfeeder_config.pin_mapping.motor, pin_manager)
    motor_controller = motor_controller_factory(catfeeder_config, motor)
    event_manager.subscribe(schedule.EVENT_EXECUTE, motor_controller.on_schedule_execute)
    event_manager.subscribe(
        ticker.state_machine.EVENT_TICKER_INCREMENTED, motor_controller.on_ticker_incremented
    )


def catfeeder_factory(catfeeder_config, gpio) -> Catfeeder:
    """Create a Catfeeder from a config"""
    schedule = schedule_factory(catfeeder_config)
    event_manager = EventManager()
    pin_manager = pin_manager_factory(gpio)
    ticker = ticker_factory(catfeeder_config.pin_mapping.ticker, pin_manager, event_manager)
    setup_motor(catfeeder_config, schedule, pin_manager, event_manager, ticker)
    return Catfeeder(catfeeder_config, schedule, event_manager, ticker)
