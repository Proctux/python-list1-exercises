#  # Introdução a Programação Estruturada (Python)
#  
#  # Prof. M.Sc. Jorge Sandoval - Agosto 2020
#  
#  # Lista de exercicíos 02 #
#  
#  # 1 - Faça um algorítimo que leia os valores A, B, C e imprima na tela se a soma
#  # de A + B é menor que C.
#  
#  a = int(input("Digite o valor de A: "))
#  b = int(input("Digite o valor de B: "))
#  c = int(input("Digite o valor de C: "))
#  
#  sum = a + b
#  
#  if(sum > c):
#    print("A soma de A + B é maior do que C")
#  elif(sum == c):
#    print("A soma de A + B é igual ao valor de C")
#  else:
#    print("A soma de A + B é menor do que C")
#  
#  print()  # It will be used to print a blank line between de exercises.
#  
#  # 2 - Faça um algoritimo que leia o nome, o sexo e o estado civil de uma pessoa.
#  # Caso sexo seja "F" e estado civil seja "CASADA", solicitar o tempo de casada
#  # em anos.
#  
#  name = input("Digite seu nome: ")
#  gender = input("Digite seu sexo (M/F): ")
#  relationship = input("Digite seu estado civil (SOLTEIRO(A)/CASADO(A)/VIUVO(A)/DIVORCIADO(A)): ").upper()
#  marriedTime = 0
#  
#  if(gender == 'F' and relationship == 'CASADA'):
#    marriedTime = int(input("Por favor, digite o tempo de casamento (em anos): "))
#  
#  if(marriedTime != 0):
#    print("Você é %s, do sexo %s, %s a %d anos" % (name, gender, relationship, marriedTime))
#  else:
#    print("Você é %s, do sexo %s, %s" % (name, gender, relationship))
#  
#  print()  # It will be used to print a blank line between de exercises.
#  
#  # 3 - Faça um algorítimo para receber um número qualquer e informar na tela se é par
#  # ou impar.
#  
#  number = int(input("Digite um número qualquer: "))
#  
#  if(number == 0):
#    print("Este é um número neutro")
#  elif(number % 2 > 0):
#    print("Este é um número ímpar")
#  else:
#    print("Este é um número par")
#  
#  print()  # It will be used to print a blank line between de exercises.
#  
#  # 4 -Faça um algoritimo que leia dois valores inteiros A e B. Se os valores forem
#  # iguais, deve-se realizar a soma entre eles, caso contrário, multiplica-se A por B
#  # Ao final, qualquer um dos resultados deve ser atribuído a uma variável C e mostrar
#  # seu resultado na tela.
#  
#  a = int(input("Digite um valor para A: "))
#  b = int(input("Digite um valor para B: "))
#  c = 0
#  
#  if(a == b):
#    c = a + b
#    print("A e B eram iguais. Assim, a soma de ambos é: ", c)
#  else:
#    c = a * b
#    print("A e B eram diferentes. Assim, a multiplicação de ambos é: ", c)
#  
#  print()  # It will be used to print a blank line between de exercises.
#  
#  # 5 - Encontrar o dobro de um número caso ele seja positivo e o seu triplo
#  # caso ele seja negativo, imprimindo seu resultado.
#  
#  num = int(input("Digite um númer qualquer, negativo ou positivo: "))
#  
#  if(num == 0):
#    print("Você digitou %d e este número é neutro" % num)
#  elif(num > 0):
#    num = num * 2
#    print("Você digitou um número positivo. Logo, seu dobro é: %d" % num)
#  else:
#    num = num * 3
#    print("Você digitou um número negativo. Logo, seu triplo é: %d" % num)
#  
#  print()  # It will be used to print a blank line between de exercises.
#  
# 6 - Escreva um algoritimo que leia dois valores booleanos (lógicos) e
# então determine se ambos são VERDADEIROS ou falsos
# 
# firstValue = input("Por favor, digite algo ou aperte enter: ")
# secondValue = input("Por favor, digite algo ou aperte enter novamente: ")
# 
# 
# if(bool(firstValue) == True and bool(secondValue) == True):
#   print("Você digitou algo em ambos os campos anteriores")
#   print("Logo, ambos são VERDADEIROS")
# elif(bool(firstValue) == True or bool(secondValue) == True):
#   print("Você digitou algo em ao menos um campo anterior")
#   print("Logo, ao menos um é VERDADEIRO")
# else:
#   print("Você não digito nada em ambos os campos anteriores")
#   print("Logo, ambos são FALSOS")
# 
# print()  # It will be used to print a blank line between de exercises.
# 
# # 7 - Faça um algoritimo que leia uma variável e some 5 caso seja par
# # ou some 8, caso seja ímpar. Imprimir o resultado desta operação.
# 
# number = int(input("Digite um número: "))
# 
# if(number == 0):
#   print("Você digitou um número neutro")
# elif(number % 2 > 0):
#   number = number + 8
#   print("Você digitou um número ímpar. Logo, somamos 8 ao número que você digitou.")
#   print("O resultado foi: %d" % number)
# else:
#   number = number + 5
#   print("Você digitou um número par. Logo, somamos 5 ao número que você digitou.")
#   print(f"O resultado foi: {number}")
# 
# print()  # It will be used to print a blank line between de exercises.
# 
# # 8 - Escreva um algoritimo que leia três valores inteiros e diferentes e
# # mostre-os em ordem decrescente.
# 
# a = int(input("Digite um valor para A: "))
# b = int(input("Digite um valor para B, diferente de A: "))
# 
# while(b == a):
#   print("Por favor, digite um valor diferente para B")
#   b = int(input("Digite novamente um valor para B: "))
# 
# c = int(input("Digite um valor para C, diferente de A e B: "))
# 
# while(c == a or c == b):
#   print("Por favor, digite um valor diferente para C")
#   c = int(input("Digite novamente um va lor para C: "))
# 
# if(a > b and a > c):
#   if(b > c):
#     print("Seguem os valores em ordem decrescente: A = %d, B = %d, C = %d" % (a, b, c))
#   else:
#     print("Seguem os valores em ordem decrescente: A = %d, C = %d, B = %d" % (a, c, b))
# elif(b > c):
#   if(a > c):
#     print("Seguem os valores em ordem decrescente: B = %d, A = %d, C = %d" % (b, a, c))
#   else:
#     print("Seguem os valores em ordem decrescente: B = %d, C = %d, A = %d" % (b, c, a))
# else:
#   if(a > b):
#     print("Seguem os valores em ordem decrescente: C = %d, A = %d, B = %d" % (c, a, b))
#   else:
#     print("Seguem os valores em ordem decrescente: C = %d, B = %d, A = %d" % (c, b, a))
# 
# print()  # It will be used to print a blank line between de exercises.
# 
# # 9 - Construa um algoritimo que, dado quatro valores A, B, C e D, imprima em tela
# # o maior e o menor
# 
# a = int(input("Digite um valor para A: "))
# b = int(input("Digite um valor para B: "))
# c = int(input("Digite um valor para C: "))
# d = int(input("Digite um valor para D: "))
# 
# maior = a
# menor = a
# 
# numbers = [a, b, c, d]
# 
# for number in numbers:
#   if(number > maior):
#     maior = number
#   if(number < menor):
#     menor = number
# 
# print(f"O maior número que você digitou foi: {maior}")
# print(f"O menor número que você digitou foi: {menor}")
#
# print()  # It will be used to print a blank line between de exercises.
# 
# # 10 - Tendo como dados de entrada a altura e o sexo de uma pessoa
# construa um algoritimo que calcule seu peso ideal, utilizando as
# seguintes fórmulas:
# * Para homens (72.7 * h) - 58.
# * Para mulheres (62.1 * h) - 44.7

height = float(input("Por favor, digite a sua altura, utilizando ponto como separador: "))
gender = input("Por favor, digite seu sexo (M/F): ")

if(gender == 'F'):
  idealWeight = (62.1 * height) - 44.7
  print(f"O peso ideal para o seu sexo é: {idealWeight}")
else:
  idealWeight = (72.7 * height) - 58
  print(f"O peso ideal para o seu sexo é: {idealWeight}")



