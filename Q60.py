# Read data from a JSON file, modify a value, and write the updated data back to the file.
import json
file_path = 'data.json'
try:
    with open(file_path, 'r') as file:
        data = json.load(file)
    print("Original data:", data)
    data['name'] = 'Updated Name' 
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    print("Updated data written to the file.")

except FileNotFoundError:
    print(f"Error: The file '{file_path}' does not exist.")
except json.JSONDecodeError:
    print("Error: Failed to decode JSON from the file.")
except Exception as e:
    print(f"An error occurred: {e}")