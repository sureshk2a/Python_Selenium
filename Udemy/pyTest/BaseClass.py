import inspect
import logging


class BaseClass:
    def test_LoggingDemo(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        formatter = logging.Formatter(
            "%(asctime)s :%(levelname)s : %(name)s : %(message)s")  # asctime,levelname,name,message will be taken in runtime

        fileHandler = logging.FileHandler("lgofile.log")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object should be passed here, to save logs in file

        logger.setLevel(logging.DEBUG)  # Define the level of from u need to see the log
        return logger
