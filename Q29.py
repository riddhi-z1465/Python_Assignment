# Convert a given distance in miles to kilometers and print the result.
miles = float(input("Enter the distance in miles: "))
conversion_factor = 1.60934
kilometers = miles * conversion_factor
print(f"The distance in kilometers is: {kilometers:.2f} km")