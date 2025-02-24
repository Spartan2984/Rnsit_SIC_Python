import numpy as np
# Explanation: np.arange() generates numbers starting at 1, stopping before 10, with step size 3

sequence = np.arange(1, 10, 3)
print(sequence)  # Output: [ 1  4  7]


# Generating 23 equally spaced values between 0 and 100

# Explanation: Using np.linspace() to generate specified number of values in a range

values = np.linspace(0, 100, 23)
print("Generated values:", values)
print("Total count:", len(values))