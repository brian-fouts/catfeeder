class Motor:
    def __init__(self, pin_number: int, pin_manager: "PinManager"):
        self.pin_number = pin_number
        self.pin_manager = pin_manager
        self.pin_manager.setup_pin(self.pin_number, self.pin_manager.gpio.OUT)

    def start(self) -> None:
        self.pin_manager.write_pin(self.pin_number, True)

    def stop(self) -> None:
        self.pin_manager.write_pin(self.pin_number, False)


class MotorController:
    def __init__(self, catfeeder_config: "CatfeederConfig", motor: Motor):
        self.catfeeder_config = catfeeder_config
        self.motor = motor
        self.tick_counter = 0
    
    def on_schedule_execute(self) -> None:
        self.motor.start()
    
    def on_ticker_incremented(self) -> None:
        self.tick_counter += 1
        if self.tick_counter >= self.catfeeder_config.ticker.ticks_per_serving:
            self.motor.stop()
            self.tick_counter = 0


def motor_factory(pin_number: int, pin_manager: "PinManager") -> Motor:
    return Motor(pin_number, pin_manager)


def motor_controller_factory(catfeeder_config: "CatfeederConfig", motor: Motor) -> MotorController:
    return MotorController(catfeeder_config, motor)