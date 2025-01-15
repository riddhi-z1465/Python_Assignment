# Write a Python program that reads a file and counts the number of words in it.
def count_words_in_file(filename):
    """Count the number of words in the specified file and print the count."""
    try:
        with open(filename, 'r') as file:
            word_count = 0
            for line in file:
                words = line.split()  # Split the line into words
                word_count += len(words)  # Add the number of words in the line to the total count
        print(f"The file '{filename}' contains {word_count} words.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: An I/O error occurred while reading the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    filename = 'example.txt'  # Replace with your file name
    count_words_in_file(filename)