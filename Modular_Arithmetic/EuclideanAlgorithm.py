import sys
def Euclide():
    if len(sys.argv) != 3:
        print("Format is: python3 Euclide Algorithm number1 number2")
        sys.exit()
    try:
        a,b = int(sys.argv[1]),int(sys.argv[2])
        while b != 0:
            a,b = b,a%b
        return a
    except TypeError:
        print("Use valid integer inputs")
        sys.exit()
    

def main():
    result = Euclide()
    print(result)

if __name__ == "__main__":
    main()