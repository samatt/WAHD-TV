#!/bin/bash

SRC_IMG="potrait.png"

if [ $# -eq 1 ] 
then
	SRC_IMG=$1
	echo "Using image : " + $SRC_IMG
else
	echo "Using default image : " + $SRC_IMG
fi

python ntscEncode.py $SRC_IMG
python ntsc_hackrf.py