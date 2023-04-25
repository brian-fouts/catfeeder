from catfeeder.catfeeder import catfeeder_factory
try:
    import RPi.GPIO as GPIO
except ImportError:
    print("Could not import RPi.GPIO. Are you running on a Raspberry Pi?")
    exit(1)


def main():
    catfeeder = catfeeder_factory(GPIO)
    catfeeder.run()

if __name__ == "__main__":
    main()