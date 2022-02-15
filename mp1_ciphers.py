#imports
import os
import sys
from Crypto.Cipher import AES

#function for printing menu items
def printMenu():
    print("********************************************************")
    print("------------- ENCRYPTION/DECRYPTION TOOL ---------------")
    userChoice = input("Enter E for encryption or D for decryption: ")
    print("1: AES")
    print("2: DES")
    print("3: Trivium")
    userInput = input("Please select an encryption method from the list above: ")
    print("********************************************************")
    if(userChoice == "quit"):
        return 0
    return 1

#ENCRYPTION------------------------
#function for AES encrypting
def AESencrypt():
    print("e")

#function for DES encrypting
def DESencrypt():
    print("e")

#function for Trivium encrypting
def TRIVencrypt():
    print("e")

#DECRYPTION--------------------------
#function for AES decrypting
def AESencrypt():
    print("e")

#function for DES decrypting
def DESencrypt():
    print("e")

#function for Trivium decrypting
def TRIVencrypt():
    print("e")
#------------------------------------

#function for starting and running program
def startMenu():
    output = 1
    while(output != 0):
        output = printMenu()

startMenu()