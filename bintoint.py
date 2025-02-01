def binary_to_int(binary_str):
    return int(binary_str, 2)


binary_string = input("Your binary int: ")  # Binary input.
result = binary_to_int(binary_string)  # Gets the result ready.
print(f"The integer int of binary {binary_string} is {result}.")  # Tells the integer.
