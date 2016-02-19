#!/usr/bin/env python

import picamera
import time
import os
import ConfigParser
from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError
from datetime import datetime

# Read globals
CONFIG_FILE = 'timelapse.ini'
CONFIG = ConfigParser.ConfigParser()
CONFIG.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), CONFIG_FILE))

TIMELAPSE_IMAGE_DIR = CONFIG.get('global', 'timelapse_image_dir')
IMGUR_ID = CONFIG.get('global', 'imgur_id')
IMGUR_TOKEN = CONFIG.get('global', 'imgur_token')


class BioTimeLapse(object):
    def create_album(self):
        try:
            album_fields={'title':'familabincubator','description':'familabincubator','privacy':'public'}
            #allowed_album_fields = {'ids', 'title', 'description', 'privacy', 'layout', 'cover'}
            client = ImgurClient(IMGUR_ID,IMGUR_TOKEN)
            album_url=client.create_album(album_fields)
            return album_url
        except ImgurClientError, error:
            if (("InsecurePlatformWarning" in error.error_message) or ("SNIMissingWarning" in error.error_message)):
                print "there was an ssl warning, mitm may rickroll your images"
            else:
                print error.error_message, error.status_code
    def generate_filename(self):
        return '/home/pi/images/diybio_{0}.jpg'.format(datetime.now().strftime("%Y-%m-%d_%H_%M_%S.%f"))
    def upload_imgr(self, filename,albumhash):
        try:
	    config = {'album': albumhash,'name':'famibio','title': 'familabincubator','description': 'Cute organisms being cute on {0}'.format(datetime.now())}

            client = ImgurClient(IMGUR_ID,IMGUR_TOKEN)
            image_url=client.upload_from_path(filename,config=config,anon=False)
            return image_url
        except ImgurClientError, error:
            if (("InsecurePlatformWarning" in error.error_message) or ("SNIMissingWarning" in error.error_message)):
                print "there was an ssl warning, mitm may rickroll your images"
            else:
                print error.error_message, error.status_code

    def start_capture(self, album_hash = '', seconds = 60, cycles = 100):
        for i in range(cycles):
            filename = self.generate_filename()
            with picamera.PiCamera() as camera:
                camera.capture(filename)
            result_url=self.upload_imgr(filename,albumhash)
            print("You can find it here: {0}".format(result_url['link']))
            time.sleep(seconds)

    def single_capture(self, album_hash = '', seconds = 60, cycles = 100):
        filename = self.generate_filename()
        with picamera.PiCamera() as camera:
            camera.capture(filename)
        result_url=self.upload_imgr(filename,album_hash)
        print("You can find it here: {0}".format(result_url['link']))
        return result_url

if __name__ == "__main__":
    biocam = BioTimeLapse()
    albumname=biocam.create_album()
    print("album name is {0}".format(albumname['deletehash']))
    print("album url is http://imgur.com/a/{0}".format(albumname['id']))
    print(albumname)
    albumhash=albumname['deletehash']
    biocam.start_capture(albumhash)
