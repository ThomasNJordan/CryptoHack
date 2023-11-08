# define file path
file_path = "src/output_5a478a5d4764257d0bbdfaed340fcbdd.txt"

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


factors = [9282105380008121879,
 9303850685953812323,
 9389357739583927789,
 10336650220878499841,
 10638241655447339831,
 11282698189561966721,
 11328768673634243077,
 11403460639036243901,
 11473665579512371723,
 11492065299277279799,
 11530534813954192171,
 11665347949879312361,
 12132158321859677597,
 12834461276877415051,
 12955403765595949597,
 12973972336777979701,
 13099895578757581201,
 13572286589428162097,
 14100640260554622013,
 14178869592193599187,
 14278240802299816541,
 14523070016044624039,
 14963354250199553339,
 15364597561881860737,
 15669758663523555763,
 15824122791679574573,
 15998365463074268941,
 16656402470578844539,
 16898740504023346457,
 17138336856793050757,
 17174065872156629921,
 17281246625998849649]

n_tot = 1
for factor in factors:
    n_tot = n_tot  * (factor - 1)
print("Totient: ", n_tot)

from src.gcd import extended_gcd
s, t, r = extended_gcd(e, n_tot)
print("Coefficients: ", s, t)

d = s

# now decrypt ct
decoded_int = pow(ct, d, n)
print("Decoded int: ", decoded_int)

from Cryptodome.Util.number import long_to_bytes

print("Plaintext: ", long_to_bytes(decoded_int))