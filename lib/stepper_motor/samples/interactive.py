import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core import StepperMotor
import curses

DIR = 20
STEP = 21
MODE = (14,15,18)

stdscr = curses.initscr()
stdscr.keypad(True)
curses.cbreak()
curses.noecho()
distance = 0

try:
    motor = StepperMotor(DIR, STEP, MODE, '1/32', 0.001)
    while True:
        key = stdscr.getkey()
        if key == "KEY_LEFT":
            motor.doStep(StepperMotor.CCW, 2 ** distance)
        elif key == "KEY_RIGHT":
            motor.doStep(StepperMotor.CW, 2 ** distance)
        elif key == "KEY_UP":
            if distance < 10:
                distance += 1
            print(distance)
        elif key == "KEY_DOWN":
            if distance > 0:
                distance -= 1
            print(distance)
except Exception as e:
    print(e)
finally:
    curses.endwin()
