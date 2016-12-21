__author__ = 'Joaquim Alves'
"""
Leia um valor inteiro N. Apresente todos os números entre 1 e 10000 que divididos por N dão resto igual a 2.
Entrada: A entrada contém um valor inteiro N (N < 10000).
Saída: Imprima todos valores que quando divididos por N dão resto = 2, um por linha.

Exemplo de Entrada	Exemplo de Saída
13
2
15
28
41
...
"""

N = int(input())
for i in range(1,10000):
    if(i % N == 2):
        print(i)