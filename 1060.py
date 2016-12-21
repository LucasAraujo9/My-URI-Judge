__author__ = 'Joaquim Alves'
"""
Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos).
A seguir, mostre a quantidade de valores positivos digitados.

Entrada: Seis valores, negativos e/ou positivos.

Saída: Imprima uma mensagem dizendo quantos valores positivos foram lidos.

Exemplo de Entrada	Exemplo de Saída
7
-5
6
-3.4
4.6
12                  4 valores positivos
"""

n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())

cont = 0
if(n1 > 0):
    cont += 1
if(n2 > 0):
    cont += 1
if(n3 > 0):
    cont += 1
if(n4 > 0):
    cont += 1
if(n5 > 0):
    cont += 1
if(n6 > 0):
    cont += 1
print("%d valores positivos"%cont)