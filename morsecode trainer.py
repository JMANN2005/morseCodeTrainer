import winsound
from time import sleep
import random
frequency = 700
speed = 100
##winsound.Beep(frequency, duration)
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
morsecode = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','/',]
def playsound(code):
    for i in range(0,len(code)):
        if (code[i] == '.'):
            winsound.Beep(frequency, speed)
        if (code[i] == '-'):
            winsound.Beep(frequency, speed * 3)


while(True):
    letter = random.randint(0,25)
    playsound(morsecode[letter])
    guess = input()
    if (guess == alphabet[letter]):
        print("correct")
    else:
        print("intcorrect it was " + alphabet[letter])
    sleep(0.5)

