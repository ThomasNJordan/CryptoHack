# Define the file path
file_path = "src/output_086036e35349a406b94bfac9a7af6cca.txt"

# Initialize variables
n = None
e = None
ct = None

# Read the values from the file
with open(file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        # Split the line into variable name and value
        parts = line.strip().split(' = ')
        if len(parts) == 2:
            variable_name = parts[0].strip()
            value = parts[1].strip()

            if variable_name == 'n':
                n = int(value)
            elif variable_name == 'e':
                e = int(value)
            elif variable_name == 'ct':
                ct = int(value)

# Check if values were successfully read
if n is not None and e is not None and ct is not None:
    print("n:", n)
    print("e:", e)
    print("ct:", ct)
else:
    print("Failed to read values from the file.")

# since only one prime number:
n_tot = n - 1

# Use EEuclid to fine coefficients
from src.gcd import extended_gcd
s, t, r = extended_gcd(e, n_tot)
print("Coefficients: ", s, t)

# in this case, s is d
d = s
# verify: print(e * d % n_tot) -> returns 1

# now decrypt ct
decoded_int = pow(ct, d, n)
print("Decoded int: ", decoded_int)

from Cryptodome.Util.number import long_to_bytes, inverse

print("Plaintext: ", long_to_bytes(decoded_int))
