##ADXL377 driver attempt

from machine import ADC
from machine import Pin

xpin = 32
ypin = 33
zpin = 34

xadc = ADC(Pin(xpin))
yadc = ADC(Pin(ypin))
zadc = ADC(Pin(zpin))

xadc.atten(ADC.ATTN_11DB)
yadc.atten(ADC.ATTN_11DB)
zadc.atten(ADC.ATTN_11DB)

xAccel = (-200.0)+(400.0*(xadc.read()/3754))
yAccel = (-200.0)+(400.0*(yadc.read()/3754))
zAccel = (-200.0)+(400.0*(zadc.read()/3754))
