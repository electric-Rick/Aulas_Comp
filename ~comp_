lista_alunos = []

class provas:
	def __main__(self, prov_1, prov_2, prov_3, media):
		self.prov_1 = prov_1
		self.prov_2 = prov_2
		self.prov_3 = prov_3
		self.media = media			
		
	def prov_1():
		res = int(input('Insira o valor da primeira prova: '))
		store = res
		return res
	def prov_2():
		res = int(input('Insira o valor da segunda prova: '))
		store = res
		return res
	def prov_3():
		res = int(input('Insira o valor da terceira prova: '))
		store = res
		return res
		
class aluno:
	def __main__(self, nome, matricula, curso):
		self.nome = nome
		self.matricula = matricula
		self.curso = curso
	def nome():
		_nome = input('Digite seu nome: ')
		store_name = _nome
		return store_name
	def matricula():
		_matricula = input('Digite sua matricula: ')
		store_matricula = _matricula
		return store_matricula
	def curso():
		_curso = input('Digite seu curso: ')
		store_curso = _curso
		return store_curso


def calc__media(lista):
	
	question = input('Quer começar:[y/n]')
	def proceed():
		reprovados = []
		aprovados = []	
		f = open('listagem_alunos_aprovados.txt','w')
		fr = open('listagem_alunos_reprovados.txt', 'w')
		nome = aluno.nome()
		matr = aluno.matricula()
		curso = aluno.curso()
		nota_1 = provas.prov_1()
		nota_2 = provas.prov_2()
		nota_3 = provas.prov_3()
		media = int(((nota_1 + nota_2 + nota_3)/3))
		print('Sua media foi de : ', media)	
		if media < 5:
			lista.append([{'Nome':nome, 'Matrícula':matr,'Curso':curso, 'Situação':'Reprovado por nota', 'Media':media}])
			reprovados.append([{'Nome':nome, 'Matrícula':matr,'Curso':curso, 'Situação':'Reprovado por nota', 'Media':media}])
			fr.write(str(aprovados))
			print('Consulte o seu professor.')			
		elif media >= 5 or media == 5:
			lista.append([{'Nome':nome, 'Matrícula':matr,'Curso':curso, 'Situação':'Aprovado por nota', 'Media':media}])
			aprovados.append([{'Nome':nome, 'Matrícula':matr,'Curso':curso, 'Situação':'Aprovado por nota', 'Media':media}])
			f.write(str(reprovados))
			quest_ = input('Deseja continuar?')
			if(quest_ == 'S' or quest_ == 's' or quest_ == 'Sim' or quest_ == 'Yes' or quest_ == 'y'):
				proceed()
			elif quest_ == '' or quest_ == 'N' or quest_ == 'Não' or quest_ == 'nao' or quest_ == 'não' or quest_ == 'Nao':	
				print('Fim da operação')
				pass
	if(question == 's' or question == 'S' or question == 'Sim' or question == 'Y' or question == 'y' or question == 'Yes'):
		proceed()
	else:		
		print('Usuário interrompeu a ação, nada foi feito.')
	

	




