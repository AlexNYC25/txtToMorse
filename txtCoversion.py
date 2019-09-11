import sys
from MorseAlphabet import *

inFile = sys.argv[1]

o = open("output.txt", "w")
pyMorseLib = MorseAlphabet()

with open(inFile, 'r') as i:
    for line in i:
        for word in line.split():
            for letter in word:
                o.write(pyMorseLib.letterToMorse(letter) + " ")
            o.write(" ")
        o.write("\n") 