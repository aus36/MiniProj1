#imports
import os
import sys
from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Cipher import Salsa20
from Crypto.Random import get_random_bytes

#ENCRYPTION------------------------
#function for AES encrypting
def AESencrypt():
    print("e")

#function for DES encrypting
def DESencrypt():
    print("e")

#function for Salsa20 encrypting
def SALSAencrypt():
    print("e")

#DECRYPTION--------------------------
#function for AES decrypting
def AESencrypt():
    print("e")

#function for DES decrypting
def DESencrypt():
    print("e")

#function for Salsa20 decrypting
def SALSAencrypt():
    print("e")
#------------------------------------

#function for printing encrypt/decrypt menu
def printStartMenu():
    print("*************************************************************")
    print("---------------- ENCRYPTION/DECRYPTION TOOL -----------------")
    userInput = input("Enter E for encryption or D for decryption or enter 'quit': ")
    print("*************************************************************")
    if(userInput == "quit"):
        return
    else:
        printSecondMenu()

#function for printing encryption/decryption scheme choice
def printSecondMenu():
    print("********************************************************")
    print("1: AES")
    print("2: DES")
    print("3: Salsa20")
    userInput = input("Please select an encryption method from the list above: ")
    print("********************************************************")
    if(userInput == 1):
        AESencrypt()
    else:
        print("E")

#runner function
def main():
    printStartMenu()

main()