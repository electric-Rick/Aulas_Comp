def grau_to_rad():
	grau = int(input('Insira o valor em grau: '))
	pi = 3.141592653
	result = grau*(pi/180)
	str_result = str(result)
	print(str_result[:5] + 'rad')


def rad_to_grau():
	rad = float(input('Insira o valor em radiano: '))
	pi = 3.141592653
	result = rad*(180/pi)
	str_result = str(result)
	print(str_result[:5] + 'graus')
	
quest = input('Digite "RAD" para converter graus para radianos, ou digite "GRAUS" para converter de radianos para graus:')
if quest in 'RAD':
	grau_to_rad()
elif quest in 'GRAUS':
	rad_to_grau()
else:
	print('Operação finalizada')