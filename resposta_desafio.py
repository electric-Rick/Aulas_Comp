# Autor: Erick Augusto de Almeida
# Propósito: Desafio 1 - Computação I
# Professor: Robson Marinho
# Instituto: Instituto de Ciências Exatas


import random
global DOC_PESSOA
DOC_PESSOA = []
class cpf:
	def __init__(self, digits):
		self.digits = digits
	def digits():
		d_1, d_2, d_3, d_4, d_5, d_6, d_7, d_8, d_9, d_10, d_11, distrito = random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),0,0,0, ''
		_all = [d_1, d_2, d_3, d_4, d_5, d_6, d_7, d_8, d_9, d_10, d_11, distrito]
		return _all

def estado(_list):
	state_id = str(input('Digite seu estado: '))		
	distrito = state_id
	_list[11] = distrito
	for i in _list:
		if  state_id =='DF' or state_id =='GO' or state_id =='MS' or state_id =='MT' or state_id =='TO':
			_list[8] += int(1)
			break
		elif  state_id =='AC' or state_id =='AM' or state_id =='AP' or state_id =='PA' or state_id =='RO' or state_id =='RR':
			_list[8] += int(2)
			break
		elif  state_id =='CE' or state_id =='MA' or state_id =='PI':
			_list[8] += int(3)
			break
		elif  state_id =='AL' or state_id == 'PB' or state_id =='PE' or state_id =='RN':
			_list[8] += int(4)
			break 
		elif  state_id =='BA' or state_id =='SE':
			_list[8] += int(5)
			break
		elif  state_id =='MG':
			_list[8] += int(6)
			break
		elif  state_id =='ES' or state_id =='RJ':
			_list[8] += int(7)
			break  
		elif state_id == 'SP':			 
			_list[8] += int(8)
			break
		elif  state_id  =='PR' or state_id =='SC':			 
			 _list[8] += int(9)
			 break
		elif  state_id == 'RS':			 
			_list[8] += int(0)
			break
		else:
			print('Operação não realizada, falha ao atribuir ESTADO feito.')
			break
def cpf_generator():
	nome = str(input('Digite seu nome: '))
	DOC_PESSOA = cpf.digits()
	regiao = str(input('Digite a sua região: '))
	separador = '.'
	estado(DOC_PESSOA)
	L = 10*DOC_PESSOA[0]+9*DOC_PESSOA[1]+8*DOC_PESSOA[2]+7*DOC_PESSOA[3]+6*DOC_PESSOA[4]+5*DOC_PESSOA[5]+4*DOC_PESSOA[6]+3*DOC_PESSOA[7]+2*DOC_PESSOA[8]
	M = 10*DOC_PESSOA[1]+9*DOC_PESSOA[2]+8*DOC_PESSOA[3]+7*DOC_PESSOA[4]+6*DOC_PESSOA[5]+5*DOC_PESSOA[6]+4*DOC_PESSOA[7]+3*DOC_PESSOA[8]+2*DOC_PESSOA[9]
	r = 11 - (L%11)
	r_ = 11 - (M%11)	
	if r == 0 or r == 1 and r_ == 0 or r_ == 1:
		DOC_PESSOA[9] = 0
		DOC_PESSOA[10] = 0
		pass
	else:
		DOC_PESSOA[10] = 11 - r_
		DOC_PESSOA[9] = 11 - r
		pass
	reg_doc = DOC_PESSOA
	reg_doc = ''.join(map(str, reg_doc))
	o_doc = reg_doc[:3]+ '.'+ reg_doc[3:6]+'.' + reg_doc[6:9] + '-' + reg_doc[9:11]
	print('*****************CPF GERADO COM SUCESSO*******************')
	print('------------------------------------------------------------------')
	print('Nome: ' , nome)
	print('Região: ', regiao)
	print('Estado: ',DOC_PESSOA[11])
	print('CPF: ' + o_doc)
	print('------------------------------------------------------------------')
	quest_ = str(input('Deseja salvar este arquivo? [S][N]'))
	if quest_ == 'S' or quest_ == 's':
		f = open(nome+'_CPF.csv', 'w')
		f.write(str('Nome:' + nome + '\n'))
		f.write(str('CPF: '))
		f.writelines(str(o_doc + '\n'))
		f.write(str('Região :' + regiao + '\n'))
		print("USUÁRIO CADASTRADO COM SUCESSO!")		
	else: 
		print('USUÁRIO NÃO CADASTRADO, FIM DA OPERAÇÃO')
		pass
cpf_generator()