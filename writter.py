import math

# 19 - Escreva uma função que recebe como entrada um número n e 
# imprime todas as potências de 2 menores ou iguais a n

value = int(input("Digite um número inteiro qualquer: "))

def powerOfTwoLowerThan(value):
  for number in range(value + 1):
    powerOfTwo = math.pow(number, 2)
    print(powerOfTwo)


powerOfTwoLowerThan(value)

print()  # It will be used to print a blank line between de exercises.