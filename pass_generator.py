import random
print("Welcome to passgenerator chafaWoW 2030")
password_list = []
letras = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r',
's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ',
'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = [ '!', '@', '#', '$', '%', '&', '/', '(', ')', '*', '+', '-', 'Ç', 'ª', 'º', '|'  ]

user_letras = int(input("How many words ?  "))
user_num = int(input(" How many numbers ?  "))
user_simbol = int(input(" How many special symbols ?  "))

for x in range(1, user_letras +1):
    password_list.append(random.choice(letras))

    ''' Esta es la forma simplificada de hacer la misma funcion anterior ahora con los números y simbolos '''
for x in range(1, user_num +1):
    password_list.append(random.choice(numeros))

for x in range(1, user_simbol +1):
    password_list.append(random.choice(simbolos))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for x in password_list:
    password += x
print(f"Your new password is: {password}")

