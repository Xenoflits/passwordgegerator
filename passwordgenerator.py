import random
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "\\", "|", ";", ":", "'", '"', ",", "<", ".", ">", "/", "?"]

number = int(input("how many numbers"))
letter = int(input("how many letters"))
symbol = int(input("how many symbols"))

password = []

for _ in range(number):
    x = random.choice(numbers)
    password.append(x)

for _ in range(letter):
    x = random.choice(letters)
    password.append(x)
for _ in range(symbol):
   x = random.choice(symbols)
   password.append(x)

random.shuffle(password)
password = "".join(password)
print(password)