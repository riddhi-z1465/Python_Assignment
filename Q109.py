# Write a script that extracts all email addresses from a given string using the re module.
import re

# Sample string containing email addresses
text = """
Hello, you can reach out to us at support@example.com or sales@example.org.
For personal inquiries, contact john.doe123@gmail.com or jane_doe@company.co.uk.
Thank you!
"""

# Regular expression pattern for matching email addresses
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Extracting email addresses using re.findall
email_addresses = re.findall(email_pattern, text)

# Print the extracted email addresses
print("Extracted email addresses:")
for email in email_addresses:
    print(email)