# 40 - Campo minado é um jogo que se tornou muito popular por
# acompanhar o sistema operacional Microsoft Windows. Nesse jogo,
# o campo minado pode ser representado por uma matriz retangular.
# O jogador deve revelar todas as posições livres (sem bomba) da
# matriz, clicando em uma posição com conteúdo desconhecido. O
# jogo acaba quando o jogador clicar em uma posição com bomba, ou
# quando todas as posições livres forem abertas. Nesse exercício,
# você deve implementar algumas funções que podem ser utilizadas
# na implementação desse jogo.
# A - Escreva uma função que recebe como parâmetros uma matriz inteira
# A e uma posição (lin, col) da matriz, e conta quantas posições ao
# redor da posição (lin, col) contém o valor -1 (valor adotado para
# representar a bomba)
# B - Escreva um programa que lê uma matriz A de 0's (posições livres)
# e -1's (bomba). Utilizando a função do item anterior, o programa
# deve computar e imprimir a quantidade de bombas ao redor de cada
# posição livre da matriz.

def bombCount(A, row, col):
  positionsWithBomb = 0
  if row > 0 and A[row-1][col] == 1:
    positionsWithBomb += 1
  if row < len(A) - 1 and A[row+1][col] == -1:
    positionsWithBomb += 1
  if col > 0 and A[row][col - 1] == 1:
    positionsWithBomb += 1
  if col < len(A[0]) - 1 and A[row][col+1] == -1:
    positionsWithBomb += 1
  
  return positionsWithBomb

m = int(input("Número de linhas: "))
n = int(input("Número de colunas: "))
A = []

for i in range(m):
  linha = []
  for j in range(n):
    linha.append(int(input("Digite A[%d][%d]: " % (i, j))))
  A.append(linha)

for i in range(m):
  for j in range(n):
    print("Bombas ao redor de A[%d][%d]: %d" % (i, j, bombCount(A, i, j)))


print()  # It will be used to print a blank line between de exercises.