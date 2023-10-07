"""
In the test we want to reveale the flag by guessing the key. As we know a part of the flag ("crypto{}"),
we can use this data in order to xor the hexadecimal decoded input with the flag format to get some information about the key.
By doing so we get the main part of the key and the missing part is quite obvious.
if the key is shorter than the message, the key will be used again until all the message is cyphered
"""
import operator
input = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
decoded = bytes.fromhex(input)
key = b'crypto{'
def test(entry):
    flag = b'' #flag in byte format
    key = b'crypto{' #key used to guess the real key used to encode the input

    for i in range(len(entry)):
        result = bytes([input ^car for(input,car) in zip(entry,key)])# First method to xor using bytes object
        flag += result

    return flag

end = test(decoded) # Main key with a part missing but you can easily guess it

def decoding(text):
    flag = b''
    key = b'myXORkey'
    for i in range(len(text)):
        result = operator.xor(text[i],key[i % len(key)]) #As the key is shorter than the message we make sure to use it % len(key) to avoid being out of range with the i incrementing
        flag += bytes([result])
    return flag

final = decoding(decoded)
print(final)

    