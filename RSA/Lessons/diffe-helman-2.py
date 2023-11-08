# https://math.stackexchange.com/questions/598485/finding-a-primitive-element-of-a-finite-field

# in sage, factored p-1: [2, 25, 563]
"""
Test cases: 
2 * 25 = 50
2 * 563 = 1126
25 * 563 = 14075
"""

p = 28151
factors = [2, 25, 563]

def is_primitive_element(alpha, p):
    for factor in factors:
        power = (p - 1) // factor # floor after integer division
        if pow(alpha, power, p) == 1:
            return False
    return True

for alpha in range(2, p): # 1 always equals 1
    if is_primitive_element(alpha, p):
        print(f"The smallest primitive element for Fp = {p} is {alpha}")
        break
