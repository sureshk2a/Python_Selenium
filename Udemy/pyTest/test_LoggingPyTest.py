# create formatter (logging.formatter(<>))
# create filehandler (logging.filehandler(<path lofg file>))
# connect formatter to file handler (filehandler.setformatter(<formatter>))
# connect filehandler to logger using (addhandler)
import logging


def test_LoggingDemo():
    logger = logging.getLogger(__name__)

    formatter = logging.Formatter(
        "%(asctime)s :%(levelname)s : %(name)s : %(message)s")  # asctime,levelname,name,message will be taken in runtime

    fileHandler = logging.FileHandler("lgofile.log")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)  # filehandler object should be passed here, to save logs in file

    logger.setLevel(logging.DEBUG)  # Define the level of from u need to see the log
    logger.debug("This is a debug statement")
    logger.info("Information Statement")
    logger.warning("This is a warning")
    logger.error("This is an error")
    logger.critical("This is critical")
