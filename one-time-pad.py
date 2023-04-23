from math import gcd

# Prompt user for p, q, and e values
p = int(input('Please select your p number:\n'))
q = int(input('Please select your q number:\n\033[91mNote: The value of e should be relatively prime to p!\033[0m \n'))
e = int(input('Lastly please select value for e:\n'))

# Check if e is relatively prime to p
if gcd(e, p) != 1:
    print("Error: e is not relatively prime to p.")
    exit()

# Calculate public and private keys
n = p * q
phiNumber = (p-1)*(q-1)
i = 0
d = (((phiNumber * i)+1) / e ) 
while not d.is_integer():
    i += 1 # Increment i by 1
    d = ((phiNumber * i) + 1) / e

# Print public and private keys
print("Your Public key is =", n, ",", n, "\n")
print("Your Private key is =", int(d), ",", n, "\n")