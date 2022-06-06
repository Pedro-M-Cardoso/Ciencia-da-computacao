import math

def primo(n):
	for i in range(2, math.ceil(n**(1/2))):
		if n%i == 0:
			return False
	return True

def primo_proximo(n):
	count = 0
	while True:
		if primo(n + count):
			return n + count
			break
		else:
			count += 1

def fatores(n):
	lista = []
	while n != 1:
		for i in range(2,n):
			if n%i==0:
				n = n//i
				if primo(i) and i not in lista:
					lista.append(i)
	return lista

# print(primo(341))
# print(primo_proximo(100))
# print(fatores(341))
