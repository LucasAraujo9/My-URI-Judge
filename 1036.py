__author__ = 'Joaquim Alves'
"""
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não foi possível calcular as
raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada: Leia três valores de ponto flutuante (double) A, B and C.

Saída: Se não houver possibildade de calcular as raízes, apresente a mensagem "Impossivel calcular". Caso contrário,
imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo.
Imprima sempre o final de linha após cada mensagem.

Exemplos de Entrada	Exemplos de Saída
10.0 20.1 5.1       R1 = -0.29788   R2 = -1.71212

0.0 20.0 5.0        Impossivel calcular

10.3 203.0 5.0     R1 = -0.02466   R2 = -19.68408

10.0 3.0 5.0 Impossivel calcular
"""
import math

A, B, C = [float(i) for i in input().split(" ")]

delta = ((B*B) - (4 * A * C))

if(delta > 0 and (A and B and C) > 0):
    R1 = ((-B) + math.sqrt(delta))/(2 * A)
    R2 = ((-B) - math.sqrt(delta))/(2 * A)
    print("R1 = %.5f"%R1)
    print("R2 = %.5f"%R2)
else:
    print("Impossivel calcular")

