import os
import time

from catfeeder.config import config_factory
from catfeeder.event import EventManager
from catfeeder.gpio import pin_manager_factory
from catfeeder.motor import motor_factory, motor_controller_factory
from catfeeder.schedule import schedule_factory
from catfeeder.ticker import ticker_factory

class Catfeeder:
    def __init__(self, config: "CatfeederConfig", schedule: "Schedule", event_manager: "EventManager", ticker: "Ticker"):
        self.config = config
        self.schedule = schedule
        self.event_manager = event_manager
        self.ticker = ticker
        self.running = False

    def update(self) -> None:
        self.schedule.update(self.event_manager)
        self.ticker.update()
    
    def run(self) -> None:
        self.running = True
        while self.running:
            try:
                self.update()
            except KeyboardInterrupt:
                self.running = False
            else:
                time.sleep(0.1)

def setup_motor(catfeeder_config, schedule, pin_manager, event_manager, ticker):
    motor = motor_factory(catfeeder_config.pin_mapping.motor, pin_manager)
    motor_controller = motor_controller_factory(catfeeder_config, motor)
    event_manager.subscribe(schedule.EVENT_EXECUTE, motor_controller.on_schedule_execute)
    event_manager.subscribe(ticker.state_machine.EVENT_TICKER_INCREMENTED, motor_controller.on_ticker_incremented)

def catfeeder_factory(gpio):
    config_path = os.path.join("data", "config.yaml")
    catfeeder_config = config_factory(config_path)
    schedule = schedule_factory(catfeeder_config)
    event_manager = EventManager()
    pin_manager = pin_manager_factory(gpio)
    ticker = ticker_factory(catfeeder_config.pin_mapping.ticker, pin_manager, event_manager)
    setup_motor(catfeeder_config, schedule, pin_manager, event_manager, ticker)
    return Catfeeder(catfeeder_config, schedule, event_manager, ticker)