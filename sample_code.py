from time import sleep
from machine import Pin

i=0

while True:
    Pin (i,Pin.OUT).high()
    sleep(0.5)
    Pin (i,Pin.OUT).low()
    i = i+1
    if i>14: i=0