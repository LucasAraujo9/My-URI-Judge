__author__ = 'Joaquim Alves'
"""
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.

Entrada:O arquivo de entrada contém três valores com um dígito após o ponto decimal.

Saída: O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima,
sempre com mensagem correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser
apresentado com 3 dígitos após o ponto decimal.

Exemplos de Entrada	Exemplos de Saída
3.0 4.0 5.2
TRIANGULO: 7.800
CIRCULO: 84.949
TRAPEZIO: 18.200
QUADRADO: 16.000
RETANGULO: 12.000
12.7 10.4 15.2
TRIANGULO: 96.520
CIRCULO: 725.833
TRAPEZIO: 175.560
QUADRADO: 108.160
RETANGULO: 132.080
"""
"""A = float(input())
B = float(input())
C = float(input())"""

A, B, C = [float(i) for i in input().split(" ")] #split ele separa as strings de acordo com o que você determinar, no meu caso foi pelo espaço em branco

areaT = (C * A)/2
areaC = ((C*C) * 3.14159)
areaTra = ((A + B) * C) / 2
areaQ = B * B
areaR = A * B

print("TRIANGULO: %.3f"%(areaT))
print("CIRCULO: %.3f"%(areaC))
print("TRAPEZIO: %.3f"%(areaTra))
print("QUADRADO: %.3f"%(areaQ))
print("RETANGULO: %.3f"%(areaR))
#Programa está certo mas o URI qer todas as entradas na mesma Linha -.-
"""Lista = input()

if(len(Lista) <= 5):
    A = float(Lista[0])
    B = float(Lista[2])
    C = float(Lista[4])
elif(len(Lista) <= 11 ):
    A = float(Lista[0] + Lista[1] + Lista[2])
    B = float(Lista[4] + Lista[5] + Lista[6])
    C = float(Lista[8] + Lista[9] + Lista[10])
elif(len(Lista) >= 12):
    A = float(Lista[0] + Lista[1] + Lista[2] + Lista[3])
    B = float(Lista[5] + Lista[6] + Lista[7] + Lista[8])
    C = float(Lista[10] + Lista[11] + Lista[12] + Lista[13])
"""
