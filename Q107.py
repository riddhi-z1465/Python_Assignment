# Write a script that reads a JSON file, modifies a value, and writes the updated data back to the file.
import json

# Sample JSON data to write to a file (for demonstration purposes)
sample_data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Write the sample data to a JSON file
with open('data.json', 'w') as json_file:
    json.dump(sample_data, json_file, indent=4)

# Read the JSON data from the file
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

# Print the original data
print("Original data:", data)

# Modify a value in the JSON data
data['age'] = 31  # Update the age

# Write the updated data back to the JSON file
with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

# Print the updated data
print("Updated data:", data)