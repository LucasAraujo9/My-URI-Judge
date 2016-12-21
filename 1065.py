__author__ = 'Joaquim Alves'
"""
Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

Entrada: O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída: Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.

Exemplo de Entrada	Exemplo de Saída
7
-5
6
-4
12
3 valores pares
"""
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

cont = 0
media = 0
if(n1 % 2 == 0):
    cont += 1
if(n2 % 2 == 0):
    cont += 1
if(n3 % 2 == 0):
    cont += 1
if(n4 % 2 == 0):
    cont += 1
if(n5 % 2 == 0):
    cont += 1
print("%d valores pares"%cont)