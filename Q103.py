# Write a script that gets the current date and time and formats it as YYYY-MM-DD HH:MM:SS.
from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Format the date and time as YYYY-MM-DD HH:MM:SS
formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

# Print the formatted date and time
print("Current date and time:", formatted_datetime)