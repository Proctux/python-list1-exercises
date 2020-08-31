# Introdução a Programação Estruturada (Python)

# Prof. M.Sc. Jorge Sandoval - Agosto 2020

# Lista de exercicíos 01 #

# 1 - Dados dois inteiros a = 30 e b = 40, calcule sua soma e 
# apresente na tela.

print("Exercício 01:")

a = 30
b = 40
soma = a + b
print(soma)

print()  # It will be used to print a blank line between exercises.

# 2 - Dados três inteiros a = 30 e b = 40 e c = 20, faça um programa que
# calcule sua multiplicação e apresente na tela.

print("Exercício 02:")

a = 30
b = 40
c = 20

resultadoMultiplicacao = a * b * c
print(f"O resultado da multiplicação dos números inteiros é: {resultadoMultiplicacao}")

print()  # It will be used to print a blank line between exercises.

# 3 - Dados dois inteirosa = 40 e b = 40, calcule sua divisão e apresente na tela

print("Exercício 03:")

a = 40
b = 40

resultadoDivisao = a / b
print(f"O resultado da divisao é: {resultadoDivisao}")

print()  # It will be used to print a blank line between exercises.

# 4 - Dados dois inteiros a = 50 e b = 25, calcule sua subtração e apresente na tela.

print("Exercício 04:")

a = 50
b = 25

resultadoSubtracao = a - b
print(f"O resultado da subtração é: {resultadoSubtracao}")

print()  # It will be used to print a blank line between exercises.

# 5 - Crie um programa que espera uma entrada do nome do usuário, e após digitar
# pergunte como ele está. Dica: pesquise o comando input do Python.

print("Exercício 05:")

print("Olá! Digite o seu nome: ")
nome = input()
print(f"Como você está, {nome}?")

print()  # It will be used to print a blank line between exercises.

# 6 - Codifique o programa abaixo e analise os resultados:

print("Exercício 06:")

# a_str e b_str guardam strings:
a_str = input("Digite o primeiro número: ")
b_str = input("Digite o segundo número: ")

# Checking if it's returning a String:
# print(isinstance(a_str, str), isinstance(b_str, str))

# a_int e b_int guardam inteiros
a_int = int(a_str)  # converte string / texto -> inteiro
b_int = int(b_str)  # converte string / texto -> inteiro

print()  # It will be used to print a blank line between exercises.

# Checking if it's returning an Integer:
# print(isinstance(a_int, int), isinstance(b_int, int))

# Calcula o valor da soma entre valores que são numeros inteiros
soma_a_b = a_int + b_int
print("A soma de", a_int, "+", b_int, "é igual a:", soma_a_b)

# It could also be written like the line below:
# print("A soma de %d + %d é igual a: %d" % (a_int, b_int, soma_a_b))

print()  # It will be used to print a blank line between exercises.

# 7 - A função int() converte um dado String para um número inteiro.
# Construa um programa que converte o String "123456"

print("Exercício 07:")

text = "123456"
textToNumber = int(text)

print("Usado o método 'isinstance' para checar se é uma instância de String. Caso retorne False, já não é mais uma String:")
print(isinstance(textToNumber, str))  # should return false
print()  # It will be used to print a blank line between exercises.
print("Usado o método 'isinstance' para checar se é uma instância de Integer. Caso retorne True, é um Integer:")
print(isinstance(textToNumber, int))  # should return true

print()  # It will be used to print a blank line between exercises.

# 8 - Construa um programa que divida dois números a = 3 e b = 2,
# e devolva apenas a parte inteira do resultado
# (o número sem as casas depois da vírgula)

print("Exercício 08:")

a = 3
b = 2
resultado = 3 / 2

print(int(resultado))  # should return an interger as 1 instead of 1.5

print()  # It will be used to print a blank line between exercises.

# 9 - Construa um programa que arredonde o número 5.9874 com duas casas
# decimais. Use o comando round

print("Exercício 09:")

a = 5.9874
roundedA = round(a, 2)

print(roundedA)

print()  # It will be used to print a blank line between exercises.

# 10 - Codifique o programa a respeito de formatação de strings abaixo, e
# analise os resultados:

# Formatting operators in Python.

print("Exercício 10:")

print("Teste de formatação de strings")
myInteger = 12345
myFloat = 3.14159  # this number represents PI.
myString = "Curso de Python"

print()  # It will be used to print a blank line between exercises.

print("Integer:", myInteger)
print("Decimal %d e um integer %d" % (myInteger, myInteger))
print("Integer Hexadecimal: %x" % myInteger)

print()  # It will be used to print a blank line between exercises.

print("Float:", myFloat)
print("Default: %f" % myFloat)
print("Exponencial: %e" % myFloat)
print("Justificar Direita: (%10d)" % myFloat)
print("Justificar Esquerda: (%-10d)" % myFloat)

print()  # It will be used to print a blank line between exercises.

print("Forçar 9 dígitos: %.9d" % myInteger)
print("3 dígitos depois do decimal (float): %.3f" % myFloat)
print("Dez e cinco caracteres permitidos na string:")
print("(%.10s) (%.5s)" % (myString, myString))