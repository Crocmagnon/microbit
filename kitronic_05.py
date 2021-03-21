from microbit import *


def main():
    while True:
        value = min(1023, abs(accelerometer.get_y()))
        pin0.write_analog(value)


if __name__ == "__main__":
    main()
