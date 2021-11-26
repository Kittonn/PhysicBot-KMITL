from machine import ADC 
from utime import sleep

ldr = ADC(28)

while True:
  ldr_read = ldr.read_u16()
  print(ldr_read)
  sleep(1)