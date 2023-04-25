import datetime
from typing import TYPE_CHECKING

from catfeeder.config import CatfeederConfig

if TYPE_CHECKING:
    from catfeeder.event import EventManager


class ScheduleItem:
    """Represents a single item in the schedule"""

    def __init__(self, hour: int, minute: int):
        self.hour = hour
        self.minute = minute

    @property
    def next_time(self) -> datetime.datetime:
        """Return the next time this item should be executed"""
        now = datetime.datetime.now()
        next_time = datetime.datetime(now.year, now.month, now.day, self.hour, self.minute)
        if next_time <= now:
            next_time += datetime.timedelta(days=1)
        return next_time


class Schedule:
    """Represents a schedule of items to be executed"""

    EVENT_EXECUTE = "schedule:execute"

    def __init__(self):
        self.items = []
        self.next_execution_time = None

    def add(self, hour: int, minute: int) -> None:
        """Add a new item to the schedule"""
        self.items.append(ScheduleItem(hour, minute))
        self.next_execution_time = self.next_time()

    def next_time(self) -> datetime.datetime:
        """Return the next time an item should be executed"""
        return min([item.next_time for item in self.items])

    def update(self, event_manager: "EventManager") -> None:
        if self.next_execution_time and datetime.datetime.now() >= self.next_execution_time:
            self.next_execution_time = self.next_time()
            event_manager.publish(self.EVENT_EXECUTE)


def schedule_factory(catfeeder_config: CatfeederConfig) -> Schedule:
    """Create a Schedule from a CatfeederConfig"""
    schedule = Schedule()
    for item in catfeeder_config.schedule.items:
        schedule.add(item.hour, item.minute)

    return schedule
