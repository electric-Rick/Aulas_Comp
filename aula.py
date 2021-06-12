# Aula sobre estruturas de repetição
# Professor: Robson Marinho
# Aluno: Erick Augusto


def __script__():
	a = 0
	x = int(input('Escolha um número: '))
	while a <= x:
		a = a + 1
		if a % 2 == 0:
			print('Par')
		else:
			print('Impar')
		pass
	pass
__script__()


