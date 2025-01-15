# Use Python’s logging module to log info and error messages in a script.
import logging
logging.basicConfig(
    level=logging.DEBUG,  
    format='%(asctime)s - %(levelname)s - %(message)s', 
    filename='app.log', 
    filemode='w'  
)

logging.info("This is an informational message.")
try:

    result = 10 / 0  
except ZeroDivisionError as e:
    logging.error("An error occurred: %s", e)
logging.info("Script execution completed.")