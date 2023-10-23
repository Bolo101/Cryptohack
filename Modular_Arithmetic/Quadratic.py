"""
Basic brute forcing quadratic residues implement
x is called a quadratric residues if it solves a**2 = x [p]
"""
import sys
from math import sqrt
def quadratic(square,p):
    for i in range(p):
        if (square - i) % p == False:
            quadri = i
            break
    a1 = sqrt(quadri)
    a2 = - sqrt(quadri)
    

def main():
    text = int(input("Enter a signed integer:"))
    modulo = int(input("Enter the modulo:"))
    result = quadratic(text,modulo)
    if result:
        print("Done")
        print(result)
    else:
        print("No result")
        sys.exit()

if __name__ =='__main__':
    main()