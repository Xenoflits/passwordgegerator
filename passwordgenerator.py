import random
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "\\", "|", ";", ":", "'", '"', ",", "<", ".", ">", "/", "?"]

number = int(input("how many numbers"))
letter = int(input("how many letters"))
symbol = int(input("how many symbols"))

password = ""
total = number + letter + symbol

for cycle in range(1,total+1):
    print(cycle+" debug")
    

def addnumber():
    return random.randint(0,number)

def addsymbol():
    return random.randint(0,symbol)

def addletter():
    return random.randint(0,letter)
