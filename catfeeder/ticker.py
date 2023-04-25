import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from catfeeder.event import EventManager
    from catfeeder.gpio import PinManager


class TickerState:
    """Base class for Ticker state machine states"""

    def on_transition(self, is_activated: bool) -> None:
        raise NotImplementedError()

    def on_enter(self) -> None:
        pass


class TickerActivatedState(TickerState):
    """State for when the Ticker is activated"""

    def __init__(self, fsm):
        self.fsm = fsm

    def on_transition(self, is_activated: bool) -> None:
        if not is_activated:
            self.fsm.state = TickerDeactivatedState(self.fsm)


class TickerDeactivatedState(TickerState):
    """State for when the Ticker is deactivated"""

    def __init__(self, fsm):
        self.fsm = fsm

    def on_enter(self) -> None:
        self.fsm.event_manager.publish(self.fsm.EVENT_TICKER_INCREMENTED)

    def on_transition(self, is_activated: bool) -> None:
        if is_activated:
            self.fsm.state = TickerActivatedState(self.fsm)


class TickerStateMachine:
    """State machine for the Ticker"""

    EVENT_TICKER_INCREMENTED = "ticker:incremented"

    def __init__(self, initial_state: bool, event_manager: "EventManager"):
        self.event_manager = event_manager
        self._state: TickerState = (
            TickerActivatedState(self) if initial_state else TickerDeactivatedState(self)
        )

    def on_transition(self, is_activated: bool):
        self.state.on_transition(is_activated)

    @property
    def state(self) -> TickerState:
        return self._state

    @state.setter
    def state(self, state: TickerState) -> None:
        self._state = state
        logging.debug(f"State changed to {state.__class__.__name__}")
        self._state.on_enter()


class Ticker:
    """Emits events when ticker hardware transitions from high to low"""

    def __init__(self, pin_number: int, pin_manager: "PinManager", event_manager: "EventManager"):
        self.pin_manager = pin_manager
        self.pin_number = pin_number
        self.pin_manager.setup_pin(self.pin_number, self.pin_manager.gpio.IN)
        is_activated = self.read_state()
        self.state_machine = TickerStateMachine(is_activated, event_manager)

    def read_state(self) -> bool:
        return self.pin_manager.read_pin(self.pin_number)

    def update(self) -> None:
        self.state_machine.on_transition(self.read_state())


def ticker_factory(
    pin_number: int, pin_manager: "PinManager", event_manager: "EventManager"
) -> Ticker:
    return Ticker(pin_number, pin_manager, event_manager)
