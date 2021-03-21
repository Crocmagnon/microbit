from microbit import *

sun = Image("70707:09990:79997:09990:70707")
moon = Image("59000:05950:00990:05950:49000")


def main():
    while True:
        light = pin0.read_analog()
        if light < 200:
            display.show(moon)
        else:
            display.show(sun)


if __name__ == "__main__":
    main()
