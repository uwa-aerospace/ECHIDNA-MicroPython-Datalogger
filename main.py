import utime
import machine
import sdcard
import uos
#import max31865
import bmp280
import adxl345
import network

from machine import ADC, Pin, I2C, SPI

led = Pin(5, Pin.OUT)
led.value(0)

i2c = I2C(scl = Pin(22), sda = Pin(21), freq=400000)

bmp280 = bmp280.BMP280(i2c)
adxl345 = adxl345.ADXL345(i2c)

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid = "uPy Payload")

xpin = 34
ypin = 32
zpin = 34

xadc = ADC(Pin(xpin))
yadc = ADC(Pin(ypin))
zadc = ADC(Pin(zpin))

xadc.atten(ADC.ATTN_11DB)
yadc.atten(ADC.ATTN_11DB)
zadc.atten(ADC.ATTN_11DB)

spid = SPI(-1, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
sd = sdcard.SDCard(spid, Pin(4))
uos.mount(sd, '/sd')
uos.listdir('/sd')
with open('/sd/datalogger_output.txt', 'a') as o:
    o.write('')
o.close()

def sdClear():
    with open('/sd/datalogger_output.txt', 'w') as o:
        o.write('')
        print('SD card has been cleared!')

def unMount():
     with open('/sd/datalogger_output.txt', 'a') as o:
         o.close()
         uos.umount('/sd')
         print('SD card has been unmounted!')

def datalogger():
    
    while True:
        x1 = adxl345.xValue
        y1 = adxl345.yValue
        z1 = adxl345.zValue
        x2 = xadc.read()
        y2 = yadc.read()
        z2 = zadc.read()
        #t = bmp280.getTemp()
        dataset = x1, y1, z1, x2, y2, z2, utime.ticks_ms()
        
        with open('/sd/datalogger_output.txt', 'a') as o:
            o.write(str(dataset) + ',\n')