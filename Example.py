#from machine import Pin, ADC
#from utime import sleep

#led = Pin(16,Pin.OUT)

#while True:
#  led.value(1) #led.on()
#  sleep(0.5)
#  led.value(0) #led.off()
#  sleep(0.5)

#ldr = ADC(26)


#while True:
#  ldr_read = ldr.read_u16()
#  print(ldr_read)
#  if (ldr_read > 45000):
#   led.value(1)
#   print('LED ON!!!!')
#  else: 
#    led.value(0)
#    print('LED OFF!!!!')
#  sleep(0.5)
  
#temp = ADC(27)

#27000 hot
#37000 cold

#while True:
#  temp_read = temp.read_u16()
#  print(temp_read)
#  if (temp_read > 37000):
#    print("cold")
#  elif (temp_read < 27000):
#    print('hot')
#  else:
#    print('General')
#  sleep(0.5)

#from machine import ADC, Pin
#import utime
#
#while True:
#  trig = Pin(15,Pin.OUT)
#  trig.off()
#  utime.sleep_us(2)
#  trig.on()
#  utime.sleep_us(10)
#  trig.off()
#  echo = Pin(14,Pin.IN)
#
#  while echo.value() == 0:
#    pass
#  t1 = utime.ticks_us()
#  while echo.value() == 1:
#    pass
#  t2 = utime.ticks_us()
#  cm = int((t2-t1) / 58.0)
#  #1 in = 2.54 cm
#  print(cm /2.54, 'in')
#  utime.sleep(2)
