#!/usr/bin/python

import sys
import os
import subprocess
import importlib
import argparse
from time import *
from machinekit import launcher

launcher.register_exit_handler()
#launcher.set_debug_level(5)
os.chdir(os.path.dirname(os.path.realpath(__file__)))

parser = argparse.ArgumentParser(description='This is the CRAMPS2-vel run script '
                                 'it demonstrates how a run script could look like '
                                 'and of course starts the CRAMPS2-vel config')

parser.add_argument('-v', '--video', help='Starts the video server', action='store_true')

args = parser.parse_args()

try:
    launcher.check_installation()
    launcher.cleanup_session()
    #launcher.load_bbio_file('cramps2_cape.bbio')
    #launcher.install_comp('e_check.comp')
    launcher.start_process("configserver -n ICON5D ../Machineface-old ../Cetus")
    if args.video:
        launcher.start_process('videoserver --ini video.ini Webcam1')
	launcher.start_process ('sudo chmod go+rw /dev/input/event1')
    launcher.start_process('linuxcnc CRAMPS-mouse.ini')
except subprocess.CalledProcessError:
    launcher.end_session()
    sys.exit(1)

while True:
    sleep(1)
    launcher.check_processes()
