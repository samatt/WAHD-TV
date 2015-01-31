#!/usr/local/bin/python
import subprocess
import os
import random
import time

def getNewFile():
		images = os.listdir('./images')
		img =  random.choice(images)
   		print './images/'+ img
   		return 'images/'+ img 

if __name__ ==  '__main__':

	while True: 
		fileName = getNewFile()
		print fileName
		p1 = subprocess.Popen(['python', 'ntscEncode.py',fileName])
		p2 = subprocess.Popen(['python', 'ntsc_hackrf.py'])
		time.sleep(4)
		p2.kill()

		print "HEREEEEE"
		