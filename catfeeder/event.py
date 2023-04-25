from collections import defaultdict
from typing import Callable

class EventManager:
    """A simple event manager that allows for subscribing to events and publishing events"""
    def __init__(self):
        self._subscriptions = defaultdict(list)
    
    def subscribe(self, event_name: str, callback: Callable) -> None:
        """Subscribe to an event"""
        self._subscriptions[event_name].append(callback)
    
    def publish(self, event_name: str, *args, **kwargs) -> int:
        """Invokes all callbacks subscribed to the event_name and returns the number of callbacks invoked"""
        for callback in self._subscriptions[event_name]:
            callback(*args, **kwargs)

        return len(self._subscriptions[event_name])