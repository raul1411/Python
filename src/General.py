# EXERCICI 1
num1 = int(input("Introdueix el primer numero: "))
num2 = int(input("Introdueix el segon numero: "))
print((num1 + num2) / 2)

# EXERCICI 2
peus = int(input("Introdueix una distància en peus: "))
polsades = float(input("Introdueix una distància en polsades: "))

print("Distancia en peus passada a centímetres: ", (peus * 12) * 2.54)
print("Distancia en polsades passada a centímetres: ", polsades * 2.54)

# EXERCICI 3
celsius = float(input("Introdueix temperatura en graus Celsius: "))
print("Temperatura en graus Fahrenheit: ", (celsius * 1.8) + 32)

# EXERCICI 4
segons = int(input("Introdueix una quantitat de segons: "))

print("Són ", int(segons/60), " minuts i ", round(((segons/60) - int(segons/60)) / 0.016666667), " segons")

# EXERCICI 5
llis=['A', 'E', 'I', 'O', 'U']
numero = int(input("Introdueix quin numero d'element de la llista vols modificar: "))
valor = input("Introdueix quin valor vols posar: ")

llis[numero] = valor

print(llis)

# EXERCICI 6
taula7 = [x * 7 for x in range(11)]
print (taula7)

# EXERCICI 7
diccionari = {"Raul": "5", "Bryan": "7", "Oihane": "10", "Montse": "9"}

print(diccionari)
alumne = input("De quin usuari vols saber la nota?")
print("Nota de ",alumne,": ",diccionari[alumne])

# EXERCICI 8
llista1 = ["Peter Parker", "Wanda Maximoff", "Tony Stark", "Pietro Maximoff"]
llista2 = ["Charles Xavier", "Jean Grey", "Wanda Maximoff", "Pietro Maximoff"]

print("Interseccions:")
print(set(llista1).intersection(llista2))

print("Diferències:")
print(set(llista1).difference(llista2))

print("Paraules que apareixen en la segona llista però no en la primera:")
print(set(llista1) - set(llista2))

print("Diferències:")
print(set(llista1).union(llista2))

# EXERCICI 9
num1 = int(input("Introdueix el primer número enter"))
num2 = int(input("Introdueix el segon número enter"))

if num2 == 0:
    print("No es pot dividir entre 0")
else:
    division = num1%num2

    if division == 0:
        print("La divisió entre els dos números és exacta")
    else:
        print("La divisió entre els dos números no és exacta")

# EXERCICI 10
import math

eleccio = int(input("Que àrea vols calcular?\n1. Triangle\n2. Cercle"))

if (eleccio == 1):
    base = float(input("Introdueix la base:"))
    altura = float(input("Introdueix l'altura:"))
    resultat = (base * altura)/2
    print("L'àrea del triangle és: ", resultat)
elif (eleccio == 2):
    radi = float(input("Introdueix el radi:"))
    resultat = math.pi * pow(radi, 2)
    print("L'àrea del cercle és: ", resultat)
else:
    print("No has escollit cap opció")

# EXERCICI 13
enter1 = int(input("Introdueix un número enter:"))
enter2 = int(input("Introdueix altre número enter més gran que el primer:"))

result = 0
if enter1 < enter2:
    for x in range(enter1+1, enter2):
        result = result + x
    print("La suma de els números entre", enter1, "i", enter2, "=", result)
else:
    print("El segon número ha de ser més gran que el primer")

# EXERCICI 14
numero = int(input("Introdueix un número enter major que 0:"))

result = 1

if numero <= 0:
    print("El número ha de ser superior a 0")

else:
    for x in range(2, numero+1):
        result = result * x
    print(result)

# EXERCICI 15
for x in range(0,100):
    division = x%7
    if (division==0):
        print(x)

# EXERCICI 16
num = int(input("Introdueix un numero"))

list = []

for x in range(0,num):
    paraula = input("Introdueix una paraula:")
    list.append(paraula)
print(list)

# EXERCICI 17
llista1 = ["Peter Parker", "Wanda Maximoff", "Tony Stark", "Pietro Maximoff"]
llista2 = ["Charles Xavier", "Jean Grey", "Wanda Maximoff", "Pietro Maximoff"]

for x in llista2:
    if x in llista1:
        llista1.remove(x)
print (llista1)

# EXERCICI 24
for x in range(1,11):
    print(x * 2)

# EXERCICI 25
n = int(input("Introdueix quants múltiples vols veure"))
m = int(input("Introdueix de quin número vols els múltiples"))

for x in range(1, n+1):
    print(x * m)

# EXERCICI 26
paraula = input("Introdueix una paraula:")

if list(paraula) == sorted(paraula):
    print("La paraula és alfabètica")
else:
    print("La paraula no és alfabètica")

# EXERCICI 27
paraula = input("Introdueix una paraula:")

if str(paraula) == str(paraula)[::-1]:
    print("La paraula és palíndroma")
else:
    print("La paraula no és palíndroma")

# EXERCICI 29
file = open("29", "r")

line = file.read().lower().split()
line = list(dict.fromkeys(line))
line.sort()
print(line)