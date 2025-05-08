def encrypt(msg, key):
    mssg = mssg.replace(" ", "")
    cols = ['' for i in range(key)]

    for i in range(len(msg)):
        col = i%key
        cols[col] += mssg[i]
    
    return ''.join(cols)

def decrypt(cipher, key):
    n = len(cipher)
    col_len = n // key
    extra = n % key

    cols = []
    start = 0
    for i in range(key):
        length = col_len + (1 if i<extra else 0)
        cols.append(cipher[start:start+length])
        start += length
        print(cols)

    rows = ['' for i in range(len(cols[0]))]
    for i in range(len(cols[0])):
        for col in cols:
            if i < len(col):
                rows[i] += col[i]
                print(rows)
    return ''.join(cols)

decrypt('helloworld', key=4)