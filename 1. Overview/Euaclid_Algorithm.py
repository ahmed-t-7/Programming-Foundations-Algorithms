# This is Example to Find the greatest common denominator (GCD) of two integers

def gcd(a, b):           
    r = a % b                 # r is the remainder  
    while r != 0: 
        a = b
        b = r
        r = a % b

    print("The GCD = ", b)    # in case of remainder = 0 the GCD = b  

gcd(20, 8)
gcd(16, 8)

