# Modify the file-reading program to handle exceptions (e.g., file not found) gracefully.
def find_longest_word(filename):
    """Find the longest word in the specified file and print it."""
    longest_word = ""

    try:
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
    except IOError:
        print(f"Error: An I/O error occurred while reading the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    filename = 'example.txt'  # Replace with your file name
    find_longest_word(filename)