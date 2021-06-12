import numpy as np

def val_sen():
	value = int(input('Insira o valor em radianos: '))
	result = np.sin(value)
	str_result = str(result)
	print('O valor de seno é: ', str_result[:5])

val_sen()