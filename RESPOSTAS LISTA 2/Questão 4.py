question = int(input('Digite um número e veja se ele é primo: '))
onde_estou = 0 

for i in range(1,question+1):
	if question%i == 0:
		k +=1
	else:
		pass
if k == 2:
		print('Este número é primo!')
else:
		print('Este número não é primo.')
