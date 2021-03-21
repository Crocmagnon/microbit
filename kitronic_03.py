from microbit import *


def main():
    light_on = False
    touched = False
    while True:
        if pin0.is_touched() and not touched:
            light_on = not light_on
            touched = True
        if not pin0.is_touched():
            touched = False
        if light_on:
            pin2.write_analog(pin1.read_analog())
        else:
            pin2.write_digital(0)


if __name__ == "__main__":
    main()
