
aluno = []
alunos = []
alunos_aprovados, alunos_reprovados = []
nome = str(input('Insira o nome do aluno: '))
nota_1 = int(input('Insira o valor da P1: '))
nota_2 = int(input('Insira o valor da P2: '))
nota_3 = int(input('Insira o valor da Optativa: '))
aluno = [nome, nota_1, nota_2, nota_3, media]
if aluno[-1] > 5:
	alunos_aprovados.append(aluno)
elif aluno[-1] < 5 and aluno[3] == 0:
	alunos_reprovados.append(aluno)
elif aluno[3] > aluno[1] or aluno[3] > aluno[2]:
		aluno[1] = aluno[3] or aluno[2] = aluno[3] if True

elif aluno[3] > aluno[2]:
	aluno[2] = aluno[3]
AHAHAHAHAHAHAH
