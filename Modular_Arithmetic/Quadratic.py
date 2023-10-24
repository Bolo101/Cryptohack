"""
Basic quadratic residue implement
x is called a quadratric residues if it solves a**2 = x [p]
"""
import sys
from math import sqrt
def quadratic(square,p):
    for i in range(p):
        if (square - i ) % p == 0:
            quadri = i
            print(f"Quadratic residue = {quadri}")
            break
    a1 = sqrt(square) 
    #a2 = sqrt(square) * (-1)
    #print(f"{a1} ; {a2}")
    if a1 == int(a1):
        return[int(a1),quadri]
    else:
        print("Floating solution")
        return [False,False]
        
    

def main():
    text = int(input("Enter a signed integer:"))
    modulo = int(input("Enter the modulo:"))
    root,quadri = quadratic(text,modulo)
    if root:
        print(f"{root} is the square root of {quadri} mod[{modulo}]")
    else:
        print("No result")
        sys.exit()

if __name__ =='__main__':
    main()