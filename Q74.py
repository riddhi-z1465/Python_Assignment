# Write a recursive function that checks if a string is a palindrome.
def is_palindrome(s):
    """Check if a string is a palindrome using recursion."""
    # Base case: if the string is empty or has one character
    if len(s) <= 1:
        return True
    # Check the first and last characters
    if s[0] != s[-1]:
        return False
    # Recursive case: check the substring excluding the first and last characters
    return is_palindrome(s[1:-1])

# Example usage
if __name__ == "__main__":
    user_input = input("Enter a string to check if it's a palindrome: ")
    # Remove spaces and convert to lowercase for a more robust check
    cleaned_input = user_input.replace(" ", "").lower()
    if is_palindrome(cleaned_input):
        print(f'"{user_input}" is a palindrome.')
    else:
        print(f'"{user_input}" is not a palindrome.')