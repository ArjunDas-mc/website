inp = int(input("How many bits? (if unsigned) "))  # Convert input to an integer
if inp > 16:
    print("Too many bits entered as after 16, numbers get crazy.")
elif inp > 1:
    print(2 ** inp - 1, "is the max for", inp, "bits.")
else:
    print("Input must be greater than 1 to get a valid result.")
