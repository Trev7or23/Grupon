import random

def longitud():
	longitud = 0
	while longitud <8 or longitud >16:
		longitud = int(input("elija una longitud de 8 a 16 "))
	return longitud
def mayusculas():
	mayusculas = ""
	while True:
		mayusculas = input("quiere mayusculas? ").strip().lower()
		if mayusculas == "si" or mayusculas == "no":
			break
	return True if mayusculas == "si" else False

def numeros():
	numeros = ""
	while True:
		numeros = input("quiere numeros? ").strip().lower()
		if numeros == "si" or numeros == "no":
			break
	return True if numeros == "si" else False

def simbolos():
	simbolos = ""
	while True:
		simbolos = input("quiere simbolos? ").strip().lower()
		if simbolos == "si" or simbolos == "no":
			break
	return True if numeros == "si" else False

def caracteres(m, n, s):
	caracteres = "abcdefghijklmnopqrstuvwxyz"
	if m:
		caracteres +=("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	if n:
		caracteres +=("0123456789")
	if s:
		caracteres +=("!@#$%^&*()_+{}[]<>?/\\|-=")

	return caracteres

def password(c, l):
	password = ""
	for i in range(l):
		rd = random.randint(0,len(c))
		password += c[rd]
	return password

if __name__ == "__main__":
	longitud = longitud()
	mayusculas = mayusculas()
	numeros = numeros()
	simbolos = simbolos()
	caracteres = caracteres(mayusculas, numeros, simbolos)
	password = password(caracteres, longitud)
	print(f"la password seria \n\n>>> {password} <<<")