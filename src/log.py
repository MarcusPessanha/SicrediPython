import os

def log_debug(msg):
    if os.environ.get('SICREDI_DEBUG', None):
        print(msg)
