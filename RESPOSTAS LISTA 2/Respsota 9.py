tipos = {'escaleno':'ESCALENO', 'isósceles':'ISÓSCELES', 'equilatero':'EQUILATERO'}
while True:
	try:
		print('-%-'*4*4)
		print('Identifique seu triãngulo, vamos começar:')
		tri_ = [int(input('Insira o primeiro lado: ')),int(input('Insira o segundo lado: ')),int(input('Insira o terceiro lado: '))]
		for i in range(0, len(tri_)):
			tri_[i]
		pass
		if tri_[0] > (tri_[1] + tri_[2]) or tri_[1] > (tri_[0]+tri_[2]) or tri_[2] > (tri_[0]+tri_[1]):
			print('Estes carinhas aí não podem ser um triângulo.')
		elif tri_[0] == tri_[1] == tri_[2]:
			print('Bacana, temos um triãngulo', tipos['equilatero'])
		elif tri_[0] == tri_[1] or tri_[0] == tri_[2] or tri_[1] == tri_[2]:
			print('Bacana, temos um triãngulo', tipos['isósceles'])
		else:
			print('Maravilha, este é um triãngulo', tipos['escaleno'])
	except Exception as e:
		raise e
	else:
		pass
	pass