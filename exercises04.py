import math
import random


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

# 11 - Alanderson quer saber se um endereço IP é válido. Faça
# um programa para ajudar Alanderson a testar se um endereço
# é válido. Para isso, a entrada deve ser um endereço IP
# (Digitado pelo usuário) e o programa deve escrever na tela
# se é válido ou não. Um endereço IPv4 é composto por 4 números
# inteiros entre 0 e 255, separados por um ponto.

ipAddress = input("Digite o endereço de ip: ")

def verifyIpAuthenticity(ipAddress):
  ipArray = ipAddress.split('.')
  numberArray = []
  auth = 0

  for number in ipArray:
    numberArray.append(int(number))

  if(len(numberArray) != 4):
    print("Este é um endereço de Ip inválido.")
  else:
    for number in numberArray:
      if(number > 255 or number < 0):
        auth += 1
  
    if(auth >= 1):
      print("Este é um endereço de Ip inválido.")
    else:
      print("Este é um endereço de Ip válido.")


verifyIpAuthenticity(ipAddress)

print()  # It will be used to print a blank line between de exercises.

# 12 - Dada a função y = 5x + 2, transforme-a em uma função em python
# e crie um programa que determine os valores de Y para x entre -10 a
# +10, onde x é inteiro

def yValue():
  for x in range(-10, 11):
    y = 5 * x + 2
    print(f"Para x = {x}, o valor de y será {y}")


yValue()
print()  # It will be used to print a blank line between de exercises.

# 13 - Escreva uma função que recebe um número como parâmetro e para
# cada número menor que o parâmetro, a função imprime "Fizz" se o
# número for mútiplo de 3, imprime "Buzz" se o número for múltiplo
# de 5 e imprime "FizzBuzz" se o número for múltiplo de três e cinco
# Caso o número não seja múltiplo nem de três nem de cinco, ele deve
# ser impresso. Note que, ao contrário das funções anteriores, sua
# função não deve retornar nada. Ela precisa simplesmente imprimir
# o que foi pedido.

value = int(input("Digite um valor aleatório inteiro: "))

def fizzBuzz(value):
  for number in range(1, value + 1):
    if(number % 3 == 0 and number % 5 == 0):
      print("FizzBuzz")
    elif(number % 3 == 0):
      print("Fizz")
    elif(number % 5 == 0):
      print("Buzz")
    else:
      print(number)


fizzBuzz(value)

print()  # It will be used to print a blank line between de exercises.

# 14 - Escreva uma função que, dado um número nota representando a
# nota de um estudante, coverte um valor de nota para o conceito
# (A, B, C, D, E e F)

mark = float(input("Digite a nota do aluno para saber seu conceito: "))

def markConcept(mark):
  if(mark >= 9.0):
    print(f"Para a nota {mark} o conceito deste aluno será A")
  elif(mark >= 8.0):
    print(f"Para a nota {mark} o conceito deste aluno será B")
  elif(mark >= 7.0):
    print(f"Para a nota {mark} o conceito deste aluno será C")
  elif(mark >= 6.0):
    print(f"Para a nota {mark} o conceito deste aluno será D")
  elif(mark >= 5.0):
    print(f"Para a nota {mark} o conceito deste aluno será E")
  else:
    print(f"Para a nota {mark} o conceito deste aluno será F")


markConcept(mark)

print()  # It will be used to print a blank line between de exercises.

# 15 - Escreva uma função que recebe como entrada uma lista ordenada
# de números e retorna True se um número passado como parâmetro está
# presente na lista.

numberList = [1, 2, 3, 4, 5]
number = int(input("Digite um número para verificar se este está na lista: "))

def isNumberPresent(numberList, number):
  try:
    position = numberList.index(number)
    print(f"O número em questão está presente na lista, na posição {position + 1}")
    return True
  except:
    print(f"O número em questão não está presente nesta lista.")
    return False


isNumberPresent(numberList, number)

print()  # It will be used to print a blank line between de exercises.

# 16 - Escreva uma função que recebe como entrada uma lista ordernada
# de números e retorna o índice do primeiro elemento maior que um
# elemento limite. Se nenhum elemento da lista for maior que o
# limite desejado, retorne o valor -1.

numbers = input("Digite os números da lista separados por vírgula: ")
limit = int(input("Digite o valor do limite: "))


def indexFirstBiggerThan(numbers, limit):
  numbersList = numbers.replace(" ", "").split(",")
  newArray = []
  index = -1

  for number in numbersList:
    newValue = float(number)
    newArray.append(newValue)

  for number in newArray:
    if(number > limit):
      index = newArray.index(number)
      return index
    else:
      pass
  
  return index


print(indexFirstBiggerThan(numbers, limit))

print()  # It will be used to print a blank line between de exercises.

# 17 - escreva uma função que recebe como entrada um número
# inteiro positivo n e retorna a soma de todos os inteiros positivos
# menores ou iguais a n.

value = int(input("Digite um número inteiro qualquer: "))

def sumIntegerLowerThan(value):
  sumValues = 0
  for number in range(value + 1):
    sumValues += number

  return sumValues


print(f"A soma de todos os inteiros até {value} é de:", sumIntegerLowerThan(value))

print()  # It will be used to print a blank line between de exercises.

# 18 - Escreva uma função que recebe como entrada um ano e retorna
# True caso o ano seja bissexto. Caso contrário, retorn false

year = int(input("Digite o ano e verifique se o mesmo é bissexto: "))

def checkLeapYear(year):
  if(year % 400 == 0 or year % 4 == 0 and year % 100 != 0):
    print("Este é um ano bissexto!")
    return True
  else:
    print("Este não é um ano bissexto")
    return False


checkLeapYear(year)

print()  # It will be used to print a blank line between de exercises.

# 19 - Escreva uma função que recebe como entrada um número n e 
# imprime todas as potências de 2 menores ou iguais a n

value = int(input("Digite um número inteiro qualquer: "))

def powerOfTwoLowerThan(value):
  for number in range(value + 1):
    powerOfTwo = math.pow(number, 2)
    print(powerOfTwo)


powerOfTwoLowerThan(value)

print()  # It will be used to print a blank line between de exercises.

# 20 - Escreva uma função que recebe como entrada um número inteiro
# positivo n e imprime a representação binária desse número

number = int(input("Digite um número inteiro qualquer: "))

def intToBinary(number):
  binaryArray = []
  binaryStr = ""

  while(number != 0):
    if(number < 2):
      binaryArray.append(1)
      number = 0
    else:
      mod = number % 2
      binaryArray.append(mod)
      number = number // 2

  binaryArray.reverse()
  
  for binary in binaryArray:
    binaryStr += str(binary)

  print(binaryStr)


intToBinary(number)

print()  # It will be used to print a blank line between de exercises.

# 21- Faça um programa para imprimir todos os números até chegar a um
# n informado pelo usuário. Use uma função que receba um valor n
# inteiro e imprima até a n-ésima linha.

value = int(input("Digite um número inteiro qualquer: "))

def printUntilNumber(value):
  for number in range(value + 1):
    print(number)


printUntilNumber(value)

print()  # It will be used to print a blank line between de exercises.

# 22 - Faça um programa com uma função que necessite de três
# argumentos, e que forneça a soma desses três argumentos

valueOne = int(input("Digite um valor para A: "))
valueTwo = int(input("Digite um valor para B: "))
valueThree = int(input("Digite um valor para C: "))

def sumOfValues(a, b, c):
  return a + b + c


print(" A soma dos valores fornecidos é:", sumOfValues(valueOne, valueTwo, valueThree))

print()  # It will be used to print a blank line between de exercises.

# 23 - Faça um programa com uma função que necessite de um argumento
# A função retorna o valor de caractere "P", se seu argumento for
# positivo e "N", se seu valor for zero ou negativo.

value = int(input("Digite um número qualquer inteiro: "))

def isPositiveOrNegative(value):
  if(value > 0):
    return "P"
  else:
    return "N"


print(isPositiveOrNegative(value))

print()  # It will be used to print a blank line between de exercises.

# 24 - Faça um programa com uma função chamada somaImposto. A
# função possui dois parâmetros formais: taxaImposto, que é a
# quantia de imposto sobre vendas expressa em porcentagem e custo
# que é o custo de um item antes do imposto. A função altera o
# valor de custo para incluir o imposto sobre vendas

custo = float(input("Digite o valor de custo do produto: "))
taxaImposto = float(input("Digite a taxa de imposto sem o simbo de porcentagem: "))

def somaImposto(custo, taxaImposto):
  custo += custo * taxaImposto / 100
  return custo


print("O novo valor de custo é: R$ ", somaImposto(custo, taxaImposto))

print()  # It will be used to print a blank line between de exercises.

# 25 - Faça um programa que converta da notação de 24 horas
# para a notação de 12 horas. Por exemplo, o programa deve
# converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros
# Deve haver pelo menos duas funções: uma para fazer a conversão
# e uma para a saída. Registre a informação A.M/P.M como um valor
# 'A' para A.M e 'P' para P.M. Assim, a função para efetuar as
# conversões terá um parâmetro formal para registrar se é A.M ou
# P.M. Inclua um loop que permita que o usuário repita esse calculo
# para novos valores de entrada todas as vezes que desejar.

repeat = "S"


while(repeat == "S"):
  hours = int(input("Digite as horas, sem os minutos, com duas casas no máximo: "))
  minutes = int(input("Agora, digite os minutos: "))

  def hourCheck(hours):
    if(hours > 12):
      return "A.M"
    else:
      return "P.M"


  def hourConvertor(hours, minutes):
    notation = hourCheck(hours)

    if(hours >= 24):
      print("Lamento, o horário digitado é maior do que 23:59")
    elif(hours > 12):
      hours = hours - 12
      print(f"{hours}:{minutes} {notation}")
    else:
      print(f"{hours}:{minutes} {notation}")

  hourConvertor(hours, minutes)  
  response = input("Deseja repetir a operação? (S/N): ")
  repeat = response.upper()
  
  
  
print()  # It will be used to print a blank line between de exercises.

# 26 - Faça um programa que use a função valorPagamento para
# determinar o valor a ser pago por uma prestação de uma conta
# O programa deverá solicitar ao usuário o valor da prestação
# e o número de dias em atraso e passar estes valores para a função
# valorPagamento, que calculará o valor a ser pago e devolverá este
# valor ao programa que a chamou. O programa deverá então exibir o
# valor a ser pago na tela. Após a execução o programa deverá voltar
# a pedir outro valor de prestação e assim continuar até que seja
# informado um valor igual a zero para a prestação. Neste momento
# o programa deverá ser encerrado, exibindo o relatório do dia, que
# conterá a quantidade e o valor total de prestações pagas no dia.
# O cálculo do valor a ser pago é feito da seguinte forma: Para
# pagamentos sem atraso, cobrar o valor da prestação.Quando houver
# atrasos, cobrar 3% de multa, mais 0,1% de juros por dia de atraso

def valorPagamento(valorPrestacao, diasAtraso):
  if(diasAtraso > 0):
    novoValor = valorPrestacao + (valorPrestacao * 0.03) + (valorPrestacao * (diasAtraso * 0.001))
    return novoValor
  return valorPrestacao

def paymentsReport():
  payDayList = []
  valorPrestacao = 0.01

  while(valorPrestacao > 0):
    valorPrestacao = float(input("Digite o valor da prestação: R$ "))
    if(valorPrestacao == 0):
      break
    else:
      diasAtraso = int(input("Digite a quantidade de dias em atraso: "))
      amount = valorPagamento(valorPrestacao, diasAtraso)
      payDayList.append(amount)
  
  payDayListTotal = sum(payDayList)

  print(f"A quantidade total de prestações pagas foram: {len(payDayList)}")
  print(f"O montante total pago foi de: R$ {round(payDayListTotal, 2)}")


paymentsReport()

print()  # It will be used to print a blank line between de exercises.

# 27 - Faça uma função que informe a quantidade de dígitos de um
# determinado número inteiro informado

def qtyOfDigits():
  value = int(input("Digite um número qualquer: "))
  print("O número informado possuí:", len(str(value)), "dígito(s)")


qtyOfDigits()

print()  # It will be used to print a blank line between de exercises.

# 28 - Reverso do número. Faça uma função que retorne o reverso
# de um número inteiro informado. Por exemplo, 127 - 721.

def reverseNumber():
  value = int(input("Digite um número qualquer: "))
  strValue = str(value)
  print(f"O valor reverso do número informado é: {strValue[::-1]}")


reverseNumber()

print()  # It will be used to print a blank line between de exercises.

# 29 - Jogo de Craps. Faça um programa que implemente um jogo de
# craps. O jogador lança um par de dados, obtendo um valor entre
# 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você tira
# um "natural" e ganhou. Se você tirar 2,3 ou 12, isto é chamado
# de "craps" e você perdeu. Se na primeira jogada, você fez um
# 4, 5, 6, 8, 9 ou 10, este é seu "Ponto". Seu objetivo agora é
# continuar jogando os dados até tirar este número novamente. Você
# perde, no entanto, se tirar um 7 antes de tirar esse ponto novamente.

def crapsGame():
  diceOne = random.randint(1, 6)
  diceTwo = random.randint(1, 6)
  sumDice = diceOne + diceTwo
  point = sumDice

  if(sumDice == 7 or sumDice == 11):
    print(f"Você tirou um Natural e ganhou! Valor da soma dos dados: {sumDice}")
  elif(sumDice == 2 or sumDice == 3 or sumDice == 12):
    print(f"Você tirou um craps e perdeu! Valor da soma dos dados: {sumDice}")
  else:
    while(sumDice != 7 or sumDice != point):
      diceOne = random.randint(1, 6)
      diceTwo = random.randint(1, 6)
      sumDice = diceOne + diceTwo
      print(f"Novos valores de soma dos dados x valor 1° jogada: {sumDice} x {point}")
      if(sumDice == point):
        print("Você Tirou o mesmo número e ganhou")
        break
      elif(sumDice == 7):
        print("Você tirou um 7 e perdeu")
        break
      else:
        pass

  
crapsGame()

print()  # It will be used to print a blank line between de exercises.

from datetime import datetime, date

# 30 - Data com mês por extenso. Construa uma função que receba uma
# data no formato DD/MM/AAAA e devolva uma string no formato D de
# mesPorExtenso de AAAA. Opcionalmento, valide a data e retorne 
# Null caso a data seja inválida.

dateValue = input("Digite a data que deseja converter, (DD/MM/AAA): ")

def dateConversor(dateValue):
  try:
    data = datetime.strptime(dateValue, '%d/%m/%Y').date()
    dataFormatada = data.strftime('%d/%B/%Y')
    dateStr = str(dataFormatada).replace("/", " de ")
    print(f"A data será retornada da seguinte forma: {dateStr}")
    return dateStr
  except:
    print("Data digitada é inválida. Retornando None.")
    return None


dateConversor(dateValue)

print()  # It will be used to print a blank line between de exercises.

# 31 - Embaralha palavra. Construa uma função que receba uma
# string como parâmetro e devolva outra string com os caracteres
# embaralhados. Por exemplo: se a função receber a palavra python
# pode retornar npthyo, ophtyn, ou qualquer outra combinação
# possível, de forma aleatória. Padronize em sua função que todos
# os caracteres serão devolvidos em caixa alta ou caixa baixa
# independentemente de como foram digitados.

from random import sample

def shuffle(word):
    arraySample = sample(word, len(word))
    newString = ''.join(arraySample)
    
    while(newString == word):
        arraySample = sample(word, len(word))
        newString = ''.join(arraySample)
    
    print(newString)


word = input('Digite algo: ')
shuffle(word)

print()  # It will be used to print a blank line between de exercises.

# 32 - Desenha moldura. Construa uma função que desenhe um retângulo
# usando os caracteres "+", "" e "-". Esta função deve receber dois
# parâmetros, linhas e colunas, sendo que o valor por omissão é o
# valor mínimo igual a 1 e o valor máximo é 20. Se os valores fora da
# faixa forem informados, eles devem ser modificados para os valores
# dentro da faixa de forma elegante.

def moldurePrint(height, width):
    if(height > 20):
        height = 20
        print(f"Você digitou mais do que {height}. Iremos usar o valor máximo de 20")
    elif(height < 1):
        height = 1
        print(f"Você digitou menos do que {height}. Iremos usar o valor mínimo de 1")
    
    if(width > 20):
        width = 20
        print(f"Você digitou mais do que {height}. Iremos usar o valor máximo de 20")
    elif(width < 1):
        width = 1
        print(f"Você digitou menos do que {height}. Iremos usar o valor mínimo de 1")
    
    print("+" * width)

    for space in range(height - 2):
        print("-" + " " * (width - 2) + "-")
    
    print("+" * width)     
            


height = int(input("Digite a altura do retângulo (min: 1 / max: 20): "))
width = int(input("Digite a largura do retângulo (min: 1 / max: 20): "))

moldurePrint(height, width)

print()  # It will be used to print a blank line between de exercises.

# 33 - O número de combinações possíveis de m elementos em grupo de
# n elementos (n! = m) é dada pela fórmula de combinação m!/((m-n)!n!).
# Escreva um programa que lê dois parâmetros m e n e calcula a
# combinação de m, n a n.

def factorialCalcule(mValue, nValue):
  varFactorial = 1
  counter = 1

  while(counter < mValue):
    counter += 1
    varFactorial *= counter
  
  mFactorial = varFactorial

  varFactorial = 1
  counter = 1

  while(counter < nValue):
    counter += 1
    varFactorial *= counter
  
  nFactorial = varFactorial

  varFactorial = 1
  counter = 1

  while(counter < (mValue - nValue)):
    counter += 1
    varFactorial *= counter
  
  m_nFactorial = varFactorial

  finalValue = mFactorial / (m_nFactorial * nFactorial)
  return finalValue


mFactorial = int(input("Digite um valor inteiro para o fatorial de M: "))
nFactorial = int(input("Digite um valor inteiro para o fatorial de N: "))

print(f"O valor da combinação fatorial M, N a N é :", factorialCalcule(mFactorial, nFactorial))

print()  # It will be used to print a blank line between de exercises.

# 34 - Complete a função fatorial abaixo, que recebe como parâmetro
# um número inteiro k, k >= 0, e retorna k!. Escreva apenas o corpo
# da função. Observe que o código já inclui chamadas para a função
# fatorial, para que você possa testar a função.

def factorial(kFactorial):
  varFactorial = 1
  counter = 1

  while(counter < kFactorial):
    counter += 1
    varFactorial *= counter
  
  return varFactorial


kFactorial = int(input("Digite o valor inteiro para ver seu valor fatorial: "))
print("O valor fatorial para o valor digitado é:", factorial(kFactorial))

print()  # It will be used to print a blank line between de exercises.

# 35 - Escreva uma função que receba dois inteiros, m e n, como
# parâmetros e retorna a combinação m!/((m-n)!n!)

def factorialCalcule(mValue, nValue):
  varFactorial = 1
  counter = 1

  while(counter < mValue):
    counter += 1
    varFactorial *= counter
  
  mFactorial = varFactorial

  varFactorial = 1
  counter = 1

  while(counter < nValue):
    counter += 1
    varFactorial *= counter
  
  nFactorial = varFactorial

  varFactorial = 1
  counter = 1

  while(counter < (mValue - nValue)):
    counter += 1
    varFactorial *= counter
  
  m_nFactorial = varFactorial

  finalValue = mFactorial / (m_nFactorial * nFactorial)
  return finalValue


mFactorial = int(input("Digite um valor inteiro para o fatorial de M: "))
nFactorial = int(input("Digite um valor inteiro para o fatorial de N: "))

print(f"O valor da combinação fatorial M, N a N é :", factorialCalcule(mFactorial, nFactorial))

print()  # It will be used to print a blank line between de exercises.

# 36 - Usando funções fatorial e combinação dos exercícios anteriores
# escreva um programa que lê um inteiro n, m >= 0 e imprime os
# coeficientes da expansão de (x+y) elevado a n.

def expasionFactorial():
    n = int(input("Digite n: "))

    cont = 0
    while cont <= n:
        print("Coeficiente de x^%d y^%d: %d"%(n-cont, cont, factorialCalcule(n, cont)))
        cont += 1


expasionFactorial()

print()  # It will be used to print a blank line between de exercises.

# 37 - Um palíndromo é uma palavra que se soletra da mesma forma
# nos dois sentidos, como "osso" e "reviver". Recursivamente, uma
# palavra é um palíndromo se a primeira e a última letra forem
# iguais e o meio for um palíndromo.

def isPalindromo(string):
  reverseString = string[::-1].lower()
  if(reverseString == string.lower()):
    print("Esta palavra é um palíndromo")
  else:
    print("Esta palavra não é um palíndromo")

word = input("Digite uma palavra para ver se a mesma é um palíndromo: ")
isPalindromo(word)

print()  # It will be used to print a blank line between de exercises.

# 38 - Um número a é uma potência de b se for divisível por b e a/b
# for uma potência de b. Escreva uma função chamada isPower que receba
# os parâmetros a e b e retorne True se a for uma potência de b.

def isPower(valueA, valueB):
  valueADivisor = valueA

  while(valueADivisor >= valueB):
    valueADivisor = valueADivisor / valueB
  
  if(valueADivisor == 1):
    print(f"Este número é uma potência de {valueB}")
  else:
    print(f"Este número não é uma potência de {valueB}")



valueA = int(input("Digite um valor inteiro para A: "))
valueB = int(input("Digite um valor inteiro para B: "))

isPower(valueA, valueB)

print()  # It will be used to print a blank line between de exercises.

# 39 - O maior divisor comum (MDC, ou GDC em inglês) de a e b é o
# maior número que divide ambos sem sobrar resto. Um modo de encontrar
# o MDC de dois números é observar qual é o resto r quando a é dividido
# por b, verificando que gcd(a, b) = gcd(b, r). Como caso-base, podemos
# usar gcd(a, 0) = a. Escreva uma função chamada gcd que receba os
# parâmetros a e b e devolva o maior  divisor comum.

def gcd(valueA, valueB):
  if(valueB == 0):
    return valueA
  else:
    print(valueA % valueB)
    return gcd(valueB, valueA % valueB)


valueA = int(input("Digite um valor para A: "))
valueB = int(input("Digite um valor para B: "))

print(gcd(valueA, valueB))

print()  # It will be used to print a blank line between de exercises.

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

