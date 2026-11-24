import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

# Demonstrate different logging levels
logging.debug("This is a DEBUG message")
logging.info("This is an INFO message")
logging.warning("This is a WARNING message")
logging.error("This is an ERROR message")
logging.critical("This is a CRITICAL message")
'''
# Output:
# 2026-11-20 10:00:00 - DEBUG - This is a DEBUG message
# 2026-11-20 10:00:00 - INFO - This is an INFO message
# 2026-11-20 10:00:00 - WARNING - This is a WARNING message
# 2026-11-20 10:00:00 - ERROR - This is an ERROR message
# 2026-11-20 10:00:00 - CRITICAL - This is a CRITICAL message'''
