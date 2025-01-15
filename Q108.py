# Write a program (assuming you have internet access) that fetches data from a public API using the requests module and prints part of the JSON response.
import requests

# URL of the public API
url = 'https://jsonplaceholder.typicode.com/users/1'

# Sending a GET request to the API
response = requests.get(url)

# Checking if the request was successful
if response.status_code == 200:
    # Parsing the JSON response
    user_data = response.json()
    
    # Printing specific parts of the JSON response
    print("User  Information:")
    print(f"Name: {user_data['name']}")
    print(f"Email: {user_data['email']}")
    print(f"City: {user_data['address']['city']}")
else:
    print(f"Failed to retrieve data: {response.status_code}")