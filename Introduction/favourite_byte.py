def outcome_func(string,key):
    flag = b''  # flag stored as a byte string as we manipulate bytes data
    for a in string: #Decode each byte one by one
        flag += bytes([a^key])  # bytes objects take a list as argument
    return flag.decode()


data = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
data_decoded = bytes.fromhex(data)

for k in range(256): #As we are looking for a unique byte we will try all possibilities from the ASCII table
    outcome = outcome_func(data_decoded,k)
    if 'crypto' in outcome: #Looks for the beginning of the flag in the outputat the end of every function call
        print(outcome)
        break
        
    