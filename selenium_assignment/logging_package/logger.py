import time
import logging
current_time = time.strftime("%Y%m%d-%H%M%S")


def create_logfile():
    logging.basicConfig(level=logging.INFO, filename="../logs/logfile_" + current_time + ".log")


def create_log(log_level, log_message):
    logging.log(log_level, log_message)
