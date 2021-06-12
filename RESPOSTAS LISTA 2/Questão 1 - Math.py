import math

def fc_sin():
	n = int(input('Digite o valor em radianos: '))
	z= math.sin(n)
	str_z = str(z)
	print('O valor de de seno é de: ', str_z[0:5])
	
fc_sin()