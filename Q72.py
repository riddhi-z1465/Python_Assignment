# Write a recursive function that returns the number of vowels in a string.
def count_vowels(s):
    """Count the number of vowels in a string using recursion."""
    # Base case: if the string is empty, return 0
    if not s:
        return 0
    
    # Check if the first character is a vowel
    first_char = s[0].lower()  # Convert to lowercase for case-insensitive comparison
    if first_char in 'aeiou':
        return 1 + count_vowels(s[1:])  # Count this vowel and recurse on the rest of the string
    else:
        return count_vowels(s[1:])  # Just recurse on the rest of the string

# Example usage
if __name__ == "__main__":
    user_input = input("Enter a string to count the vowels: ")
    vowel_count = count_vowels(user_input)
    print(f"The number of vowels in the string is: {vowel_count}")