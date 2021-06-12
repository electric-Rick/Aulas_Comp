import random
global estado, regiao, nome
state_id = str(input('Insira aqui o seu estado: '))
estado = state_id

def d_r(state_id):
	if state_id == 'DF':
		x = int(1)
		regiao = 'Centro-Oeste'
		estado = 'Distrito Federal'
		return regiao
	elif state_id == 'GO':
		x = int(1)
		regiao = 'Centro-Oeste'
		estado = 'Goiás'
		return regiao
	elif state_id == 'MS':
		x = int(1)
		regiao = 'Centro-Oeste'
		estado = 'Mato grosso do Sul'
		return regiao				
	elif state_id == 'MT':
		x = int(1)
		regiao = 'Centro-Oeste'
		estado = 'Mato Grosso'
		return regiao		
	elif state_id == 'TO':
		x = int(1)
		regiao = 'Centro-Oeste'
		estado = 'Tocantins'
		return regiao
	elif state_id == 'AC':
		x = int(2)
		regiao = 'Norte'
		estado = 'Acre'
		return regiao
	elif state_id == 'AM':
		x = int(2)
		regiao = 'Norte'
		estado = 'Amazonas'
		return regiao
	elif state_id == 'AP':
		x = int(2)
		regiao = 'Norte'
		estado = 'Amapá'
		return regiao
	elif state_id == 'PA':
		x = int(2)
		regiao = 'Norte'
		estado = 'Pará'
		return regiao
	elif state_id == 'RO':
		x = int(2)
		regiao = 'Norte'
		estado = 'Rondônia'
		return regiao
	elif state_id == 'RR':
		x = int(2)
		regiao = 'Norte'
		estado = 'Roraima'
		return regiao			
	elif state_id == 'CE':
		x = int(3)
		regiao = 'Nordeste'
		estado = 'Ceará'
		return regiao
	elif state_id == 'MA':
		x = int(3)
		regiao = 'Nordeste'
		estado = 'Maranhão'
		return regiao
	elif state_id == 'PI':
		x = int(3)
		regiao = 'Nordeste'
		estado = 'Piauí'
		return regiao
	elif state_id == 'AL':
		x = int(4)
		regiao = 'Nordeste'
		estado = 'Alagoas'
		return regiao
	elif state_id == 'PB':
		x = int(4)
		regiao = 'Nordeste'
		estado = 'Paraíba'
		return regiao
	elif state_id == 'PE':
		x = int(4)
		regiao = 'Nordeste'
		estado = 'Pernambuco'
		return regiao
	elif state_id == 'RN':
		x = int(4)
		regiao = 'Nordeste'
		estado = 'Rio Grande do Norte'
		return regiao
	elif state_id == 'BA':
		x = int(5)
		regiao = 'Nordeste'
		estado = 'Bahia'
		return regiao
	elif state_id == 'SE':
		x = int(5)
		regiao = 'Nordeste'
		estado = 'Sergipe'
		return regiao
	elif  state_id =='MG':
		x = int(6)
		regiao = 'Sudeste'
		estado = 'Minas Gerais'
		return regiao
	elif state_id == 'ES':
		x = int(7)
		regiao = 'Sudeste'
		estado = 'Espírito Santo'
		return regiao
	elif state_id == 'RJ':
		x = int(7)
		regiao = 'Sudeste'
		estado = 'Rio de Janeiro'
		return regiao
	elif state_id == 'SP':			 
		x = int(8)
		regiao = 'Sudeste'
		estado = 'São Paulo'
		return regiao
	elif state_id == 'PR':
		x = int(9)
		regiao = 'Sul'
		estado = 'Paraná'
		return regiao
	elif state_id == 'SC':
		x = int(9)
		regiao = 'Sul'
		estado = 'Santa Catarina'
		return regiao
	elif  state_id == 'RS':			 
		x = int(0)
		regiao = 'Sul'
		estado = 'Rio Grande do Sul'
		return regiao	

def d_e(state_id):
	if state_id == 'DF':
		x = int(1)
		regiao = 'Centro-Oeste'
		estado = 'Distrito Federal'
		return estado
	elif state_id == 'GO':
		x = int(1)
		regiao = 'Centro-Oeste'
		estado = 'Goiás'
		return estado
	elif state_id == 'MS':
		x = int(1)
		regiao = 'Centro-Oeste'
		estado = 'Mato grosso do Sul'
		return estado				
	elif state_id == 'MT':
		x = int(1)
		regiao = 'Centro-Oeste'
		estado = 'Mato Grosso'
		return estado		
	elif state_id == 'TO':
		x = int(1)
		regiao = 'Centro-Oeste'
		estado = 'Tocantins'
		return estado
	elif state_id == 'AC':
		x = int(2)
		regiao = 'Norte'
		estado = 'Acre'
		return estado
	elif state_id == 'AM':
		x = int(2)
		regiao = 'Norte'
		estado = 'Amazonas'
		return estado
	elif state_id == 'AP':
		x = int(2)
		regiao = 'Norte'
		estado = 'Amapá'
		return estado
	elif state_id == 'PA':
		x = int(2)
		regiao = 'Norte'
		estado = 'Pará'
		return estado
	elif state_id == 'RO':
		x = int(2)
		regiao = 'Norte'
		estado = 'Rondônia'
		return estado
	elif state_id == 'RR':
		x = int(2)
		regiao = 'Norte'
		estado = 'Roraima'
		return estado			
	elif state_id == 'CE':
		x = int(3)
		regiao = 'Nordeste'
		estado = 'Ceará'
		return estado
	elif state_id == 'MA':
		x = int(3)
		regiao = 'Nordeste'
		estado = 'Maranhão'
		return estado
	elif state_id == 'PI':
		x = int(3)
		regiao = 'Nordeste'
		estado = 'Piauí'
		return estado
	elif state_id == 'AL':
		x = int(4)
		regiao = 'Nordeste'
		estado = 'Alagoas'
		return estado
	elif state_id == 'PB':
		x = int(4)
		regiao = 'Nordeste'
		estado = 'Paraíba'
		return estado
	elif state_id == 'PE':
		x = int(4)
		regiao = 'Nordeste'
		estado = 'Pernambuco'
		return estado
	elif state_id == 'RN':
		x = int(4)
		regiao = 'Nordeste'
		estado = 'Rio Grande do Norte'
		return estado
	elif state_id == 'BA':
		x = int(5)
		regiao = 'Nordeste'
		estado = 'Bahia'
		return estado
	elif state_id == 'SE':
		x = int(5)
		regiao = 'Nordeste'
		estado = 'Sergipe'
		return estado
	elif  state_id =='MG':
		x = int(6)
		regiao = 'Sudeste'
		estado = 'Minas Gerais'
		return estado
	elif state_id == 'ES':
		x = int(7)
		regiao = 'Sudeste'
		estado = 'Espírito Santo'
		return estado
	elif state_id == 'RJ':
		x = int(7)
		regiao = 'Sudeste'
		estado = 'Rio de Janeiro'
		return estado
	elif state_id == 'SP':			 
		x = int(8)
		regiao = 'Sudeste'
		estado = 'São Paulo'
		return estado
	elif state_id == 'PR':
		x = int(9)
		regiao = 'Sul'
		estado = 'Paraná'
		return estado
	elif state_id == 'SC':
		x = int(9)
		regiao = 'Sul'
		estado = 'Santa Catarina'
		return estado
	elif  state_id == 'RS':			 
		x = int(0)
		regiao = 'Sul'
		estado = 'Rio Grande do Sul'
		return estado

def  n_r(x, state_id):
	if state_id == 'DF':
		x = int(1)
		regiao = 'Centro-Oeste'
		estado = 'Distrito Federal'
		return x
	elif state_id == 'GO':
		x = int(1)
		regiao = 'Centro-Oeste'
		estado = 'Goiás'
		return x
	elif state_id == 'MS':
		x = int(1)
		regiao = 'Centro-Oeste'
		estado = 'Mato grosso do Sul'
		return x				
	elif state_id == 'MT':
		x = int(1)
		regiao = 'Centro-Oeste'
		estado = 'Mato Grosso'
		return x		
	elif state_id == 'TO':
		x = int(1)
		regiao = 'Centro-Oeste'
		estado = 'Tocantins'
		return x
	elif state_id == 'AC':
		x = int(2)
		regiao = 'Norte'
		estado = 'Acre'
		return x
	elif state_id == 'AM':
		x = int(2)
		regiao = 'Norte'
		estado = 'Amazonas'
		return x
	elif state_id == 'AP':
		x = int(2)
		regiao = 'Norte'
		estado = 'Amapá'
		return x
	elif state_id == 'PA':
		x = int(2)
		regiao = 'Norte'
		estado = 'Pará'
		return x
	elif state_id == 'RO':
		x = int(2)
		regiao = 'Norte'
		estado = 'Rondônia'
		return x
	elif state_id == 'RR':
		x = int(2)
		regiao = 'Norte'
		estado = 'Roraima'
		return x			
	elif state_id == 'CE':
		x = int(3)
		regiao = 'Nordeste'
		estado = 'Ceará'
		return x
	elif state_id == 'MA':
		x = int(3)
		regiao = 'Nordeste'
		estado = 'Maranhão'
		return x
	elif state_id == 'PI':
		x = int(3)
		regiao = 'Nordeste'
		estado = 'Piauí'
		return x
	elif state_id == 'AL':
		x = int(4)
		regiao = 'Nordeste'
		estado = 'Alagoas'
		return x
	elif state_id == 'PB':
		x = int(4)
		regiao = 'Nordeste'
		estado = 'Paraíba'
		return x
	elif state_id == 'PE':
		x = int(4)
		regiao = 'Nordeste'
		estado = 'Pernambuco'
		return x
	elif state_id == 'RN':
		x = int(4)
		regiao = 'Nordeste'
		estado = 'Rio Grande do Norte'
		return x
	elif state_id == 'BA':
		x = int(5)
		regiao = 'Nordeste'
		estado = 'Bahia'
		return x
	elif state_id == 'SE':
		x = int(5)
		regiao = 'Nordeste'
		estado = 'Sergipe'
		return x
	elif  state_id =='MG':
		x = int(6)
		regiao = 'Sudeste'
		estado = 'Minas Gerais'
		return x
	elif state_id == 'ES':
		x = int(7)
		regiao = 'Sudeste'
		estado = 'Espírito Santo'
		return x
	elif state_id == 'RJ':
		x = int(7)
		regiao = 'Sudeste'
		estado = 'Rio de Janeiro'
		return x
	elif state_id == 'SP':			 
		x = int(8)
		regiao = 'Sudeste'
		estado = 'São Paulo'
		return x
	elif state_id == 'PR':
		x = int(9)
		regiao = 'Sul'
		estado = 'Paraná'
		return x
	elif state_id == 'SC':
		x = int(9)
		regiao = 'Sul'
		estado = 'Santa Catarina'
		return x
	elif  state_id == 'RS':			 
		x = int(0)
		regiao = 'Sul'
		estado = 'Rio Grande do Sul'
		return x
reg_ = 0

nome = str(input('Insira seu nome: '))			
d1 = int(random.randint(0,9))
d2 = int(random.randint(0,9))
d3 = int(random.randint(0,9))
d4 = int(random.randint(0,9))
d5 = int(random.randint(0,9))
d6 = int(random.randint(0,9))
d7 = int(random.randint(0,9))
d8 = int(random.randint(0,9))
d9 = n_r(reg_, state_id)
print(d9)
d10 = 0

L = 10*d1+9*d2+8*d3+7*d4+6*d5+5*d6+4*d7+3*d8+2*d9
_r = 11 - (L%11)
if _r == 0 or _r == 1:
	d10 = 0
else:
	d10 = 11 - _r

M = 10*d2+9*d3+8*d4+7*d5+6*d6+5*d7+4*d8+3*d9+2*d10

r_ = 11 - (M%11)

if r_ == 0 or r_ == 1:	
	d11 = 0
else: 
	d11 = 11 - r_
regiao = d_r(state_id)
estado = d_e(state_id)
reg_doc = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11]
n_reg = ''.join(map(str, reg_doc))
print('-----------------------------------------------------------------------------------')
print('Nome: '+nome)
print('Estado: '+estado)
print('Região: '+regiao)
print('CPF: ', n_reg)

print('-----------------------------------------------------------------------------------')