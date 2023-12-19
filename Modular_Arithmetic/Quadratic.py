import sys
"""
quadratic is a function that enables to determine if a number "square" is a quadratic residue by matching 
this number with its possible square root. If we find a square root for "square" mod p then "square is a 
quadratic residue of p
"""
def quadratic(square, p):
    for i in range(p):
        if (i * i) % p == square:
            return i
    return None
"""
We say that an integer x is a Quadratic Residue if there exists an a such that a² = x mod p
a being the sqare root
"""
def main():
    text = int(input("Enter a signed integer: "))
    modulo = int(input("Enter the modulo: "))
    quadri = quadratic(text, modulo)
    if quadri is not None:
        print(f"{text} is a quadratic residue mod {modulo}, with a = {quadri}.")
    else:
        print(f"{text} is not a quadratic residue mod {modulo}.")

if __name__ == '__main__':
    main()
