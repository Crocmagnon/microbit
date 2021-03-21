import random

from microbit import *


def main():
    wait_for_ready()
    while True:
        countdown()
        winner = game()
        display_winner(winner)
        wait_for_ready()


def display_winner(winner):
    display.show(winner)
    sleep(2000)
    display.show(Image.HAPPY)


def game():
    wait = random.randint(1, 10) * 1000
    sleep(wait)
    display.show("!")
    while True:
        if button_a.is_pressed():
            winner = "A"
            break
        elif button_b.is_pressed():
            winner = "B"
            break
    return winner


def wait_for_ready():
    display.scroll("A or B...")
    while True:
        if button_a.is_pressed() or button_b.is_pressed():
            break


def countdown():
    display.show("3")
    sleep(1000)
    display.show("2")
    sleep(1000)
    display.show("1")
    sleep(1000)
    display.scroll("...")
    display.clear()


if __name__ == "__main__":
    main()
