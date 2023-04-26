from catfeeder.hardware.gpio.state_machine import ActivatedBoolPinState, DeactivatedBoolPinState


def test_initial_state(state_machine):
    """
    GIVEN a state machine
    WHEN the state machine is created
    THEN the initial state is DeactivatedBoolPinState
    """
    assert state_machine.state.__class__ == DeactivatedBoolPinState


def test_noop_transition(state_machine, event_manager):
    """
    GIVEN a state machine
    WHEN the state machine is transitioned with no change
    THEN the state remains DeactivatedBoolPinState
    """
    state_machine.update(False, event_manager)
    assert state_machine.state.__class__ == DeactivatedBoolPinState


def test_activate_transition(state_machine, event_manager):
    """
    GIVEN a state machine
    WHEN the state machine is transitioned to activated
    THEN the state is ActivatedBoolPinState
    """
    state_machine.update(True, event_manager)
    assert state_machine.state.__class__ == ActivatedBoolPinState


def test_deactivate_transition(state_machine, event_manager):
    """
    GIVEN a state machine
    WHEN the state machine is transitioned to activated then deactivated
    THEN the state is DeactivatedBoolPinState
    """
    state_machine.update(True, event_manager)
    state_machine.update(False, event_manager)
    assert state_machine.state.__class__ == DeactivatedBoolPinState
