import logging
import os
from datetime import datetime

datetimeFormat = '%d/%m/%Y %H:%M:%S'
log_file = "{datetime.now().strftime({datetimeFormat})}.log"

log_path = os.path.join(os.getcwd(),"logs")
os.makedirs(log_path,exist_ok=True)

# joining log path and log file
log_pathFile = os.path.join(log_path, log_file)

logging.basicConfig(level= logging.INFO,
                    filename= log_pathFile,
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s")