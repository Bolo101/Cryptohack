"""
Same resolution as favourite_byte.py
We use the pwn library to avoid using direct bytes object use. Xoring is much more easier to implement this way
"""
from pwn import xor
input ="73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
decoded = bytes.fromhex(input)
for i in range(256):
    solution = xor(decoded,i)
    if 'crypto'.encode() in solution:
        print(solution)
