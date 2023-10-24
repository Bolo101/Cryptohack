import sys

def quadratic(square, p):
    for i in range(p):
        if (i * i) % p == square:
            return i

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
