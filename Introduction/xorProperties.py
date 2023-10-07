allitems = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
item1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
item12 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
item23 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"

f1 = [car for car in bytes.fromhex(item1)] #create a list containing all the bytes collection from the hexadecimal input representing Key1 
f23 = [car for car in bytes.fromhex(item23)] #create a list containing all the bytes collection from the hexadecimal input representing Key2 ^ Key3
ff123 = [car for car in bytes.fromhex(allitems)] #create a list containing all the bytes collection from the hexadecimal input representing Flag^Key1^Key2^Key3

flag_h1 = [allitem ^ k1c for (allitem,k1c) in zip(ff123,f23)] #We xor each bytes from the ff123 collection by the ones in the f1 collection to remove the Key1 (Key1^Key1 = 0)
flagg = [flag_h1 ^ f1 for (flag_h1,f1) in zip(flag_h1,f1)] # We xor each bytes from the ff123 collection by the ones in the f23 collection to remove the Key2^Key3

flagfinal = "".join(chr(o) for o in flagg) #Convert all bytes into an ASCII character
print(flagfinal)


