#imports
import os
import sys
from Crypto.Cipher import AES

#function for printing menu items
def printMenu():
    print("********************************************************")
    print("------------- ENCRYPTION/DECRYPTION TOOL ---------------")
    print("1: AES")
    print("2: Bruh idk")
    print("3: lol no idea")
    usrInput = input("Please select an encryption method from the list above: ")
    print("********************************************************")

#function for starting and running program
def startMenu():
    userInput = ""
    while(userInput != "quit"):
        printMenu()
        userInput = input()

startMenu()