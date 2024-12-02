# import the logging module
# import os
import logging
import os

# set up the logging module 
def logger():
    """
    The central logging module of the PyREF.

    Sets up a central logger used in each core function.

    Return:
        log: logger
    """

    if not os.path.exists('PyREF/Data/Output'):
        os.mkdir('PyREF/Data/Output')

    log = logging.getLogger('PyREF')
    log.setLevel(logging.DEBUG)

    logHandle = logging.FileHandler(
                'PyREF/Data/Output/PyREF_log.log',
                encoding="utf-8",
                mode="a"
                )
    
    logFormat = logging.Formatter(
                "{asctime} - {levelname} - {message}",
                style="{",
                datefmt="%Y-%m-%d %H:%M:%S"
                )
    
    logHandle.setFormatter(logFormat)
    log.addHandler(logHandle)
    return log