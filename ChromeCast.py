from __future__ import print_function
import time
import logging
import pychromecast
from pychromecast.controllers.youtube import YouTubeController

class CC_Build:

    def initialize(self):

        while True:
            try:
                IP = input('Enter your ChromeCast IP Address: ')
                cast = pychromecast.Chromecast(IP)
                print("Connected!")
                break
            except:
                print("Invalid ChromeCast IP Address")
                continue

        return cast


class CC_Controller:

    MEDIA_URL = "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"
    #MEDIA_URL = "file:///C:/Users/Capn/Desktop/22.mp4"    this doesn't work. chromecast doesn't do local files without some fuckery.
    MEDIA_TYPE = "video/mp4"
    global MC
    global CAST
    PlayPause = ["play","pause","pp","playpause"]
    CC_Kill = ["stop","kill","quit","exit","close","shutdown","off"]
    InsertMedia = ["load","insert","initialize","begin","start","go"]

    def initialize(self, myCast):

        self.CAST = myCast
        self.MC = self.CAST.media_controller
        self.deamonize()

    def play_media(self, url, type):
        print("play_media triggered")
        self.MC.play_media(url, type)

    def play_pause_toggle(self):
        print("play_pause_toggle triggered")
        if self.MC.status.player_state == "PLAYING":
            self.MC.pause()
        else:
            self.MC.play()

    def stop_CC(self):
        print("stop_CC triggered")
        self.MC.stop()

    def deamonize(self):
        #We need to change this method to create an actual deamon
        #I was lazy and used a while true until we know what a raspberry pi will need for a deamon

        while True:
            try:
                user_command = input('Enter a command: ')

                if str(user_command).lower() in self.PlayPause:
                    self.play_pause_toggle()

                elif str(user_command).lower() in self.InsertMedia:
                    self.play_media(self.MEDIA_URL, self.MEDIA_TYPE)

                elif str(user_command).lower() == "youtube":
                    yt = YouTubeController()
                    self.CAST.register_handler(yt)
                    yt.play_video('dQw4w9WgXcQ')

                elif str(user_command).lower() in self.CC_Kill:
                    self.stop_CC()
                    break

            except ValueError:
                print("Invalid Command")
                continue

#Builds the chromecast object
myCC = CC_Build()
myCast = myCC.initialize()

#Sends the chromecast object to the controller class
myController = CC_Controller()
myController.initialize(myCast)


#192.168.1.176




