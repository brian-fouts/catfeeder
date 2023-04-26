# Overview
This project controls a raspberry pi that runs hardware to automatically dispense cat food on a timer.

There are two main hardware components that are integrated with the software via GPIO:
- A motor, which turns a wheel that dispenses predictable units of food
- A tick counter, which determines how many units of food has been dispensed

# Installation
```
$ pip install -e ".[test]"
```

# Test
```
$ pytest
```

# Lint
```
$ black tests catfeeder
$ isort tests catfeeder
```

# Run
```
$ catfeeder
```

# Run Instructions
```
$ catfeeder --help
```