#!/usr/bin/python3

from gpiozero import LED
from signal import pause

ir = LED(22)
ir.on()
pause()
