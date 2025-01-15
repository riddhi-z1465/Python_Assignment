# Demonstrate various string slicing operations (e.g., reverse a string, skip letters).
original_string = "Hello, World!"

first_five = original_string[:5]
print("First five characters:", first_five)

from_index_7 = original_string[7:]
print("String from index 7 to end:", from_index_7)

reversed_string = original_string[::-1]
print("Reversed string:", reversed_string)

every_second_character = original_string[::2]
print("Every second character:", every_second_character)

last_five = original_string[-5:]
print("Last five characters:", last_five)

every_third_character = original_string[::3]
print("Every third character:", every_third_character)