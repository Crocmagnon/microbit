from microbit import *

sun = Image("90909:09990:99999:09990:90909")
moon = Image("59000:05990:00999:05990:49000")


def main():
    while True:
        if button_a.is_pressed():
            display.show(sun)
        elif button_b.is_pressed():
            display.show(moon)
        else:
            display.clear()


if __name__ == "__main__":
    main()
