from machine import Pin 
from utime import sleep

led = Pin(5,Pin.OUT)

while True:
  led.on()
  sleep(3)
  led.off()
  sleep(3)