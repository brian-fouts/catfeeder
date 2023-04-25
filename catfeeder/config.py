from dataclasses import dataclass, field
from typing import List
import yaml

@dataclass
class PinMapping:
    motor: int
    ticker: int

@dataclass
class ScheduleItemConfig:
    """Configuration for schedule item"""
    hour: int
    minute: int


@dataclass
class ScheduleConfig:
    """Configuration for schedule"""
    items: List[ScheduleItemConfig]

    def __post_init__(self):
        items = []
        for item in self.items:
            items.append(ScheduleItemConfig(**item))

        self.items = items

@dataclass
class TickerConfig:
    ticks_per_serving: int


@dataclass
class CatfeederConfig:
    schedule: ScheduleConfig
    pin_mapping: PinMapping
    ticker: TickerConfig

    def __post_init__(self):
        self.schedule = ScheduleConfig(items=self.schedule)
        self.pin_mapping = PinMapping(**self.pin_mapping)
        self.ticker = TickerConfig(**self.ticker)


def config_factory(config_path: str) -> CatfeederConfig:
    """Create a CatfeederConfig from a yaml file"""
    with open(config_path, 'r') as f:
        config_data = yaml.safe_load(f)

    return CatfeederConfig(**config_data)