import random

import music

from microbit import *

BUTTON_A = "A"
BUTTON_B = "B"


class Main:
    def __init__(self):
        self._debounce = {BUTTON_A: False, BUTTON_B: False}
        self._buttons = {BUTTON_A: button_a, BUTTON_B: button_b}
        self._reset_goal()
        compass.calibrate()
        display.show(Image.HAPPY)

    def main(self):
        while True:
            self._forever()

    def _forever(self):
        direction = compass.heading()
        difference = abs(self.goal - direction)
        self._blink(difference)
        if self._rising_edge(BUTTON_A):
            if difference < 15:
                display.scroll("Winner")
                self._reset_goal()
            else:
                display.scroll("Nope")

    def _blink(self, difference):
        pin0.write_digital(1)
        sleep(difference * 5)
        pin0.write_digital(0)
        sleep(difference * 5)

    def _reset_goal(self):
        self.goal = random.randint(0, 360)

    def _rising_edge(self, button: str):
        real_button = self._buttons[button]
        if real_button.is_pressed() and not self._debounce[button]:
            self._debounce[button] = True
            return True
        elif not real_button.is_pressed():
            self._debounce[button] = False
        return False


if __name__ == "__main__":
    Main().main()
