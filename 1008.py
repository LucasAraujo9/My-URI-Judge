__author__ = 'Joaquim Alves'
"""Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por
hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

Entrada

O arquivo de entrada contém 2 números inteiros e 1 número com duas casas decimais, representando o número, quantidade
de horas trabalhadas e o valor que o funcionário recebe por hora trabalhada, respectivamente.

Saída

Imprima o número e o salário do funcionário, conforme exemplo fornecido, com um espaço em branco antes e depois da
igualdade. No caso do salário, também deve haver um espaço em branco após o $."""

""" #Forma Correta com descrição das Entradas!
numeroF = int(input("Entre com o Numero do Funcionario: "))
numeroH = int(input("Horas Trabalhadas: "))
valorH = float(input("Valor da Hora de Trabalhada: "))
print("NUMBER =",numeroF)
print("SALARY = U$ %.2f"%(numeroH * valorH))
"""

#Forma Aceita pelo URI
numeroF = int(input(""))
numeroH = int(input(""))
valorH = float(input(""))


print("NUMBER =",numeroF)
print("SALARY = U$ %.2f"%(numeroH * valorH))
