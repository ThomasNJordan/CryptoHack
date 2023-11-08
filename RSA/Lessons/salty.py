# define file path
file_path = "src/output_95f558e889cc66920c24a961f1fb8181.txt"

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

# e = 1, so since m^e %n = m^e*d % n, if we know e, no need to know d
from Cryptodome.Util.number import long_to_bytes
print("Flag: ", long_to_bytes(pow(ct, e, n)))
