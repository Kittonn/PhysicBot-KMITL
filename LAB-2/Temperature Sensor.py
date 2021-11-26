from machine import ADC 
from utime import sleep

temp = ADC(28)

while True:
  temp_read = temp.read_u16()
  print(temp_read)
  sleep(1)