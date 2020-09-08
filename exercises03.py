import math
import datetime

#  # Introdução a Programação Estruturada (Python)
#  
#  # Prof. M.Sc. Jorge Sandoval - Agosto 2020
#  
#  # Lista de exercicíos 03 #


# 01 - Faça um programa que exiba 30 vezes na tela a mensagem
# "Olá, tudo bem?".

for message in range(30):
  print("Olá, tudo bem?")

print()  # It will be used to print a blank line between de exercises.

# 02 - Faça um algoritimo que leia 10 valores inteiros e
# mostre a sua soma.

soma = 0

for number in range(10):
  contador = number + 1
  valor = int(input(f"Digite o {contador}° valor inteiro: "))
  soma += valor
  print("A soma dos valores até o momento é: ", soma)

print()  # It will be used to print a blank line between de exercises.

# 03 - Escreva um programa que lê 15 valores reais, encontra o maior
# e o menor deles e mostra o resultado.

maior = ''
menor = ''

for number in range(15):
  contador = number + 1
  valor = float(input(f"Digite o {contador}° valor real: "))

  if(maior == ''):
    maior = valor
  elif(menor == ''):
    menor = valor
  elif(maior < valor):
    maior = valor
  elif(menor > valor):
    menor = valor

print("O maior número digitado foi: ", maior)
print("O menor número digitado foi: ", menor)

print()  # It will be used to print a blank line between de exercises.

# 04 - Faça um programa para exibir a tabuada de 0 a 9.

a = 0
b = 0

for x in range(110):

  result = a * b
  print(f"A multiplicação de {a} e {b} deu: {result}")
  b += 1
  

  if(b == 11):
    b = 0
    a +=1
  
print()  # It will be used to print a blank line between de exercises.

# 05 - Faça um programa que calcula e escreve a seguinte soma
# soma = 1/1 + 3/2 + 5/3 + 7/4 ... + 99/50

counter = 1
baseCounter = 1
total = 0

for numbers in range(49):
  value = counter / baseCounter
  total += value
  counter += 2
  baseCounter += 1

print(round(total, 2))

print()  # It will be used to print a blank line between de exercises.

# 06 - Faça um programa que calcula o produto dos números digitados
# pelo usuário. O programa em deve permitir que o usuário digite uma
# quantidade não determinada de números. Ele encerra quando o usuário
# digita o valor zero.

number = 1
total = 1

while(number != 0):
  value = int(input("Digite um número qualquer: "))
  total *= value
  print(f"O produto dos números digitados é: {total}")
  value = int(input("Deseja continuar? Caso não, digite 0 para sair: "))



print()  # It will be used to print a blank line between de exercises.

# 07 - Dado um número n inteiro e positivo, dizemos que n é perfeito
# se n for igual a soma de seus divisores positivos diferentes de n.
# Construa um programa que verifica se um dado número é perfeito.
# Ex: 1 + 2 + 3 = 6

def perfeito(n):
    soma=0
    for val in range(1,n):
        if n % val == 0:
            soma += val

    if soma==n:
        return True
    else:
        return False
        
def exibe():
    n = int(input('Exibir perfeitos até o número: '))
    
    for val in range(1,n+1):
        if(perfeito(val)):
            print(val)
    
while True:
    exibe()

print()  # It will be used to print a blank line between de exercises.

# 08 - Chico tem 1,50 metros e cresce 2 centímetros por ano, enquanto
# Zé tem 1,10 metros e cresce 3 centímetros por ano. Construa um
# algoritimo que calcule e imprima quantos anos serão necessários
# para que Zé seja maior que Chico.

ChicoHeight = 1.50
ZeHeight = 1.10
counter = 0

while(ZeHeight < ChicoHeight):
  ZeHeight += 0.03
  ChicoHeight += 0.02
  counter += 1

print(f"Serão necessários {counter} anos para que Zé passe Chico.")

print()  # It will be used to print a blank line between de exercises.

# 09 - Elabore um algoritimo que leia um conjunto indeterminado
# de valores e informe, ao final, o maior e o menor valores lidos
# O algoritimo deverá ser encerrado se o usuário digitar um valor
# negativo ou o valor 0.

menor = ''
maior = ''
number = 1

while(number > 0):
  value = float(input("Digite um número aleatório qualquer (Digite 0 ou um número negativo para encerrar): "))

  if(value <= 0):
    break

  if(menor == ''):
    menor = value
  elif(menor > value):
    menor = value

  if(maior == ''):
    maior = value
  elif(maior < value):
    maior = value

if(menor == ''):
  print("Desculpe, você não digitou números suficientes")
elif(menor == ''):
  print("O maior número digitado foi: ", menor)
  print("O menor número digitado foi: ", menor)
else:
  print("O maior número digitado foi: ", maior)
  print("O menor número digitado foi: ", menor)


print()  # It will be used to print a blank line between de exercises.

# 10 - Faça um algoritimo que solicite um valor ao usuário e gere
# a tabuada deste valor. Por exemplo, se o usuário digitar 2 deverá
# ser gerada a tabuada do número 2, variando de 0 a 10

value = int(input("Digite um número para ser exibida sua tabuada: "))


for number in range(11):
  result = value * number
  print(f"{number} * {value} =", result)

print()  # It will be used to print a blank line between de exercises.

# 11 - Faça um algoritimo que gere, automaticamente, a tabuada
# dos valores de 1 a 10. Por exemplo, 1 x 1 = 1, 1 x 2 = 2 ...
#1 x 10 = 10, 2 x 1 = 2, ..., 10 x 10 = 100.

a = 0
b = 0

for x in range(121):

  result = a * b
  print(f"A multiplicação de {a} e {b} deu: {result}")
  b += 1
  

  if(b == 11):
    b = 0
    a +=1
  
print()  # It will be used to print a blank line between de exercises.

# 12 - Faça um programa que solicita ao usuário dois valores
# inteiros e positivos. O programa deve usar laço
# de repetição para calcular e escrever o resultado da base
# elevado ao expoente (potência).


number = 1

while(number != 0):
  base = int(input("Digite um valor para a base: "))
  expo = int(input("Digite um valor para o expoente: "))
  result = math.pow(base, expo)
  print("O resultado foi: ", result)
  print()
  print("Deseja realizar uma nova operação? (digite um numero diferente de zero caso sim).")
  number = int(input())

print()  # It will be used to print a blank line between de exercises.

# 13 - Faça um programa que solicita ao usuário uma quantidade
# indeterminada de números inteiros. O programa deve escrever
# a média aritimética apenas dos números pares. A entrada de
# dados deve ser encerrada quando o número 0 (ZERO) for digitado

number = 1
total = 0
counter = 1

while(number != 0):
  value = int(input("Por favor, digite o primeiro número inteiro: "))
  
  if(value % 2 == 0):
    total += value
    result = total / counter
    print(f"A média aritimética dos números é {result}")
    counter += 1

  number = int(input("Deseja continuar? (Digite 0 para sair): "))

print()  # It will be used to print a blank line between de exercises.

# 14 - Faça um programa que solicita ao usuario um número real
# positivo. Verifique se o número é realmente positivo, e em caso
# contrário, solicite ao usuário para digitar novamente (este
# processo pode se repetir inúmeras vezes e é chamado de
# consistência, pois garante que o número será válido após a
# entrada de dados). Saídas:
# - Pedido ao usuário = "Digite um número real positivo";
# - Caso número válido = "O número digitado é valido";
# - Caso número inválido = "Número inválido, tente novamente".

number = float(input("Por favor, digite um número real positivo: "))

while(number < 0):
  print("O número digitado é inválido. Por favor, digite novamente: ")
  number = float(input())

print("O número digitado é válido.")

print()  # It will be used to print a blank line between de exercises.

# 15 - Escreva um programa que gera números entre 1000 e 1999
# e mostra aqueles que divididos por 11 dão resto 5

for number in range(1000, 1999):
  if(number % 11 == 5):
    print(f"{number} é um dos número que dividido por 11 sobra 5")

print()  # It will be used to print a blank line between de exercises.

# 16 - Um determinado material radioativo perde metade de sua massa
# a cada 50 segundos. Dada a massa inicial, em gramas, fazer um
# programa que calcule o tempo necessário para que essa massa se
# torne menor do que 0,5 grama. O programa em C deve escrever a
# massa inicial, a massa final e o tempo calculado em horas,
# minutos e segundos.

weight = float(input(
  "Digite a massa inicial do material radioativo (utilizando ponto como separador): "))

newWeight = weight

counter = 0

while(newWeight > 0.5):
  newWeight = newWeight / 2
  counter += 50

time = datetime.timedelta(seconds=counter)

print(f"A massa inicial é de {weight}g, e a massa final é de {newWeight}g")
print(f"Serão necessários {time} para que a massa se torne menor que 0,5g")

print()  # It will be used to print a blank line between de exercises.


# 17 - Faça um programa para gerar os n primeiros termos da sequencia
# 1 1 2 3 5 8 13 21 34 55 89...

quantity = int(input("Digite o n° de termos iniciais da sequência de Fibonacci que deseja visualizar: "))

arrFibonacci = [1, 1]
value = 1

for number in range(quantity):
  print(value)
  value = arrFibonacci[0] + arrFibonacci[1]
  arrFibonacci.append(value)
  arrFibonacci.pop(0)


print()  # It will be used to print a blank line between de exercises.

# 18 - Faça um programa para uma calculadora simples que solicita
# ao usuário dois operandos como entrada, seleciona uma das opções
# da lista (1 - soma, 2 - produto, 3 - divisão, 4 potência) e
# exibe o resultado. O algoritimo deve executar repetidamente até
# que dois operandos informados sejam igual a zero. Utilize uma
# variável tipo real para exibir o resultado.

total = 0

while True:
  valueOne = float(input("Digite o primeiro valor: "))
  func = int(input("Digite qual operação deseja fazer: 1 - soma, 2 - produto, 3 - divisão, 4 potência: "))
  valueTwo = float(input("Digite o segundo valor: "))

  if(valueOne == 0 and valueTwo == 0):
    break
  
  if(func == 1):
    total = valueOne + valueTwo
  elif(func == 2):
    total = valueOne * valueTwo
  elif(func == 3):
    total = valueOne / valueTwo
  else:
    total = math.pow(valueOne, valueTwo)
  
  print("O resultado é: ", total)

print()  # It will be used to print a blank line between de exercises.


# 19 - Escrever um programa em C que calcula a número de dias
# decorridos entre duas datas lidas: a data mais antiga e a data mais
# recente. Considerar a ocorrência de anos bissextos. Considerar o
# seguinte intervalo para o valor do ano fornecido: 1950-1996
# (1952 foi um ano bissexto).

dateArray = []

for date in range(1, 3):
  day = int(input(f"Digite o dia da {date}° data: "))
  month = int(input(f"Digite o mês da {date}° data: "))
  year = int(input(f"Digite o ano da {date}° data: "))
  result = datetime.date(year, month, day)
  dateArray.append(result)

if(dateArray[0] > dateArray[1]):
  differenceBetweenDates = dateArray[0] - dateArray[1]
else:
  differenceBetweenDates = dateArray[1] - dateArray[0]

print(f"A diferença de dias entre as datas é de: {differenceBetweenDates.days} dias")

print()  # It will be used to print a blank line between de exercises.

# 20 - Faça um programa que leia vários inteiros positivos e mostre
# no final, a soma dos números pares e a soma dos números ímpares.
# O programa para quando entrar um número maior do que 1000.

sumEven = 0
sumOdd = 0
number = 1

while(number < 1001):
  value = int(input("Por favor, digite um número qualquer: "))

  if(value % 2 == 0):
    sumEven += value
    
  else:
    sumOdd += value
  
  print(f"A soma dos número pares até o momento é de: {sumEven}")
  print(f"A soma dos número pares até o momento é de: {sumOdd}")
  number = int(input("Deseja continuar? Digite um número maior que 1000 para sair: "))

print()  # It will be used to print a blank line between de exercises.

# 21 - Faça um programa que leia vários conjuntos de três valores reais
# e mostre para cada conjunto: sua soma, seu produto e a sua média.
# O programa para quando um conjunto não entrar com seus valores em
# ordem crescente.

while True:
  valueOne = float(input("Digite o primeiro valor: "))
  valueTwo = float(input("Digite o segundo valor: "))
  valueThree = float(input("Digite o terceiro valor: "))

  if(valueOne < valueTwo and valueTwo < valueThree):
    sumValues = valueOne + valueTwo + valueThree
    timeValues = valueOne * valueTwo * valueThree
    averageValues = (valueOne + valueTwo + valueThree) / 3
    print("A soma dos valores é de: ", sumValues)
    print("O produto dos valores é de: ", timeValues)
    print("A média dos valores é de: ", averageValues)
  else:
    break

print()  # It will be used to print a blank line between de exercises.

# 22 - Faça um programa que leia as médias finais de vários alunos
# de uma turma e mostre a maior média, a menor média e a média
# aritimética da turma. O programa para quando encontrar uma média
# negativa.

maior = ''
menor = ''
total = 0
students = 0

while True:
  mark = float(input("Digite a média do aluno ou -1 para sair: "))
  
  if(mark < 0):
    break

  students += 1
  total += mark

  if(maior == ''):
    maior = mark
  elif(maior < mark):
    maior = mark
  
  if(menor == ''):
    menor = mark
  elif(menor > mark):
    menor = mark
  
print("A maior média encontrada foi: ", maior)
print("A menor média encontrada foi:", menor)

total = round(total / students, 2)
print("A média final da turma foi: ", total)

print()  # It will be used to print a blank line between de exercises.

# 23 - Faça um programa que leia um número n e mostre na tela os n
# primeiros números pares e depois os n primeiros número ímpares

numbers = int(input("Digite a quantidade de primeiros pares e ímpares que deseja ver: "))

arrayEven = []
arrayOdd = []
numberEven = 2
numberOdd = 1

for number in range(numbers):
  arrayEven.append(numberEven)
  numberEven += 2


for number in range(numbers):
  arrayOdd.append(numberOdd)
  numberOdd += 2

print(f"Esses são os {numbers} primeiros números pares: ", arrayEven)
print(f"Esses são os {numbers} primeiros números ímpares: ", arrayOdd)

print()  # It will be used to print a blank line between de exercises.

# 24 - Faça um programa que leia um número n e imprima se ele é
# primo ou não. (um número primo tem apenas 2 divisores: 1 e ele mesmo, 
# sendo que o próprio número 1 não é primo).

primes = [2, 3, 5, 7]
counter = 0

number = int(input("Digite o número para verificar se este é primo: "))

for n in range(len(primes)):
  if(number % primes[n] == 0):
    counter += 1

if(counter != 0):
  print("Este não é um número primo.")
else:
  print("Este é um número primo.")

print()  # It will be used to print a blank line between de exercises.

# 25 - Faça um programa que leia um número n e imprima na tela os
# n primeiros número primos.

numbers = int(input("Digite a quantidade de n primeiro primos para se visualizar: "))

def is_prime(n, div=2):

    if(n == 0 or n == 1):
      return False
    if(div > n / 2.0):
      return True

    if n % div == 0:
        return False
    else:
        div += 1
        return is_prime(n,div)

for i in range(numbers):
    if is_prime(i):
        print(i)

print()  # It will be used to print a blank line between de exercises.

# 26 - Faça um algoritimo que leia dois valores inteiros e informe:
# - A soma dos números pares desse intervalos de números, incluindo
#   os números digitados;
# - A multiplicação dos números ímpares desse intervalo de números,
#   incluindo os números digitados.

valueOne = int(input("Por favor, digite o primeiro número: "))
valueTwo = int(input("Por favor, digite o segundo número: "))

sumEven = 0
timesOdd = 1

for number in range(valueOne, valueTwo + 1):
  if(number % 2 == 0):
    sumEven += number
  else:
    timesOdd *= number

print("A soma dos números pares deste intervalo é: ", sumEven)
print("A multiplicação dos número ímpares desse intervalo é: ", timesOdd)

print()  # It will be used to print a blank line between de exercises.

# 27 - Faça um programa que solicita ao usuário o número de alunos de
# uma turma e o número de provas realizadas. A seguir o programa
# deve para cada aluno:
# - Solicitar o nome do aluno;
# - Para cada prova realizada solicita a nota deste aluno;
# - Exibir o nome e a média aritimética das notas deste aluno
#   após o término da digitação o programa deverá exibir o nome
#   do aluno com a maior média.

# Saídas:
# - Pedido para a quantidade de alunos = "Digite a quantidade de
#   alunos na sala."
# - Pedido para a quantidade de provas realizadas = "Digite a
#   quantidade de provas aplicadas."
# - Para cada aluno = "Digite o nome do aluno: "
# - Para cada prova do aluno = "Digite a nota da prova: "
# - Após cada pedido de nome e nota, será exibido o nome do aluno
#   e a média aritimética;
# - Ao fim será exibido = "Aluno com melhor média: ", seguido do
#   nome do aluno com melhor média.

students = int(input("Digite a quantidade de alunos na sala: "))
exams = int(input("Digite a quantidade de provas aplicadas: "))

higherMark = 0
studentHigherMarkName = ''

for student in range(students):
  studentName = str(input("Digite o nome do aluno: "))

  marks = 0

  for exam in range(exams):
    mark = float(input("Digite a nota da prova: "))
    marks += mark
  
  averageMark = marks / exams

  if(averageMark == ''):
    higherMark = averageMark
    studentHigherMarkName = studentName
  elif(averageMark > higherMark):
    higherMark = averageMark
    studentHigherMarkName = studentName

  print(f"{studentName} nota final: {round(averageMark, 2)}")

print(f"Aluno com melhor média: {studentName}")

print()  # It will be used to print a blank line between de exercises.

# 28 - Uma companhia de seguros possui um número indeterminado de
# corretores. A companhia paga o salário de cada corretor na forma
# de comissão, calculada de acordo com a venda mensal do corretor.
# Essa comissão é de 35% o valor da venda, se esse valor for maior
# que R$3.000,00; 20% do valor da venda, se esse valor estiver entre
# R$1.500,00 e R$3.000,00; e 13% do valor da venda, se este valor
# estiver abaixo de R$1.500,00. Construa um algoritimo que:
# - Mostre o salário (comissão) de cada corretor;
# - Calcule e mostre o total de vendas da companhia;
# - Calcule e mostre o total geral de salários (comissões) pagos
#   aos corretores.

number = 1
totalSales = 0
salary = 0

salariesArray = []

while(number != 0):
  sales = float(input("Digite as vendas do correto, usando ponto como separador: "))
  
  if(sales > 3000):
    salary = sales * 0.35
  elif(sales > 1499.99):
    salary = sales * 0.2
  else:
    salary = sales * 0.13
  
  print(f"O salário deste vendedor foi de R$: {round(salary, 2)}")
  salariesArray.append(salary)

  totalSales += sales
  number = float(input("Deseja sair? Caso sim, digite 0: "))

print("A lista de salários será exibida a seguir, separada por vírgulas", salariesArray)
print("A soma de salários pagos foi de: R$", round(sum(salariesArray), 2))
print("O total de vendas da empresa foi de: R$", round(totalSales, 2))


print()  # It will be used to print a blank line between de exercises.

# 29 - Uma empresa contratou-o para desenvolver um software para
# realizar a seleção de pessoal para seu quadro de funcionários.
# O software deve solicitar os seguintes dados dos candidatos:
# - Número de inscrição;
# - Idade;
# - Sexo (M ou F);
# - Possui experiência anterior (S ou N)

# A entrada dos dados deve ser encerrada quando o número de
# inscrição for igual a -1. Não é necessário fazer a consistência
# de nenhuma das informações digitadas. A empresa solicitou que as
# seguintes informações fossem exibidas na tela após a entrada dos
# dados:
# - Quantidade de candidatos inscritos;
# - Idade média dos candidatos;
# - Porcentagem dos homens com mais de 45 anos;
# - Quantidade de mulheres com idade inferior a 35 anos e com
#   experiência anterior;
# - Entre as mulheres que já tem experiência anterior, a que
#   possui a menor idade.

class Candidates:
  def __init__(self, doc, age, gender, experience):
    self.doc = doc
    self.age = age
    self.gender = gender
    self.experience = experience

listOfCandidates = list()

while True:
  doc = int(input("Digite o n° da inscrição: "))

  if(doc == -1):
    break

  age = int(input("Digite a idade: "))
  gender = str(input("Digite o sexo (M / F): "))
  experience = str(input("Possui experiência anterior (S / N): "))

  candidate = Candidates(doc, age, gender, experience)
  listOfCandidates.append(candidate)


print(f"O número de candidatos inscritos foi: {len(listOfCandidates)}")

sumAges = 0

highAgedMen = 0
lowAgedMen = 0

lowAgedWomenExperienced = 0

lowerAgedWoman = 0
lowerAgedWomanDoc = 0

for candidate in listOfCandidates:
  sumAges += candidate.age

  if(candidate.gender == 'M' and candidate.age > 45):
    highAgedMen += 1
  if(candidate.gender == 'M' and candidate.age <= 45):
    lowAgedMen += 1

  if(candidate.gender == 'F' and candidate.age < 35 and candidate.experience == 'S'):
    lowAgedWomenExperienced += 1

  if(lowerAgedWoman == 0 and candidate.gender == 'F' and candidate.experience == 'S'):
    lowerAgedWoman = candidate.age
    lowerAgedWomanDoc = candidate.doc
  
  if(lowerAgedWoman > candidate.age and candidate.gender == 'F' and candidate.experience == 'S'):
    lowerAgedWoman = candidate.age
    lowerAgedWomanDoc = candidate.doc


averageAge = sumAges / len(listOfCandidates)

print(f"A idade média dos inscritos é de: {round(averageAge, 2)}")

percentageHighAgedMen = (highAgedMen / (highAgedMen + lowAgedMen)) * 100
print(f"O percentual de homens acima dos 45 anos é de: {round(percentageHighAgedMen, 2)} porcento")

print("A quantidade de mulheres abaixo de 35 anos e com experiência é de: ", lowAgedWomenExperienced)

print(f"A candidata com menor idade e experiência possui {lowerAgedWoman} anos e é portador do doc n°{lowerAgedWomanDoc}")

print()  # It will be used to print a blank line between de exercises.

# 30 - Elabore um algoritimo para fazer a leitura de N notas de M
# alunos de uma turma. Os valores N e M devem ser solicitados ao
# usuário no início do algoritimo. Exibir:

# - A média de cada aluno;
# - A média geral;
# - A maior e a menor média

students = int(input("Digite a quantidade de alunos na sala: "))
exams = int(input("Digite a quantidade de provas aplicadas: "))

higherMark = ''
studentHigherMarkName = ''

lowerMark = ''
studentLowerMarkName = ''

sumStudentsMarks = 0
allMarksArray = []

for student in range(students):
  studentName = str(input("Digite o nome do aluno: "))

  marks = 0

  for exam in range(exams):
    mark = float(input("Digite a nota da prova: "))
    marks += mark
  
  averageMark = marks / exams

  if(higherMark == ''):
    higherMark = averageMark
    studentHigherMarkName = studentName
  elif(averageMark > higherMark):
    higherMark = averageMark
    studentHigherMarkName = studentName
  
  if(lowerMark == ''):
    lowerMark = averageMark
    studentLowerMarkName = studentName
  elif(averageMark < lowerMark):
    lowerMark = averageMark
    studentLowerMarkName = studentName

  print(f"{studentName} nota final: {round(averageMark, 2)}")
  allMarksArray.append(averageMark)
  sumStudentsMarks += averageMark

print("A seguir, a lista com a média de todos os alunos: ", allMarksArray)

print(f"Aluno com melhor média foi: {studentHigherMarkName}, {higherMark}")
print(f"Aluno com pior média foi: {studentLowerMarkName}, {lowerMark}")

averageStudentsMarks = sumStudentsMarks / students

print(f"A média final da turma foi: {round(averageStudentsMarks, 2)}")

print()  # It will be used to print a blank line between de exercises.