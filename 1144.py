__author__ = 'joaquim'
"""
 URI Online Judge | 1143
Quadrado e ao Cubo

Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1

Escreva um programa que leia um valor inteiro N (1 < N < 1000). Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.
Entrada

O arquivo de entrada contém um número inteiro positivo N.
Saída

Imprima a saída conforme o exemplo fornecido.
Exemplo de Entrada 	Exemplo de Saída

5
                            1 1 1
                            2 4 8
                            3 9 27
                            4 16 64
                            5 25 125
"""

num = int(input())

cont = 1
contN = 1
contN2 = 1
contN3 = 1
contSoma = 1

for i in range(num):
    if cont == 1:
        contN2 = contN * contN
        contN3 = contN * contN2

        contSoma = 1
        print(contN, contN2, contN3)
        
    if contSoma == 1:
        contN2 += 1
        contN3 += 1

        print(contN, contN2, contN3)

    contN += 1
