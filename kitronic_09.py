from microbit import *


def main():
    while True:
        charge = pin0.read_analog() / 10
        if charge >= 95:
            pin1.write_digital(1)
            pin2.write_digital(1)
            pin8.write_digital(1)
            pin12.write_digital(1)
        elif charge >= 75:
            pin1.write_digital(1)
            pin2.write_digital(1)
            pin8.write_digital(1)
            pin12.write_analog(int((charge - 75) / 25 * 1023))
        elif charge >= 50:
            pin1.write_digital(1)
            pin2.write_digital(1)
            pin8.write_analog(int((charge - 50) / 25 * 1023))
            pin12.write_digital(0)
        elif charge >= 25:
            pin1.write_digital(1)
            pin2.write_analog(int((charge - 25) / 25 * 1023))
            pin8.write_digital(0)
            pin12.write_digital(0)
        else:
            pin1.write_analog(int(charge / 25 * 1023))
            pin2.write_digital(0)
            pin8.write_digital(0)
            pin12.write_digital(0)


if __name__ == "__main__":
    main()
