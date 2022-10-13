#!/bin/bash

usrname="manideep"
IP="192.168.53.233"

path="/home/$usrname/FWC/arm"

cd boolean/GCC_Project
make

scp output/bin/boolean.bin $usrname@$IP:$path

cd ../../docs
texfot pdflatex arm.tex

cp arm.pdf /sdcard/FWC/arm 
