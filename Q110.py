# Write a script that uses the logging module to log debug, info, warning, and error messages to a file.
import logging

# Configure the logging
logging.basicConfig(
    filename='app.log',  # Log messages will be written to this file
    filemode='w',        # 'w' to overwrite the file each time, 'a' to append
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log message format
    level=logging.DEBUG   # Set the logging level to DEBUG
)

# Log messages of different severity levels
logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")

# Example of logging an exception
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    logging.error("An error occurred: %s", e)

print("Logging complete. Check 'app.log' for the logged messages.")