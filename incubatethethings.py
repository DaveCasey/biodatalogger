from timelapse import BioTimeLapse
import Adafruit_CharLCD
import tempread
from biodatalogger import Collector
import time
from datetime import datetime


if __name__ == "__main__":
    print "this rug really pulls the room together"
    collector=Collector()
    biocam = BioTimeLapse()
    album=biocam.create_album()
    album_url="album url is http://imgur.com/a/{0}".format(album['id'])
    #print album_url
    album_hash=album['deletehash']
    while True:
        image_url=biocam.single_capture(album_hash)
        #album_hash="foo"
        #image_url="http://google.com"
        temp_c, temp_f =tempread.read_temp()
        now = datetime.now()
        data=[now, temp_c, temp_f, album_url, image_url]
        #print data
        collector.save_console(data)
        collector.save_csv(data)
        collector.save_thingspeak(data)
        time.sleep(1800)
