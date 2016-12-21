__author__ = 'Joaquim Alves'
"""
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada: Não há nenhuma entrada neste problema.

Saída: Imprima a sequencia conforme exemplo abaixo.

Exemplo de Entrada	Exemplo de Saída
I=0 J=1
I=0 J=2
I=0 J=3
I=0.2 J=1.2
I=0.2 J=2.2
I=0.2 J=3.2
.....
I=2 J=?
I=2 J=?
I=2 J=?
"""
I = 0
J = 1
contJ = 1

while(I <= 2):
    if(contJ <= 3):
        if(I == 0):
            print("I=%d J=%d"%(I,J))
            contJ += 1
            J += 1
        elif(I == 1):
            print("I=1 J=%d"%(J+I))
            contJ += 1
            J += 1
        elif(I < 2):
            if(I < 1.8):
                print("I=%.1f J=%.1f"%(I,J+I))
                contJ += 1
                J += 1
            else:
                print("I=2 J=%d"%(J+I))
                contJ += 1
                J += 1
    else:
        J = 1
        contJ = 1
        I += 0.2
