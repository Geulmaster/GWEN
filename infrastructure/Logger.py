import logging

log = logging.getLogger()

console = logging.StreamHandler()
log.addHandler(console)

def warn(msg):
    print(log.warn(msg))

def info(msg):
    print(log.info(msg))

def error(msg):
    print(log.error(msg))