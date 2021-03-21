from microbit import *


def main():
    duty = 0
    while True:
        while duty < 1023:
            pin0.write_analog(duty)
            duty += 1
            sleep(10)
        while duty > 0:
            pin0.write_analog(duty)
            duty -= 1
            sleep(10)


if __name__ == "__main__":
    main()
