import logging

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')
logger_db = logging.getLogger('database')
logger_db.setLevel(logging.INFO)
logger_repo = logging.getLogger('repository')
logger_repo.setLevel(logging.INFO)