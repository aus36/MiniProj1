#imports
from asyncore import write
import os
import sys
from Crypto.Cipher import AES

#ENCRYPTION------------------------
#function for AES encrypting
def AESencrypt():
    inFilename = input("Enter the name of an existing file in this directory to encrypt: ")
    file = open(inFilename, "r") #open input file to get plaintext
    message = (file.read()).encode("UTF-8") #read plaintext message from file

    #password = input("Enter a 16-character password for encryption: ")
    AESencryptObj = AES.new("Sixteen Char Key".encode("utf8"), AES.MODE_CBC, "Sixteen Char IV ".encode("utf8")) #create new AES object

    cipherText = AESencryptObj.encrypt(message) #encrypt text
    print("Cipher Text: ", cipherText) # print for testing
    file.close() #close input filee

    outFile = open("inputFile_AES.txt", "wb") #create output file
    outFile.write(cipherText) #write ciphertext into output file

    outFile.close() #close output file to finish

#DECRYPTION--------------------------
#function for AES decrypting
def AESdecrypt():
    AESdecryptionObj = AES.new("Sixteen Char Key".encode("utf8"), AES.MODE_CBC, "Sixteen Char IV ".encode("utf8")) #object for decryption


#MENU--------------------------------
#function for printing encrypt/decrypt menu
def printStartMenu():
    encrypted = False #Variables for ending loop
    decrypted = False #^^^

    print("***************************************************************")
    print("----------------- ENCRYPTION/DECRYPTION TOOL ------------------")
    userInput = input("Enter e/E for encryption or d/D for decryption or enter 'quit': ")
    print("***************************************************************")
    while(userInput != "quit" or (encrypted != True and decrypted != True)): #continues program until user enters quit or has encrypted and decrypted at least once
        return
    if userInput == "e" or userInput == "E":
        AESencrypt()
        encrypted = True
    elif userInput == "d" or userInput == "D":
        AESdecrypt()
        decrypted = True
    else:
        print("Invalid Input. Restarting...") #catches exception cases and restarts loop

#run
printStartMenu()