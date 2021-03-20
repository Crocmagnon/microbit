from microbit import *

SENSITIVITY = 250


def main():
    while True:
        x = accelerometer.get_x()
        y = accelerometer.get_y()

        image = get_image(x, y)
        display.show(image)


def get_image(x, y) -> Image:
    if x > SENSITIVITY:
        if y < -SENSITIVITY:
            image = Image.ARROW_NE
        elif y > SENSITIVITY:
            image = Image.ARROW_SE
        else:
            image = Image.ARROW_E
    elif x < -SENSITIVITY:
        if y < -SENSITIVITY:
            image = Image.ARROW_NW
        elif y > SENSITIVITY:
            image = Image.ARROW_SW
        else:
            image = Image.ARROW_W
    else:
        if y < -SENSITIVITY:
            image = Image.ARROW_N
        elif y > SENSITIVITY:
            image = Image.ARROW_S
        else:
            image = Image.CLOCK1
    return image


if __name__ == "__main__":
    main()
