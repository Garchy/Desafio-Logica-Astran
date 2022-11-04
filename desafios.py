def desafio1():

  alunoNota = {}

  repet = input("\nInforme a quantidade de alunos: ")
  repet = int(repet)

  for _ in range(repet):    
    nome = input('\nEscreva seu nome: ')

    nota1 = input('Digite sua primeira nota: ')
    nota2 = input('Digite sua segunda nota: ')
    nota3 = input('Digite sua terceira nota: ')
    nota4 = input('Digite sua quarta nota: ')

    nota1 = int(nota1)
    nota2 = int(nota2)
    nota3 = int(nota3)
    nota4 = int(nota4)

    alunoNota[nome] = {
      'nota1' : nota1, 'nota2' : nota2, 'nota3' : nota3, 'nota4' : nota4
      }

  i = 0
  for aluno in alunoNota:
    print(f'\nAluno = {aluno}' +
      f' // Media = {sum(alunoNota[aluno].values())/len(alunoNota[aluno].values())}')


def desafio2(palavra):
  maior = -1
  for p in palavra:
    if ord(p) > maior:
      maior = ord(p)
  print(chr(maior))

def desafio3(nome):
  listaNome = []
  ultimoNome = nome.split(' ')[len(nome.split(' '))-1]
  
  for nomes in range(len(nome.split(' '))):
    if nome.split(' ')[nomes] != ultimoNome:
      listaNome.append(nome.split(' ')[nomes][0])
  
  nomes = '.'.join(listaNome)
  print(f'{ultimoNome.upper()}, {nomes}.')


desafio3('George Raymond Richard Martin')