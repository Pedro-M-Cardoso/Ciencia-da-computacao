def palindromo(n):
	final = 0
	digits = []
	sec = n
	for i in range(len(str(n))):
		digits.append((n - n%(10**(len(str(n))-1)))//(10**(len(str(n))-1)))
		n = n - digits[-1]*(10**(len(str(n))-1))
	for num, i in enumerate(digits):
		final += i*(10**num)
	if final == sec:
		return True
	else:
		return False

print(palindromo(245))
