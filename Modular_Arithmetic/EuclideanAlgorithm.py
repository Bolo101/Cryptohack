import sys
def Euclide():
    if len(sys.argv) != 3:
        print("Format is: python3 Euclide Algorithm number1 number2")
        sys.exit()
    try:
        a,b,r = int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[2])
        while r != 0:
            a,b,r = b,r,a%b
        return b
    except TypeError:
        print("Use valid integer inputs")
        sys.exit()
    

def main():
    result = Euclide()
    print(result)

if __name__ == "__main__":
    main()