import time
from datetime import datetime
import Adafruit_CharLCD as LCD
import tempread




if __name__ == "__main__":
    print "this rug really pulls the room together"
    # Initialize the LCD using the pins
    lcd = LCD.Adafruit_CharLCDPlate()
    while True:
        lcd.set_color(1.0, 0.0, 0.0)
        lcd.clear()
        temp_c, temp_f =tempread.read_temp()
        temp_f_message="{0} F".format(temp_f)
        temp_c_message="{0} C".format(temp_c)
        print temp_f
        lcd.message(temp_f_message)
        time.sleep(5)
        print temp_c
        lcd.message(temp_c_message)
        time.sleep(5)
        lcd.set_color(0.0, 0.0, 1.0)
        #now = datetime.now()
        date_message=datetime.now().strftime("%Y-%m-%d")
        print date_message
        lcd.message(date_message)
        time.sleep(5)
