#                                                        UNIVERSIDADE FEDERAL RURAL DO RIO DE JANEIRO  / 11/03/2021
#     AUTOR:     ERICK AUGUSTO DE ALMEIDA
# MATRÍCULA:     20190078717
# PROFESSOR:     ROBSON MARINHO
# PROPÓSITO:     DESAFIO  II - LISTAS
#     GRUPO:     EFRAIM, TAMIRES, ERICK
# INSTITUTO: Instituto de Ciências Exatas - UFRRJ
# Observações: Desafio concluído, as operações seguintes são apenas pequenos aprimoramentos, entretanto, já foram implementadas as maneiras de captar a string e posteriormente tratá-las adequadamente. 
# Período: 2020.1
# Turma: 
from functools import reduce
global aprovados
global reprovados
global total
global media_provas
alunos = list()
aprovados = list()
reprovados = list()
media_provas = list()
nome_turma = str(input('Digite o nome da turma: ')).upper()
file = open('DADOS BRUTOS DA TURMA'+' '+nome_turma+'.txt', 'a')
#file_r = open('DADOS BRUTOS DA TURMA' + ' ' + nome_turma+'.txt', 'r')
#alunos.append(file_r.read()) // Apenas sugestões a serem implementadas

def __main__(alunos, aprovado, reprovado):
    nome = input(str('Digite o nome do aluno: '))
    print('\n')
    prova_1 = float(input('Insira o valor da PR1: '))
    print('\n')
    prova_2 = float(input('Insira o valor da PR2: '))
    print('\n')
    prova_3 = float(input('Insira o valor da OPT: '))
    print('\n')
    if prova_1 < prova_3 and prova_1 < prova_2:
        prova_1 = prova_3
        pass
    elif prova_2 < prova_3:
        prova_2 = prova_3
    elif prova_1 == prova_2 and prova_3 > prova_2:
        prova_2 = prova_3
    else:
        pass
    media_pond = float((1*prova_1+2*prova_2)/(1+2))            
    _media_pond = str(media_pond)
    aluno = [nome, prova_1, prova_2, prova_3, '',_media_pond[:4],media_pond]    
    media_provas.append(media_pond)
    x = 1
    if float(aluno[6]) >= 5:
        aluno[4] = 'Aprovado'        
        aprovado.append(x)
        alunos.append(aluno)      
    elif float(aluno[6]) < 5:
        aluno[4] = 'Reprovado'        
        reprovado.append(x)
        alunos.append(aluno)
    else:
        pass
    alunos_totais = len(alunos)
    media_turma = 0
    todas_notas = int(reduce(lambda nota__, nota_: nota__ + nota_, media_provas))
    media_turma = todas_notas/len(alunos)
    menor_nota = min(media_provas)
    maior_nota = max(media_provas)
    action = input('Digite [D] + [Enter] para [D]etalhar ou 2x[Enter] para Continuar: [ [D]+[Enter] / 2x[Enter] ] \n')
    STRINGFILE = str(alunos).join(' \n')
    file.writelines(str(STRINGFILE))    
    print('-'*80)
    if action == 'D' or action == 'd':
        print(('+'+ '//'*29+ '+\n') +'|  ' + '{:<5}{:>1}{:>16}{:>5}{:>5}{:>8}  {:>8}'.format('ID','NOME ','P1 ', 'P2', 'OPT','MÉDIA', 'SITUAÇÃO',))
        print('='*60)
        for i, a in enumerate(alunos):
            print('Nº{:<2}{:<3}{:<20}{:<6}{:<5}{:<6}{:<6}{:>5}'.format('|',i+1,a[0][0:15], a[1],a[2], a[3], a[5], a[4],' |' ))
            print('-'*60)
        print('-'*60 + '\n')
        print(f'\\\\Total de alunos: {alunos_totais} \n')
        print('========DESTAQUES=========\n')    
        print('\\\\Menor nota encontrada: {:.1f} \n'.format(menor_nota))
        print('\\\\Maior nota encontrada: {:.1f} \n '.format(maior_nota))    
        print('>>'*13 + '\n')   
        print('=====SITUAÇÃO DA TURMA====')    
        print('-*'*13 + '\n')
        print(f'\\\\Total de aprovados: ', len(aprovado), ' \n')
        print(f'\\\\Total de reprovados: ', len(reprovado), ' \n')
        print('*-'*13)
        print('\\\\Percentual de aprovados: {:.2f}%'.format((len(aprovados)/alunos_totais)*100))
        print('\\\\Percentual de reprovados: {:.2f}%'.format((len(reprovados)/alunos_totais)*100))
        print('\\\\Média da turma: {:.1f} \n'.format(media_turma))    
        print('*-'*13)
        pass
    else:
        pass
while True:
    __main__(alunos, aprovados, reprovados)
    action = input('Pressione [Enter] para continuar ou [E] + [Enter] para encerrar. ')
    if action == 'E' or action == 'e':   
        break        
    else:
        continue
    
