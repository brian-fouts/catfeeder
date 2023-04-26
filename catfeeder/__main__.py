import os

from catfeeder.catfeeder import catfeeder_factory
from catfeeder.config import config_factory


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
    catfeeder = catfeeder_factory(catfeeder_config)
    catfeeder.run()


if __name__ == "__main__":
    main()
