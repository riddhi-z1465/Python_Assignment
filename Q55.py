# Write a script that reads a CSV file and prints each row. (Assume the file exists and is properly formatted.)
import csv

# Specify the path to the CSV file
file_path = 'data.csv'  # Change this to your CSV file path

# Open the CSV file and read its content
with open(file_path, mode='r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Iterate through each row in the CSV file
    for row in csv_reader:
        print(row)  # Print the current row