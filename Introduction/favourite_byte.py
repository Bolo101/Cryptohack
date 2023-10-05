def outcome_func(string,key):
    flag = b''
    for a in string:
        flag += bytes([a^key])
    return flag.decode()


data = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
data_decoded = bytes.fromhex(data)

for k in range(256):
    outcome = outcome_func(data_decoded,k)
    if 'crypto' in outcome:
        print(outcome)
        break
        
    