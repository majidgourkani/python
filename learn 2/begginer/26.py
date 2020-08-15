#encrypt and decrypt program
alfa = "abcdefghijklmnopqrstuvwxyz"
def encrypt(s , shift = 2):
    enc_str = ""
    for ch in s:
        x = alfa.index(ch)
        enc_str += alfa[(x + shift)%26]
    return enc_str

def decrypt(s , shift = 2):
    dec_str = ""
    for ch in s:
        x = alfa.index(ch)
        dec_str += alfa[(x - shift)%26]
    return dec_str

print(encrypt("abcmnoxyz" , 3))
print(decrypt("defpqrabc" , 3))
print(decrypt(encrypt("majidddd")))
