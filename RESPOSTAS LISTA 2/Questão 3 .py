def numbers():
	n = int(input('Insira um valor para n: '))
	i = int(input('Insira um valor para i: '))
	j = int(input('Insira um alor para j: '))
	
	for k in range(0, n+i):
		if(k%i==0):
			print(k)
		elif(k%j==0):
			print(k)
numbers()