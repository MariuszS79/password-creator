import random

letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
digits=["0","1","2","3","4","5","6","7","8","9"]
symbols=["£","$","%","^","&","*","(",")","|","<",">","@","?"]

letqty=int(input("How many letters?: "))
digqty=int(input("How many digits?: "))
symqty=int(input("How many symbols?: "))

password1=[]

for i in range(letqty):
  password1.append(random.choice(letters))
for i in range(digqty):
  password1.append(random.choice(digits))
for i in range(symqty):
  password1.append(random.choice(symbols))
random.shuffle(password1)

print("Your password is: ", "".join(password1))
