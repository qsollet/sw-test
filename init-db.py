from database import init_db
import time
import logging

# Not great but allows to wait until the db is ready to accept connections
while True:
    try:
        init_db()
        logging.info('DB is ready')
        break
    except Exception as e:
        logging.warning('DB not ready... waiting')
        time.sleep(1)
