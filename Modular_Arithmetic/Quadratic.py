"""
Basic brute forcing quadratic residues implement
x is called a quadratric residues if it solves a**2 = x [p]
"""
import sys
def quadratic(square):
    for i in range(square):
        if i*i == square:
            print(f"{i} is the square root of {square}")
            return True
    return False    

def main():
    text = int(input("Enter a signed integer:"))
    result = quadratic(text)
    if result:
        print("Done")
    else:
        print("Cow")
        sys.exit()

if __name__ =='__main__':
    main()