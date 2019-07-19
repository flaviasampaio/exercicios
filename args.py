#         Exercício 1 

# nome_funcionario = input('Digite seu nome")
# horas_trabalhadas = int(input('Digite o numeto de horas trabalhadas: '))
# valor_hora = float(input("Digite o valor que recebe por hora: '))
# calcular_salario = (horas_trabalhadas * valor_hora) *31

# print (f'{nome_funcionario} seu salário é de: {calcular salário}')

# -------------------------------------------------------------------------------------------------

#                         Exercício 2 

# import random 

# contador = 0 
# aleatorio = []

# while contador < 20:
#         aleatorio.append(random.randrange(0,20))
#         contador +=1

# maior = max(aleatorio)

# print(aleatorio)
# print(f'O maior número da lista é: {maior}')

# -----------------------------------------------------------------------------------------------------------

import random

# contador = 0
# aleatorio = []
# pares = []
# impares = []

# while contador <10:
#         aleatorio.append(random.randrange(0,20))
#         contador +=1

# for i in aleatorio:
#         if i%2 == 0:
#                 pares.append(i)
#         else:
#                 impares.append(i)

# print(f'Essa é sua lista: {aleatorio}')
# print(f'impares = {impares}')
# print(f'pares = {pares}')

#----------------------------------------------- exercicio 4

# a = int(input('Valor de a: ')) #solicitando valores
# b = int(input('Valor de b: '))
# c = int(input('Valor de c: '))

# def bhaskara(a, b, c):
#         delta = (b*b) - (4*(a*c))
#         bask = ((-b) + ((delta)**(1/2)) / (2*a)) 
#         bask2 = ((-b) - ((delta)**(1/2)) / (2*a)) 
#         print('Bhaskara positivo ++ : ',bask)
#         print('Bhaskara negativo -- : ',bask2)

# bhaskara(a,b,c)

#---------------------------------------------- exercicio 5

#raio = int(input('Qual o raio do circulo: '))
# meu_nome = input('seu nome parceiro: ')
# def hello(meu_nome):
#    print('Olá',meu_nome)

# def calculo (raio):
#         area = (raio**2) * 3.14
#         return area

# raio_circulo = float(input('Digite o raio do círculo: '))

# pi = 3.14 

# def calcula_area(raio_circulo, pi):
#         area = (pi * (raio_circulo ** 2))
#         print('Area do circulo é: {}m²' .format(area))

# calcula_area(raio_circulo, pi)

# def calcula_comprimento(raio_circulo, pi):
#         comprimento = (2*pi * raio_circulo)
#         print('Comprimento do círculo é {}m' .format(comprimento))

# calcula_comprimento(raio_circulo, pi)