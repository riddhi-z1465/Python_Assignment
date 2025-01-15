# Write a script that demonstrates the difference between a list comprehension and a generator expression for large data.
import time

n = 10**7  # Large number for demonstration

# Timing list comprehension
start_time = time.time()
list_result = [x * 2 for x in range(n)]  # Create a list using list comprehension
end_time = time.time()
print(f"List comprehension created a list of {len(list_result)} elements in {end_time - start_time:.4f} seconds.")

# Timing generator expression
start_time = time.time()
gen_result = (x * 2 for x in range(n))  # Create a generator using generator expression
# To consume the generator, we can convert it to a list
gen_list = list(gen_result)  # Convert generator to list to consume it
end_time = time.time()
print(f"Generator expression created a generator in {end_time - start_time:.4f} seconds.")
print(f"Generator produced {len(gen_list)} elements.")