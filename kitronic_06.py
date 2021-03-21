import music

from microbit import *

BUTTON_A = "A"
BUTTON_B = "B"


class Main:
    def __init__(self):
        self._debounce = {BUTTON_A: False, BUTTON_B: False}
        self._buttons = {BUTTON_A: button_a, BUTTON_B: button_b}

    def main(self):
        while True:
            self._forever()

    def _forever(self):
        if self._rising_edge(BUTTON_A):
            music.pitch(400, 500)
        elif self._rising_edge(BUTTON_B):
            music.play(
                [
                    "b",
                    "b",
                    "b",
                    "g",
                    "a:12",
                    "a:4",
                    "a",
                    "a",
                    "f#",
                    "g",
                    "g",
                    "a",
                    "b",
                    "g",
                    "g",
                    "g",
                    "e",
                    "f#",
                    "a",
                    "g",
                    "f#",
                    "b",
                    "g",
                    "f#",
                    "e",
                    "f#:8",
                    "d:8",
                    "e:12",
                ]
            )

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
