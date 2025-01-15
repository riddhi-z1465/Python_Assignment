# Use the statistics module to compute the mean, median, and mode of a list of numbers.
import statistics

# Sample list of numbers
numbers = [10, 20, 20, 30, 40, 50, 50, 50, 60, 70]

# Calculate mean
mean_value = statistics.mean(numbers)
print(f"Mean: {mean_value}")

# Calculate median
median_value = statistics.median(numbers)
print(f"Median: {median_value}")

# Calculate mode
try:
    mode_value = statistics.mode(numbers)
    print(f"Mode: {mode_value}")
except statistics.StatisticsError as e:
    print(f"Mode: {e}")  # Handle case where there is no unique mode