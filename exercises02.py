import math

#  # Introdução a Programação Estruturada (Python)
#  
#  # Prof. M.Sc. Jorge Sandoval - Agosto 2020
#  
#  # Lista de exercicíos 02 #
#  
# 1 - Faça um algorítimo que leia os valores A, B, C e imprima na tela se a soma
# de A + B é menor que C.

print("Exercício 01:")
print()

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

sum = a + b

if(sum > c):
  print("A soma de A + B é maior do que C")
elif(sum == c):
  print("A soma de A + B é igual ao valor de C")
else:
  print("A soma de A + B é menor do que C")

print()  # It will be used to print a blank line between de exercises.

# 2 - Faça um algoritimo que leia o nome, o sexo e o estado civil de uma pessoa.
# Caso sexo seja "F" e estado civil seja "CASADA", solicitar o tempo de casada
# em anos.

print("Exercício 02:")
print()

name = input("Digite seu nome: ")
gender = input("Digite seu sexo (M/F): ")
relationship = input("Digite seu estado civil (SOLTEIRO(A)/CASADO(A)/VIUVO(A)/DIVORCIADO(A)): ").upper()
marriedTime = 0

if(gender == 'F' and relationship == 'CASADA'):
  marriedTime = int(input("Por favor, digite o tempo de casamento (em anos): "))

if(marriedTime != 0):
  print("Você é %s, do sexo %s, %s a %d anos" % (name, gender, relationship, marriedTime))
else:
  print("Você é %s, do sexo %s, %s" % (name, gender, relationship))

print()  # It will be used to print a blank line between de exercises.

# 3 - Faça um algorítimo para receber um número qualquer e informar na tela se é par
# ou impar.

print("Exercício 03:")
print()

number = int(input("Digite um número qualquer: "))

if(number == 0):
  print("Este é um número neutro")
elif(number % 2 > 0):
  print("Este é um número ímpar")
else:
  print("Este é um número par")

print()  # It will be used to print a blank line between de exercises.

# 4 -Faça um algoritimo que leia dois valores inteiros A e B. Se os valores forem
# iguais, deve-se realizar a soma entre eles, caso contrário, multiplica-se A por B
# Ao final, qualquer um dos resultados deve ser atribuído a uma variável C e mostrar
# seu resultado na tela.

print("Exercício 04:")
print()

a = int(input("Digite um valor para A: "))
b = int(input("Digite um valor para B: "))
c = 0

if(a == b):
  c = a + b
  print("A e B eram iguais. Assim, a soma de ambos é: ", c)
else:
  c = a * b
  print("A e B eram diferentes. Assim, a multiplicação de ambos é: ", c)

print()  # It will be used to print a blank line between de exercises.

# 5 - Encontrar o dobro de um número caso ele seja positivo e o seu triplo
# caso ele seja negativo, imprimindo seu resultado.

print("Exercício 05:")
print()

num = int(input("Digite um númer qualquer, negativo ou positivo: "))

if(num == 0):
  print("Você digitou %d e este número é neutro" % num)
elif(num > 0):
  num = num * 2
  print("Você digitou um número positivo. Logo, seu dobro é: %d" % num)
else:
  num = num * 3
  print("Você digitou um número negativo. Logo, seu triplo é: %d" % num)

print()  # It will be used to print a blank line between de exercises.

# 6 - Escreva um algoritimo que leia dois valores booleanos (lógicos) e
# então determine se ambos são VERDADEIROS ou falsos

print("Exercício 06:")
print()

firstValue = input("Por favor, digite algo ou aperte enter: ")
secondValue = input("Por favor, digite algo ou aperte enter novamente: ")


if(bool(firstValue) == True and bool(secondValue) == True):
  print("Você digitou algo em ambos os campos anteriores")
  print("Logo, ambos são VERDADEIROS")
elif(bool(firstValue) == True or bool(secondValue) == True):
  print("Você digitou algo em ao menos um campo anterior")
  print("Logo, ao menos um é VERDADEIRO")
else:
  print("Você não digito nada em ambos os campos anteriores")
  print("Logo, ambos são FALSOS")

print()  # It will be used to print a blank line between de exercises.

# 7 - Faça um algoritimo que leia uma variável e some 5 caso seja par
# ou some 8, caso seja ímpar. Imprimir o resultado desta operação.

print("Exercício 07:")
print()

number = int(input("Digite um número: "))

if(number == 0):
  print("Você digitou um número neutro")
elif(number % 2 > 0):
  number = number + 8
  print("Você digitou um número ímpar. Logo, somamos 8 ao número que você digitou.")
  print("O resultado foi: %d" % number)
else:
  number = number + 5
  print("Você digitou um número par. Logo, somamos 5 ao número que você digitou.")
  print(f"O resultado foi: {number}")

print()  # It will be used to print a blank line between de exercises.

# 8 - Escreva um algoritimo que leia três valores inteiros e diferentes e
# mostre-os em ordem decrescente.

print("Exercício 08:")
print()

a = int(input("Digite um valor para A: "))
b = int(input("Digite um valor para B, diferente de A: "))

while(b == a):
  print("Por favor, digite um valor diferente para B")
  b = int(input("Digite novamente um valor para B: "))

c = int(input("Digite um valor para C, diferente de A e B: "))

while(c == a or c == b):
  print("Por favor, digite um valor diferente para C")
  c = int(input("Digite novamente um va lor para C: "))

if(a > b and a > c):
  if(b > c):
    print("Seguem os valores em ordem decrescente: A = %d, B = %d, C = %d" % (a, b, c))
  else:
    print("Seguem os valores em ordem decrescente: A = %d, C = %d, B = %d" % (a, c, b))
elif(b > c):
  if(a > c):
    print("Seguem os valores em ordem decrescente: B = %d, A = %d, C = %d" % (b, a, c))
  else:
    print("Seguem os valores em ordem decrescente: B = %d, C = %d, A = %d" % (b, c, a))
else:
  if(a > b):
    print("Seguem os valores em ordem decrescente: C = %d, A = %d, B = %d" % (c, a, b))
  else:
    print("Seguem os valores em ordem decrescente: C = %d, B = %d, A = %d" % (c, b, a))

print()  # It will be used to print a blank line between de exercises.

# 9 - Construa um algoritimo que, dado quatro valores A, B, C e D, imprima em tela
# o maior e o menor

print("Exercício 09:")
print()

a = int(input("Digite um valor para A: "))
b = int(input("Digite um valor para B: "))
c = int(input("Digite um valor para C: "))
d = int(input("Digite um valor para D: "))

maior = a
menor = a

numbers = [a, b, c, d]

for number in numbers:
  if(number > maior):
    maior = number
  if(number < menor):
    menor = number

print(f"O maior número que você digitou foi: {maior}")
print(f"O menor número que você digitou foi: {menor}")

print()  # It will be used to print a blank line between de exercises.

# 10 - Tendo como dados de entrada a altura e o sexo de uma pessoa
# construa um algoritimo que calcule seu peso ideal, utilizando as
# seguintes fórmulas:
# * Para homens (72.7 * h) - 58. 
# * Para mulheres (62.1 * h) - 44.7 

print("Exercício 10:")
print()

height = float(input("Por favor, digite a sua altura, utilizando ponto como separador: ")) 
gender = input("Por favor, digite seu sexo (M/F): ") 

if(gender == 'F'): 
  idealWeight = (62.1 * height) - 44.7 
  print(f"O peso ideal para o seu sexo é: {idealWeight}") 
else: 
  idealWeight = (72.7 * height) - 58
  print(f"O peso ideal para o seu sexo é: {idealWeight}")
   
print()  # It will be used to print a blank line between de exercises. 

# 11 - O IMC - Indice de Massa Corporal é um critério da Organização Mundial da Saúde 
# para dar uma indicação sobre a condição de peso de uma pessoa adulta. A fórmula é 
# IMC = peso / (altura)²

print("Exercício 11: Este exercício não pediu nenhum output. Apenas foi criada a fórmula do imc")
print() 

def imcFormula(weight, height):
  imc = round(weight / (height * height), 2)
  if(imc > 30):
    print("Obeso")
  elif(imc > 25):
    print("Acima do peso")
  elif(imc > 18.5):
    print("Peso normal")
  else:
    print("Abaixo do peso")
  print(f"Seu IMC é de: {imc}")    


print()  # It will be used to print a blank line between de exercises. 

# 12 - Elabore um algoritimo que leia o peso e a altura de um adulto e mostre sua
# condição de acordo com a tabela abaixo. # # IMC em adultos, Condição:
# - Abaixo de 18.5: Abaixo do peso; # # - Entre 18.5 e 25: Peso normal;
# - Entre 25 e 30: Acima do peso; # # - Acima de 30: Obeso.

print("Exercício 12:")
print()

height = float(input("Digite sua altura, utilizando ponto como separador: "))
weight = float(input("Digite o seu peso, utilizando ponto como separador: "))


imcFormula(weight, height)

print()  # It will be used to print a blank line between de exercises.
 
# 13 - Elabore um algoritimo que calcule o que deve ser pago por um produto,
# considerando o preço normal de etiqueta e a escolha da condição de pagamento
# Utilize os códigos da tabela a seguir para ler qual a condição de pagamento
# escolhida e efetuar o pagamento adequado.
# Condições de pagamento:
# - À vista em dinheiro ou cheque, recebe 10% de desconto;
# - À vista no cartão de crédito, recebe 15% de desconto;
# - Em duas vezes, preço normal de etiqueta, sem juros;
# - Em mais de deuas vezes, preço normal de etiqueta, mais juros de 10%; 

print("Exercício 13:")
print()

product = input("Digite o nome do produto adquirido: ")
print()

price = float(input("Digite o valor do produto adquirido, utilizando ponto como separador: "))
print()

print("Por favor, escolha uma das condições de pagamento abaixo, digitando o seu número: ")
paymentCondition = int(input("1 - À vista em dinheiro ou cheque | 2 - À vista no cartão de crédito | 3 - Em duas vezes | 4 - Acima de duas vezes: "))

if(paymentCondition == 1):
  price = price - (price * 0.1)
  print("você comprou o produto %s e ganhou 10 porcento de desconto. Valor final %.2f" % (product, price))
elif(paymentCondition == 2):
  price = price - (price * 0.15)
  print("você comprou o produto %s e ganhou 15 porcento de desconto. Valor final %.2f" % (product, price))
elif(paymentCondition == 3):
  print("Você comprou o produto %s. O preço final é: %.2f" % (product, price))
else:
  price = price + (price * 1.1)
  print("Você comprou o produto %s. Devido ao parcelamento maior que 2x o preço final é: %.2f" % (product, price))

print()  # It will be used to print a blank line between de exercises.

# 14 - Escreva um algoritimo que leia o número de identificação, as 3 notas obtidas
# por um aluno nas 3 verificações e média dos exercícios que fazem
# parte da avaliação, e calcule a média de aproveitamento, usando a fórmula:
# - MA = (nota1 + nota2 * 2 + nota3 * 3 + ME) / 7

print("Exercício 14:")
print()

def markCalc(mark1, mark2, mark3, markExercises):
  finalMark = round((mark1 + (mark2 * 2) + (mark3 * 3) + markExercises) / 7, 2)
  print(f"A sua média final é: {finalMark}")

mark1 = float(input("Por favor, digite a primeira nota: "))
mark2 = float(input("Por favor, digite a segunda nota: "))
mark3 = float(input("Por favor, digite a terceira nota: "))
markExercises = float(input("Por favor, digite a nota dos exercícios: "))

markCalc(mark1, mark2, mark3, markExercises)

print()  # It will be used to print a blank line between de exercises.

# 15 - A atribuição dos conceitos obedece a tabela abaixo. O Algoritimo deve
# escrever o número do aluno, suas notas, a média dos exercícios, a média
# de aproveitamento, o conceito correspondente e a mensagem 'Aprovado'
# se o conceito for A, B ou C e 'Reprovado' se o conceito for D ou E.
# Média de aproveitamento Conceito:
# - >= 90: A
# - >= 75 e < 90: B
# - >= 60 e < 75: C
# - >= 40 e < 60: D
# - < 40: E

print("Exercício 15:")
print()

def markCalc(studentId, mark1, mark2, mark3, markExercises):
  finalMark = round(((mark1 + (mark2 * 2) + (mark3 * 3) + markExercises) / 7) * 10, 2)
  print(f"Estudante n° {studentId} a sua média final é: {finalMark}")
  if(finalMark >= 90):
    print("Com isso, seu conceito foi A e você está APROVADO")
  elif(finalMark >= 75):
    print("Com isso, seu conceito foi B e você está APROVADO")
  elif(finalMark >= 60):
    print("Com isso, seu conceito foi C e você está APROVADO")
  elif(finalMark >= 40):
    print("Com isso, seu conceito foi D e você está REPROVADO")
  else:
    print("Com isso, seu conceito foi E e você está REPROVADO")

studentId = input("Por favor, digite o número da sua matrícula: ")
mark1 = float(input("Por favor, digite a primeira nota: "))
mark2 = float(input("Por favor, digite a segunda nota: "))
mark3 = float(input("Por favor, digite a terceira nota: "))
markExercises = float(input("Por favor, digite a nota dos exercícios: "))

markCalc(studentId, mark1, mark2, mark3, markExercises)

print()  # It will be used to print a blank line between de exercises.

# 16 - Dados três valores X, Y, Z, verificar se eles podem ser os comprimentos
# dos lados de um triângulo, e se forem, verificar se é um triângulo equilátero
# isóceles ou escaleno. Se eles não formarem um triângulo, escrever uma mensagem
# Antes da elaboração do algoritimo, torna-se necessária a revisão de algumas
# propriedades e definições.
# Propriedade - O comprimento de cada lado de um triangulo é menor do
# que a soma dos comprimentos dos outros dois lados.
# Definição 1 - Chama-se triangulo equilátero aqueles que têm os comprimentos
# dos tres lados iguais,
# Definição 2 - Chamam-se triangulos isósceles os que têm os comprimentos
# de dois lados iguais.
# Definição 3 - Chama-se triangulo escaleno aqueles que têm os comprimentos
# dos três lados diferentes

valueX = int(input("Digite o primeiro valor do Triângulo: "))
valueY = int(input("Digite o segundo valor do Triângulo: "))
valueZ = int(input("Digite o terceiro valor do Triângulo: "))

firstValidator = valueX - valueZ
secondValidator = valueX + valueZ

thirdValidator = valueY - valueZ
fourthValidator = valueY + valueZ

fifthValidator = valueY - valueX
sixthValidator = valueY + valueX

if(valueX > thirdValidator and valueX < fourthValidator):
  if(valueY > firstValidator and valueY < secondValidator):
    if(valueZ > fifthValidator and valueZ < sixthValidator):
      if((valueX + valueY + valueZ) / 3 == valueX):
        print("Este é um triângulo equilátero")
      elif((valueX + valueY) /2 == valueX or (valueX + valueZ) / 2 == valueX or (valueZ + valueY) / 2 == valueZ):
        print("Este é um triângulo isósceles")
      else:
        print("Este é um triângulo escaleno")
    else:
      print("Infelizmente, não é possível realizar um triângulo com os números fornecidos.")
  else:
    print("Infelizmente, não é possível realizar um triângulo com os números fornecidos.")

print()  # It will be used to print a blank line between de exercises.

# 17 - Um hotel cobra R$ 300,00 por diária e mais uma taxa adicional de serviços.
# Se a diária for menor que 15, a taxa é de R$ 20,00. Se o número de diárias
# for igual a 15, a taxa é de R$ 14,00 e se o número for maior que 15 a taxa
# é de R$ 12,00. Considerando-se que para cada pessoa tenha-se um registro contendo
# seu nome e o número de diárias. Faça um algoritimo que imprima na tela o nome e o
# total a pagar do Hóspede.

print("Exercício 17:")
print()

daily = 300
customer = input("Digite o seu nome: ")
spentDaily = int(input("Digite o número de diárias utilizadas: "))

if(spentDaily > 15):
  total = round(float((daily * spentDaily) + 12), 2)
  print(f"Senhor(a) {customer} o total a ser pago é de R$ {total}")
elif(spentDaily == 15):
  total = round(float((daily * spentDaily) + 14), 2)
  print(f"Senhor(a) {customer} o total a ser pago é de R$ {total}")
else:
  total = round(float((daily * spentDaily) + 20), 2)
  print(f"Senhor(a) {customer} o total a ser pago é de R$ {total}")

print()  # It will be used to print a blank line between de exercises.

# 18 - A prefeitura de São José da Serra abriu uma linha de crédito para os
# funcionários estatutários. O valor máximo da prestação não poderá ultrapassar
# 30% do salário bruto. Fazer um algoritimo que permita entrar com o salário e o
# valor da prestação e informar se o empréstimo pode ou não ser concedido.

print("Exercício 18:")
print()

salary = float(input("Digite o valor do seu salário bruto, utilizando o ponto com separador: "))
loanAmount = float(input("Digite o valor do empréstimo: "))
loanInstallments = int(input("Digite o número de parcelas, não podendo ultrapassar 100 parcelas: "))

while(loanInstallments >= 100):
  print("Por favor, digite um número menor do que 100 parcelas")
  loanInstallments = int(input("Digite o número de parcelas, não podendo ultrapassar 100 parcelas: "))

loanInstallmentsValue = loanAmount / loanInstallments
maximumLoanInstallmentsValue = salary * 0.3

if(loanInstallmentsValue > maximumLoanInstallmentsValue):
  print("Lamentamos, o seu empréstimo não pode ser concedido pois o valor da parcela é maior que 30 porcento de seu salário bruto. Tente um valor menor.")
else:
  print(f"Empréstimo concedido. Seu novo saldo é de {loanAmount}, que deverá ser pago em {loanInstallments} parcelas de R$ {loanInstallmentsValue}")

print()  # It will be used to print a blank line between de exercises.

# 19 - Construir um algoritimo para calcular as raízes de uma equação do 2° grau
# sendo que os valores dos coeficientes A, B e C devem ser fornecidos pelo usuário
# através do teclado.

print("Exercício 19:")
print()

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

delta = (b * b) - 4 * a * c

if(delta <= 0):
  print("Esta operação não possuí raiz de delta positiva.")
else:
  x1 = (-b + math.sqrt(delta)) / (2 * a)
  x2 = (-b - math.sqrt(delta)) / (2 * a)
  print(f"O valor de x' é {x1} e o de x'' é {x2}")

print()  # It will be used to print a blank line between de exercises.
 
# 20 - Criar um algoritimo que leia um número inteiro entre 1 e 7 e escreva o dia
# da semana correspondente. Caso o usuário digite um número fora desse intervalo,
# deverá aparecer uma mensagem informando que não existe dia da semana com esse número

print("Exercício 20:")
print()

weekDay = int(input("Digite um dia da semana entre 1 e 7: "))
week = ['Domingo', 'Segunda-Feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado']

if(weekDay > 7 or weekDay < 1):
  print("Não existe dia da semana para este número.")
else:
  print(week[weekDay - 1])
