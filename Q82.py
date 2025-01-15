# Write a program that finds the longest word in a text file and prints it.
def find_longest_word(filename):
    """Find the longest word in the specified file and print it."""
    try:
        longest_word = ""
        with open(filename, 'r') as file:
            for line in file:
                words = line.split()  # Split the line into words
                for word in words:
                    # Update longest_word if the current word is longer
                    if len(word) > len(longest_word):
                        longest_word = word
        if longest_word:
            print(f"The longest word is: {longest_word}")
        else:
            print("The file is empty or contains no words.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Example usage
if __name__ == "__main__":
    filename = 'example.txt'  # Replace with your file name
    find_longest_word(filename)