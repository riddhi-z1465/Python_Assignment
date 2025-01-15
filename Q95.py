# Create a class Counter with a class variable count. Implement a @classmethod to increment count and a @staticmethod to display some utility message.
class Counter:
    count = 0  # Class variable to keep track of the count

    @classmethod
    def increment_count(cls):
        """Increment the class variable count."""
        cls.count += 1

    @staticmethod
    def display_message():
        """Display a utility message."""
        return "This is a utility message from the Counter class."

# Example usage
if __name__ == "__main__":
    # Display the initial count
    print(f"Initial count: {Counter.count}")

    # Increment the count using the class method
    Counter.increment_count()
    print(f"Count after incrementing: {Counter.count}")

    # Increment the count again
    Counter.increment_count()
    print(f"Count after another increment: {Counter.count}")

    # Display a utility message using the static method
    message = Counter.display_message()
    print(message)