# Given a string, count how many vowels (a, e, i, o, u) it contains.
input_string = input("Enter a string: ")

vowels = "aeiouAEIOU"  
vowel_count = 0
for char in input_string:
    if char in vowels:  
        vowel_count += 1  
print("Number of vowels in the string:", vowel_count)