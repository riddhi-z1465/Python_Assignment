# Prompt for a string s and a substring sub. Check if sub is present in s.
s = input("Enter the main string: ")
sub = input("Enter the substring to check: ")
if sub in s:
    print(f"The substring '{sub}' is present in the string.")
else:
    print(f"The substring '{sub}' is not present in the string.")