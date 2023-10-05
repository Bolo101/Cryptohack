import operator
input = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
decoded = bytes.fromhex(input)
key = b'crypto{'
def test(entry):
    flag = b''
    key = b'crypto{'

    for i in range(len(entry)):
        result = bytes([input ^car for(input,car) in zip(entry,key)])
        flag += result

    return flag

end = test(decoded)

def decoding(text):
    flag = b''
    key = b'myXORkey'
    for i in range(len(text)):
        result = operator.xor(text[i],key[i % len(key)])
        flag += bytes([result])
    return flag

final = decoding(decoded)
print(final)

    