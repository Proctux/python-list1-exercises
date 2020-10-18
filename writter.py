
# def cortar(lista):
#   lista.pop(0)
#   lista.pop()
#   print(lista)

# lista = [1, 2, 3]

# cortar(lista)

# # 2 - Escreva uma função chamada mais_frequente
# # que receba uma string e exiba as letras em ordem
# # descrescente.

# lista = ['z', 'b', 'c']

# def mais_frequente(lista):
#   print(sorted(lista, reverse=True))

# mais_frequente(lista)

# 3 - Escreva um programa que leia uma lista de palavras
# de um arquivo e imprima todos os conjuntos de
# palavras que são anagramas. 

openFile = open("/home/luiz/projetos/pythonExercises/arquivo.txt", 'r')

arrayOfArrays = []

for linha in openFile:
  valores = linha.lower().split()
  arrayOfArrays.append(valores)
