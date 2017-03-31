#!/usr/bin/env python
#-*-conding:utf-8-*-

import logging

'''
logging.basicConfig(filename='example.log',level=logging.INFO,format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
'''

#create logger
logger = logging.getLogger('TEST-LOG')
logger.setLevel(logging.DEBUG)


# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create file handler and set level to warning
fh = logging.FileHandler("access.log")
fh.setLevel(logging.WARNING)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch and fh
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add ch and fh to logger
logger.addHandler(ch)
logger.addHandler(fh)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')


