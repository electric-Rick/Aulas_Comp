global aux
def all_numbers():
	aux = []
	for i in range(1000, 10000): # Todos os números com 4 algarismos
		k = str(i)
		if (int(k[:2]) + int(k[2:]))**2==i:
			aux.append(i)
	print(*aux, ' são todos estes números apresentam tal característica.')
all_numbers()