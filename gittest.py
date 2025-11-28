from picamera2 import Picamera2
from time import sleep

picam = Picamera2()

config = picam.create_still_configuration()
picam.configure(config)

picam.start()
sleep(1)

picam.capture_file("output.jpg")
picam.stop()

print("saved image")
