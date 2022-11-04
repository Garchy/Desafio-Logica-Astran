'''
1º Desafio

Desafio: Escreva uma função que solicita
o Nome do Aluno,e a nota de 4 provas e
retorne a média aritmética das notas.
'''
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

    #Essa etapa salva as notas recebidas e associa ao aluno 
    alunoNota[nome] = {
      'nota1' : nota1, 'nota2' : nota2, 'nota3' : nota3, 'nota4' : nota4
      }

  i = 0
  for aluno in alunoNota:
    print(f'\nAluno = {aluno}' +
      #Soma as notas de cada aluno e decide qual valor para divdir e obter a média
      f' // Media = {sum(alunoNota[aluno].values())/len(alunoNota[aluno].values())}')

'''
2º Desafio

Crie um script que receba uma string e 
retorne a maior letra segundo a ordem 
alfabética em minusculo.
'''
def desafio2(palavra):
  maior = -1
  for p in palavra:
    if ord(p) > maior: #Verifica o numero ASCII de cada letra
      maior = ord(p) #Caso seja maior que o anterior salvo, sobrepõe
  print("Maior letra: " + chr(maior)) #Imprime o caractere do numero ASCII associado

'''
3º Desafio

Escreva uma função que receba um string
contendo um nome completo e retorne uma string
com o seguinte formato (ULTIMO_SOBRENOME).
E as primeiras letras dos restantes dos nomes
em MAIÚSCULO, separados por virgula e pontos.)
'''
def desafio3(nome):
  listaNome = []

  #Divide o nome inteiro considerando os espaços e salva o ultimo
  ultimoNome = nome.split(' ')[len(nome.split(' '))-1]
  
  #Percorre todos os nomes antes do ultimo 
  #E salva a primeira letra de cada nome em uma lista
  for nomes in range(len(nome.split(' '))):
    if nome.split(' ')[nomes] != ultimoNome:
      listaNome.append(nome.split(' ')[nomes][0])
  
  #Junta todos os nomes da lista por um " . " em uma string
  nomes = '.'.join(listaNome)
  print(f'{ultimoNome.upper()}, {nomes}.')


desNum = input("Digite o numero do desafio (1, 2 ou 3): ")

match desNum:
  case '1':
    desafio1()
  case '2':
    frase = input("Digite uma frase: ")
    desafio2(frase)
  case '3':
    nome = input("Digite um nome: ")
    desafio3(nome)
  case _:
    print("Opção Inválida!")