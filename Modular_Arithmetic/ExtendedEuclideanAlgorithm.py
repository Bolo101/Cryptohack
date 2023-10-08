import sys

def ExtendedEuclidean(a, b):
    x,y, u,v = 0,1, 1,0
    while b != 0:
        q, r = a//b, a%b
        m, n = x-u*q, y-v*q
        a,b, x,y, u,v = b,r, u,v, m,n
    gcd = a
    return gcd, x, y

def main():
    if len(sys.argv) !=3:
        print("Only provide two integers to get the gcd and a linear combination of Bezout's identity")
        sys.exit()
    try:
        number1, number2 = int(sys.argv[1]),int(sys.argv[2])
        gcdf,resultx,resulty = ExtendedEuclidean(number1,number2)
        print(f"x : {resultx} ; y : {resulty}")
        print(f"{number1} * {resultx} + {number2} * {resulty} = {gcdf}")
    except TypeError:
        sys.exit()

if __name__ == "__main__":
    main()