from catfeeder.ticker import TickerActivatedState, TickerDeactivatedState

def test_initial_state(state_machine):
    """
    GIVEN a state machine
    WHEN the state machine is created
    THEN the initial state is TickerDeactivatedState
    """
    assert state_machine.state.__class__ == TickerDeactivatedState

def test_noop_transition(state_machine):
    """
    GIVEN a state machine
    WHEN the state machine is transitioned with no change
    THEN the state remains TickerDeactivatedState
    """
    state_machine.on_transition(False)
    assert state_machine.state.__class__ == TickerDeactivatedState

def test_activate_transition(state_machine):
    """
    GIVEN a state machine
    WHEN the state machine is transitioned to activated
    THEN the state is TickerActivatedState
    """
    state_machine.on_transition(True)
    assert state_machine.state.__class__ == TickerActivatedState

def test_deactivate_transition(state_machine):
    """
    GIVEN a state machine
    WHEN the state machine is transitioned to activated then deactivated
    THEN the state is TickerDeactivatedState
    """
    state_machine.on_transition(True)
    state_machine.on_transition(False)
    assert state_machine.state.__class__ == TickerDeactivatedState
