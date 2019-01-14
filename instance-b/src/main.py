import os.path
import time
import logging
import sys
import re

PATH_JSON_W = os.getenv('PATH_JSON_W', './bucket-w/')

def logger():

    global log
    log = logging.getLogger(__name__)
    out_hdlr = logging.StreamHandler(sys.stdout)
    out_hdlr.setFormatter(logging.Formatter('%(asctime)s [%(funcName)s] [%(levelname)-5.5s] %(message)s'))
    out_hdlr.setLevel(logging.INFO)
    log.addHandler(out_hdlr)
    log.setLevel(logging.INFO)
    return log

def waitfile():
    
    while True:
        files = [x for x in os.listdir(PATH_JSON_W) if x.endswith(".gpg")]
        time.sleep(1)
        if not files:
            log.info("File not found")
            time.sleep(10)
        else:
            log.info('File Found')
            for i in files:
                PATH_XML = PATH_JSON_W+i
                XML_FILE = re.sub('.gpg','',i)
                os.system('gpg --trust-model always --recipient pythonwithdocker@example.org --decrypt '+PATH_XML+ '>>'+PATH_JSON_W+XML_FILE)
                log.info("File Decrypted " + XML_FILE)
        break

if __name__ == '__main__':
    logger()
    waitfile()