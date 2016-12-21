__author__ = 'Joaquim Alves'
"""
Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a média semestral.
Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve
ser validada separadamente.

Entrada: A entrada contém vários valores reais, positivos ou negativos. O programa deve ser encerrado quando
forem lidas duas notas válidas.

Saída: Se uma nota inválida  for lida, deve ser impressa a mensagem "nota invalida".
Quando duas notas válidas forem lidas, deve ser impressa a mensagem "media = " seguido do valor do cálculo.
O valor deve ser apresentado com duas casas após o ponto decimal.

Exemplo de Entrada	Exemplo de Saída
-3.5
3.5
11.0
10.0
nota invalida
nota invalida
media = 6.75
"""
cont = 2
listaNotas = []

while cont > 0:
    nota = float(input())
    if nota >= 0 and nota <= 10:
        cont -= 1
    listaNotas.append(nota)

N1 = 0
N2 = 0
media = 0

for i in range(len(listaNotas)):
    if (listaNotas[i] > 10):
        print("nota invalida")
    if (listaNotas[i] < 0):
        print("nota invalida")
    if listaNotas[i] >= 0 and listaNotas[i] <= 10:
        media += listaNotas[i]

media = media/2
print("media = %.2f"%media)
