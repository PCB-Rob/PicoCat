import ST7735S_128x128 as TFT
from machine import SPI,Pin, PWM

# height defaults to 160
TFT.ST7735_TFTHEIGHT = 128
spi = SPI(0, baudrate=20000000, polarity=0, phase=0, sck=Pin(2), mosi=Pin(3), miso=Pin(4))
# move image 3 pixels across and down
# RGB is reversed = c_mode fixes that
tft=TFT.ST7735(spi, rst=6, ce=5, dc=7, offset=3, c_mode='BGR') 
pwm0 = PWM(Pin(0), freq=2000, duty_u16=32768)

tft.reset()
tft.begin()
tft._bground = 0xffff
tft.fill_screen(tft._bground)