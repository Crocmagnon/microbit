from microbit import *

LIMIT = 1020
STEP = 204

PIN8 = "PIN8"
PIN12 = "PIN12"
PIN16 = "PIN16"


class Main:
    def __init__(self):
        self._debounce = {PIN8: False, PIN12: False, PIN16: False}
        self._pins = {PIN8: pin8, PIN12: pin12, PIN16: pin16}
        self.red = 0
        self.green = 0
        self.blue = 0

    def main(self):
        while True:
            self._forever()

    def _forever(self):
        pin0.write_analog(self.red)
        pin1.write_analog(self.green)
        pin2.write_analog(self.blue)
        self._display_percents()

        self._update_color(PIN8, "green")
        self._update_color(PIN12, "red")
        self._update_color(PIN16, "blue")

    def _update_color(self, pin: str, color: str):
        if self._rising_edge(pin):
            color_value = getattr(self, color)
            if color_value < LIMIT:
                setattr(self, color, color_value + STEP)
            else:
                setattr(self, color, 0)

    def _display_percents(self):
        red_level = self._compute_level(self.red)
        green_level = self._compute_level(self.green)
        blue_level = self._compute_level(self.blue)
        red_row = self._compute_row(red_level)
        green_row = self._compute_row(green_level)
        blue_row = self._compute_row(blue_level)
        empty_row = "00000"
        display.show(
            Image(":".join([red_row, empty_row, green_row, empty_row, blue_row]))
        )

    @staticmethod
    def _compute_level(color):
        return int(color / LIMIT * 6)

    @staticmethod
    def _compute_row(color_level):
        return "9" * color_level + "0" * (5 - color_level)

    def _rising_edge(self, pin: str):
        real_pin = self._pins[pin]
        pin_value = real_pin.read_digital()
        if pin_value == 1 and not self._debounce[pin]:
            self._debounce[pin] = True
            return True
        elif pin_value != 1:
            self._debounce[pin] = False
        return False


if __name__ == "__main__":
    Main().main()
