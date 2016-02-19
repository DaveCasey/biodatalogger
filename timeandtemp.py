import time
from datetime import datetime
import Adafruit_CharLCD as LCD
import tempread




if __name__ == "__main__":
    print "this rug really pulls the room together"
    # Initialize the LCD using the pins
    lcd = LCD.Adafruit_CharLCDPlate()
    lcd.set_color(0.0, 0.0, 1.0)
    lcd.clear()
    while True:
        temp_c, temp_f =tempread.read_temp()
        temp_message="{0:3.1f} F {1:3.1f} C\n".format(temp_f, temp_c)
        lcd.message(temp_message)
        date_message=datetime.now().strftime("%H:%M:%S %Y-%m-%d ")
        lcd.message(date_message)
        time.sleep(1)
