from microbit import *

SENSITIVITY = 10


while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()

    if x > SENSITIVITY and y > SENSITIVITY:
        image = Image.ARROW_NE
    elif x > SENSITIVITY and y < -SENSITIVITY:
        image = Image.ARROW_SE
    elif x > SENSITIVITY:
        image = Image.ARROW_E
    else:
        image = None

    display.show(image)
