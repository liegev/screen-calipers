#!/usr/bin/env python3
"""Screen calipers: read mouse positions and measure distances on screen, in pixels.

Handy for checking a UI mockup, a scanned drawing or a panel layout against the
real thing without opening an image editor.
"""
import math
import os
import sys

try:
    import pyautogui
except ImportError:
    sys.exit("screen-calipers needs pyautogui:  pip install pyautogui")

MENU = """
 Screen calipers
 ---------------
  l   live position (absolute)
  lc  live position from an origin you pick with the mouse
  lo  live position from an origin you type in
  d   distance between two points
  q   quit

 Ctrl+C returns to this menu.
"""


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def live(ox=0, oy=0):
    """Print the pointer position relative to (ox, oy) until Ctrl+C."""
    while True:
        x, y = pyautogui.position()
        s = f"X: {x - ox:5d}  Y: {y - oy:5d}"
        print(s + "\b" * len(s), end="", flush=True)


def pick_origin():
    input(" Put the pointer on the origin and press Enter ")
    return pyautogui.position()


def type_origin():
    return int(input(" origin x: ")), int(input(" origin y: "))


def distance():
    while True:
        input(" Pointer on the first point, press Enter ")
        x1, y1 = pyautogui.position()
        input(" Pointer on the second point, press Enter ")
        x2, y2 = pyautogui.position()
        dx, dy = x2 - x1, y2 - y1
        print(f"  dx = {dx}   dy = {dy}   diagonal = {math.hypot(dx, dy):.1f}\n")


def main():
    choice = ""
    while choice != "q":
        clear()
        print(MENU)
        choice = input(" > ").strip().lower()
        try:
            if choice == "l":
                live()
            elif choice == "lc":
                live(*pick_origin())
            elif choice == "lo":
                live(*type_origin())
            elif choice == "d":
                distance()
        except KeyboardInterrupt:
            pass
    clear()


if __name__ == "__main__":
    main()
