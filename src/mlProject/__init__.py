import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"  #custome logging string format

log_dir = "logs"    #creates a directory named logs
log_filepath = os.path.join(log_dir,"running_logs.log")  #inside directory create a log file named running_logs.log"
os.makedirs(log_dir, exist_ok=True)


'''
    
logging configuration starts from the below

'''

logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),  #file handler saves the log message in the log file
        logging.StreamHandler(sys.stdout)  #stream handler shows the log message in terminal
    ]
)

logger = logging.getLogger("mlProjectLogger")  