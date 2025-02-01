# Function to convert integer to binary string
def int_to_binary(integer):
    return bin(integer)[2:]  # Remove the '0b' prefix


# Example usage
integer_value = int(input("Enter a decimal integer: "))  # Get user input
result = int_to_binary(integer_value)
print(f"The binary value of integer {integer_value} is {result}.")
