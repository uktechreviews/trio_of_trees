from time import sleep
from machine import Pin
from random import randint

def clear_leds(led_array):
    for i in led_array:
        Pin(i,Pin.OUT).low()
        
def static_leds(led_array):
    for i in led_array:
        Pin(i,Pin.OUT).high()

def flash_leds(led_array,time):
    for i in led_array:
        Pin(i, Pin.OUT).high()
        sleep (time)
    for i in led_array:
        Pin(i,Pin.OUT).low()

def random_leds(time,repeat):
    for i in range (0,repeat):
        led = randint(0,14)
        if led == 2 or led == 7 or led == 12:
            repeat = repeat + 1
            pass
        else:
            Pin(led, Pin.OUT).high()
            sleep(time)
            Pin(led, Pin.OUT).low()
#             print (i) 
        

top_leds  = [2,7,12]
middle_leds = [1,3,6,8,11,13]
bottom_leds = [0,4,5,9,10,14]

all_leds = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

clear_leds(all_leds)

while True:
    choice = randint(1,3)
    print ("choice",choice)
    if choice == 1:
        clear_leds(all_leds)
        for repeat in range (4):
            print (repeat)
            flash_leds(top_leds,0.1)
            flash_leds(middle_leds,0.1)
            flash_leds(bottom_leds,0.1)
    if choice == 2:
        repeat = randint(20,40)
        random_leds(0.1,repeat)
    if choice == 3:
        clear_leds(all_leds)
        static_leds(top_leds)
        static_leds(middle_leds)
        static_leds(bottom_leds)
        sleep(3)
        clear_leds(all_leds)
    
    