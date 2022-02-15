# All strings need to be encoded to multiples of 16 byte arrays.
# This example has sixteen characters encoded to a byte array.
# Each character is of 1 byte (8 bits) long

# import AES from the crypto module 
from Crypto.Cipher import AES


# encryption object
enc_obj = AES.new("Sixteen Char Key".encode("utf8"), AES.MODE_CBC, "Sixteen Char IV ".encode("utf8"))

# message 'aka' plain text
m = "Sixteen Char PT ".encode("UTF-8")

# cipher text represented by 'y'
y = enc_obj.encrypt(m)
print("Cipher Text: ", y)

# decryption object - cannot reuse enc_object
dec_obj = AES.new("Sixteen Char Key".encode("utf8"), AES.MODE_CBC, "Sixteen Char IV ".encode("utf8"))


# plain text represented by 'x'
x = dec_obj.decrypt(y)
print("Plain Text: ", x)