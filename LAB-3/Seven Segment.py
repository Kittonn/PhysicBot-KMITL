from machine import Pin
from utime import sleep

#       A
#     ------
#   F | G | B
#     ------
#   E |   | C
#     ------
#       D


A = Pin(2, Pin.OUT)
#B = Pin(3, Pin.OUT)
#C = Pin(4, Pin.OUT)
#D = Pin(5, Pin.OUT)
#E = Pin(6, Pin.OUT)
#F = Pin(7, Pin.OUT)
#G = Pin(8, Pin.OUT)

while True:
  A.on() 
  sleep(1)