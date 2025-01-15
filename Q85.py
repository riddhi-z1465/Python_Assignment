# Write a Python script to read a CSV file and print each row.
import csv

class CSVReader:
    def __init__(self, filename):
        self.filename = filename  # Store the filename

    def read_csv(self):
        """Read the CSV file and print each row."""
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)  # Print each row
        except FileNotFoundError:
            print(f"Error: The file '{self.filename}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Create an instance of CSVReader with the filename
    csv_reader = CSVReader('example.csv')  # Replace 'example.csv' with your CSV file path

    # Read and print the CSV file
    csv_reader.read_csv()