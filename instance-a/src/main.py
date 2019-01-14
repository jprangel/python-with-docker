#! /usr/bin/env python

import json
import os
import logging
import sys
import time
import subprocess
from dict2xml import dict2xml


PATH_JSON_R = os.getenv('PATH_JSON_R', '/home/jprangel/Documents/python-with-docker/instance-a/bucket-r/')
PATH_JSON_W = os.getenv('PATH_JSON_W', '/home/jprangel/Documents/python-with-docker/instance-a/bucket-w/')
IP_INSTB = os.getenv('IP_INSTB', '127.0.0.2')

def logger():

	global log

	log = logging.getLogger(__name__)
	out_hdlr = logging.StreamHandler(sys.stdout)
	out_hdlr.setFormatter(logging.Formatter('%(asctime)s [%(funcName)s] [%(levelname)-5.5s] %(message)s'))
	out_hdlr.setLevel(logging.INFO)
	log.addHandler(out_hdlr)
	log.setLevel(logging.INFO)

	return log

def convert():
     
    files = os.listdir(PATH_JSON_R)
    for i in files:
        log.info("Reading JSON files "+i)
        PATH_JSON = PATH_JSON_R+i
        READ_FILE = open(PATH_JSON, "r")
        XML_DATA = json.load(READ_FILE)
        XML_DATA_CONVERT = dict2xml(XML_DATA)
        NEW_NAMEFILE_XML = i+".xml"
        WRITE_FILE = open(PATH_JSON_W+NEW_NAMEFILE_XML,'w')
        WRITE_FILE.write(XML_DATA_CONVERT)
        READ_FILE.close()
        WRITE_FILE.close()

    encrypt()

def encrypt():

    time.sleep(60)
    files = os.listdir(PATH_JSON_W)
    for i in files:
        PATH_XML = PATH_JSON_W+i
        os.system('gpg --trust-model always --recipient pythonwithdocker@example.org --encrypt '+PATH_XML)
        log.info("File Encrypted " + i)
    
    send()

def send():

    files = [x for x in os.listdir(PATH_JSON_W) if x.endswith(".gpg")]
    print(files)
    for i in files:
        PATH_XML = PATH_JSON_W+i
        os.system('scp -r -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -i /root/.ssh/id_rsa /app/bucket-w/*.gpg root@'+IP_INSTB+':/app/bucket-w/')
        log.info("Sending Files Encrypted " + i)

if __name__ == '__main__':
   logger()
   convert()

