#imports
from asyncore import write
from importlib.metadata import files
from Crypto.Cipher import AES
import datetime

#ENCRYPTION------------------------
#function for AES encrypting
def AESencrypt():
    fileSize = 0
    inFilename = input("Enter the name of an existing file in this directory to encrypt: ")
    file = open(inFilename, "r")                                                                #open input file to get plaintext
    message = (file.read()).encode("UTF-8")                                                     #read plaintext message from file

    #password = input("Enter a 16-character password for encryption: ")
    AESencryptObj = AES.new("Sixteen Char Key".encode("utf8"), AES.MODE_CBC, "Sixteen Char IV ".encode("utf8"))     #AES object for encryption

    start = datetime.datetime.now()
    cipherText = AESencryptObj.encrypt(message)     #encrypt text
    end = datetime.datetime.now()
    timeElapsed = ((end-start).total_seconds())*1000
    #print("Cipher Text: ", cipherText)             # print for testing
    file.close()                                    #close input filee

    outFile = open((inFilename + "_AES.txt"), "wb") #create output file
    outFile.write(cipherText)                       #write ciphertext into output file

    outFile.close()                                 #close output file to finish

    fileSize = len(cipherText) * 8

    print("File Size: " + str(fileSize) + " bits")
    print("Time elapsed: " + str(timeElapsed) + " ms")


#DECRYPTION--------------------------
#function for AES decrypting
def AESdecrypt():
    fileSize = 0
    timeElapsed = 0
    AESdecryptionObj = AES.new("Sixteen Char Key".encode("utf8"), AES.MODE_CBC, "Sixteen Char IV ".encode("utf8")) #AES object for decryption

    inFilename = input("Enter a file name for ciphertext input: ")
    inputFile = open(inFilename, "rb")
    ciphertext = inputFile.read()

    start = datetime.datetime.now() #start timer
    plaintext = AESdecryptionObj.decrypt(ciphertext)
    end = datetime.datetime.now()   #end timer
    timeElapsed = ((end-start).total_seconds())*1000 #calculate elapsed time using start and end points then convert to ms
    inputFile.close()

    outputFile = open("AESdecyptOutput.txt", "wb")
    outputFile.write(plaintext)
    outputFile.close()

    #print(plaintext)        #plaintext print test

    fileSize = len(plaintext) * 8 #get file size in bits

    print("File Size: " + str(fileSize) + " bits")
    print("Time elapsed: " + str(timeElapsed) + " ms")


#MENU--------------------------------
#function for printing encrypt/decrypt menu
def printStartMenu():
    userInput = " "

    while(userInput != "quit"): #continues program until user enters quit
        print("***************************************************************")
        print("----------------- ENCRYPTION/DECRYPTION TOOL ------------------")
        userInput = input("Enter e/E for encryption or d/D for decryption or enter 'quit': ")
        print("***************************************************************")
        print()
        if userInput == "e" or userInput == "E":
            AESencrypt()
        elif userInput == "d" or userInput == "D":
            AESdecrypt()

#run
printStartMenu()