import math

# Initialize variables
times_sin_zero = times_cos_zero = 0
number = 0

# Take user input once (convert to float)
blocks = float(input("Enter value: "))

# Loop until either sin or cos hits zero 3 times
while times_sin_zero < 3 and times_cos_zero < 3:
    sin_value = math.sin(number) * blocks * 15
    cos_value = math.cos(number) * blocks * 15

    # Check if sin or cos is zero
    if abs(sin_value) < 1e-9:
        times_sin_zero += 1
    if abs(cos_value) < 1e-9:
        times_cos_zero += 1

    # Increment number for the next iteration
    number += 8

# Output why the loop stopped
if times_sin_zero == 3:
    print("Sin hit zero 3 times.")
elif times_cos_zero == 3:
    print("Cos hit zero 3 times.")