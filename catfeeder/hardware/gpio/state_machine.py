import logging
from typing import List, Optional

from catfeeder.event import EventManager


class BoolPinState:
    """Base class for pin state machine states"""

    def __init__(self, fsm: "PinStateMachine"):
        self.fsm = fsm

    def on_transition(self, is_activated: bool, event_manager: "EventManager") -> None:
        raise NotImplementedError()

    def on_enter(self, event_manager: "EventManager") -> None:
        pass


class ActivatedBoolPinState(BoolPinState):
    """State for when the pin is activated"""

    def on_enter(self, event_manager: EventManager) -> None:
        event_manager.publish(event_manager.pin_activated_event_name(self.fsm.pin_number))

    def on_transition(self, is_activated: bool, event_manager: "EventManager") -> None:
        if not is_activated:
            self.fsm.on_transition(DeactivatedBoolPinState(self.fsm), event_manager)


class DeactivatedBoolPinState(BoolPinState):
    """State for when the pin is deactivated"""

    def on_enter(self, event_manager: EventManager) -> None:
        event_manager.publish(event_manager.pin_deactivated_event_name(self.fsm.pin_number))

    def on_transition(self, is_activated: bool, event_manager: EventManager) -> None:
        if is_activated:
            self.fsm.on_transition(ActivatedBoolPinState(self.fsm), event_manager)


def state_factory(is_activated: bool, fsm: "PinStateMachine") -> BoolPinState:
    """Factory function for creating the correct state"""
    return ActivatedBoolPinState(fsm) if is_activated else DeactivatedBoolPinState(fsm)


class PinStateMachine:
    """State machine for the pin"""

    def __init__(self, initial_state: bool, pin_number: int):
        self.pin_number = pin_number
        self.state = state_factory(initial_state, self)

    def update(self, is_activated: bool, event_manager: EventManager) -> None:
        self.state.on_transition(is_activated, event_manager)

    def on_transition(self, state: BoolPinState, event_manager: EventManager) -> None:
        self.state = state
        logging.debug(f"State changed to {state.__class__.__name__}")
        self.state.on_enter(event_manager)
