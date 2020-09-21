import math

#  # Introdução a Programação Estruturada (Python)
#  
#  # Prof. M.Sc. Jorge Sandoval - Agosto 2020
#  
#  # Lista de exercicíos 04 #

# 01 - Escreva uma função que recebe dois parâmetros e imprime o menor
# dos dois. Se eles forem iguais, imprima que eles são iguais.

def evenOrLower(firstValue, secondValue):
  if(firstValue == secondValue):
    print('Os valores são iguais')
  elif(firstValue > secondValue):
    print(f"O primeiro valor é o maior: {firstValue}")
  else:
    print(f"o segundo valor é o maior: {secondValue}")


firstValue = float(input("Digite o primeiro valor: "))
secondValue = float(input("Digite o segundo valor: "))

evenOrLower(firstValue, secondValue)

print()  # It will be used to print a blank line between de exercises.

# 02 - Escreva uma função que recebe um número n como parâmetro
# e imprime se n é positivo ou negativo.

def isNegativeOrPositive(value):
  if(value == 0):
    print("Este é um número neutro.")
  elif(value > 0):
    print("Este é um número positivo")
  else:
    print("Este é um número negativo")

number = float(input("Digite um número qualquer: "))

isNegativeOrPositive(number)

print()  # It will be used to print a blank line between de exercises.

# 03 - Escreva uma função para imprimir o valor absoluto de um número.

def absoluteValue(number):
  print(abs(number))


number = float(input("Digite um número qualquer: "))

absoluteValue(number)

print()  # It will be used to print a blank line between de exercises.

# 04 - Escreva uma função que recebe dois números (a e b) como
# parâmetro e retorna True caso a soma dos dois seja maior que um
# terceiro parâmetro chamado limite

def isTrue(a, b, limite):
  if((a + b) > limite):
    print("Esta função retornará True")
    return True
  else:
    print("Esta função retornará False")
    return False


a = float(input("Digite um valor A: "))
b = float(input("Digite um valor para B: "))
limite = float(input("Digite um valor para o limite: "))

isTrue(a, b, limite)

print()  # It will be used to print a blank line between de exercises.

# 05 - Escreva uma função que recebe dois números (a e b) como
# parâmetro e retorna a quantidade (0, 1 ou 2) deles que é maior
# que um terceiro parâmetro chamado limite.

def howManyBigger(a, b, limite):
  biggerCounter = 0
  
  if(a > limite): biggerCounter += 1
  if(b > limite): biggerCounter += 1

  print(f"Existem {biggerCounter} valores maiores que o limite informado")


a = float(input("Digite um valor qualquer para A: "))
b = float(input("Digite um valor qualquer para B: "))
limite = float(input("Digite um valor qualquer para o limite: "))

howManyBigger(a, b, limite)

print()  # It will be used to print a blank line between de exercises.

# 06 - Faça uma função que determina se um número é par ou ímpar. Use
# o % para determinar o resto de uma divisão. Por exemplo: 3 % 2 = 1
# e 4 % 2 = 0.

def evenOrOdd(number):
  if(number % 2 == 0):
    print("Este número é par")
  else:
    print("Este número é ímpar")


number = int(input("Digite um número inteiro: "))

evenOrOdd(number)

print()  # It will be used to print a blank line between de exercises.

# 07 - Faça uma função que calcule a área de um círculo. Insira o raio
# como argumento.

def circleArea(radius):
  diameter = math.pow(radius, 2) * math.pi
  print(f"A área do circulo com radios {radius} é de: {round(diameter, 4)}m²")


radius = float(input("Digite o raio do circulo para saber sua área: "))

circleArea(radius)

print()  # It will be used to print a blank line between de exercises.

# 08 - Crie uma função que receba um valor de temperatura em Fahrenheit
# e transforme em Celsius.

def fahrenheitToCelsius(fahTemperature):
  celsius = (fahTemperature - 32) * (5 / 9)
  print(f"A temperatura convertida para Celsius é de: {round(celsius, 2)}°C")


fahTemperature = float(input("Digite o valor da temperatura em Fahrenheit para converter em Celsius: "))

fahrenheitToCelsius(fahTemperature)

print()  # It will be used to print a blank line between de exercises.

# 09 - Duas palavras são anagramas se você puder soletrar uma rearranjando
# as letras da outra. Escreva uma função chamada is_anagram que tome duas
# strings e retorne True se forem anagramas ou False caso contrário.

def is_anagram(firstString, secondString):
  if(sorted(firstString.upper()) == sorted(secondString.upper())):
    print("As palavras são anagramas, por isso essa função retornará True.")
    return True
  else:
    print("As palavras não são anagrams, por isso, essa função retornará False.")
    return False


firstString = input("Digite a primeira palavra: ")
secondString = input("Digite a segunda palavra: ")

is_anagram(firstString, secondString)

print()  # It will be used to print a blank line between de exercises.

# 10 - Utilizando a função anterior, faça a impressão da temperatura,
# em graus Celsius, de 0C a 100C, e todos os valores correspondentes
# em Fahrenheit.

def celsiusToFahrenheit():
  for celsius in range(101):
    fahTemperature = (celsius * (9/5)) + 32
    print(
      f"O valor correspondente em Fahrenheit da temperatura {celsius}°C é: {round(fahTemperature, 2)}°F"
    )


celsiusToFahrenheit()

print()  # It will be used to print a blank line between de exercises.