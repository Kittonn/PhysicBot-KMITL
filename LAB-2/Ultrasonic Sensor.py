from machine import ADC, Pin
import utime

while True:
  trig = Pin(7,Pin.OUT)
  trig.off()
  utime.sleep_us(2)
  trig.on()
  utime.sleep_us(10)
  trig.off()
  echo = Pin(6,Pin.IN)

  while echo.value() == 0:
    pass
  t1 = utime.ticks_us()
  while echo.value() == 1:
    pass
  t2 = utime.ticks_us()
  cm = (t2-t1) / 58.0
  print(cm, 'cm')
  utime.sleep(2)