import os

from catfeeder.catfeeder import catfeeder_factory
from catfeeder.config import config_factory


def get_gpio():
    """Attempts to import RPi.GPIO and exits if it fails"""
    try:
        import RPi.GPIO as GPIO  # type: ignore
    except ImportError:
        print("Could not import RPi.GPIO. Are you running on a Raspberry Pi?")
        exit(1)
    return GPIO


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Hardware controller for cat feeder")
    parser.add_argument(
        "--config-path",
        type=str,
        default=os.path.join("data", "config.yaml"),
        help="Path to the config file",
    )
    args = parser.parse_args()

    if not os.path.exists(args.config_path):
        print(f"Config file {args.config_path} does not exist")
        exit(1)

    catfeeder_config = config_factory(args.config_path)
    catfeeder = catfeeder_factory(catfeeder_config, get_gpio())
    catfeeder.run()


if __name__ == "__main__":
    main()
