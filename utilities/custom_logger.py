import logging
import inspect


def customlogger(loglevel):

    loggername = inspect.stack()[1][3]
    logger = logging.getLogger(loggername)
    logger.setLevel(logging.DEBUG)

    filehandler = logging.FileHandler("{0}.log".format(loggername), mode="a")
    filehandler.setLevel(loglevel)

    formatter = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s',
                                  datefmt='%d/%m/%Y %H:%M:%S')

    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)

    return logger























