__author__ = 'Joaquim Alves'
"""
Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A e a soma de C com D for
maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos",
senão escrever "Valores nao aceitos".

Entrada: Quatro números inteiros A, B, C e D.

Saída: Mostre a respectiva mensagem após a validação dos valores.

Exemplo de Entrada	Exemplo de Saída
5 6 7 8                 Valores nao aceitos
2 3 2 6                 Valores aceitos
"""
A, B, C, D = [int(i) for i in input().split(" ")]

if(B > C):
    if(D > A):
        if((C + D) > (A + B)):
            if((C and D) > 0):
                if(A % 2 == 0):
                    print("Valores aceitos")
                else:
                    print("Valores nao aceitos")
            else:
                print("Valores nao aceitos")
        else:
            print("Valores nao aceitos")
    else:
        print("Valores nao aceitos")
else:
    print("Valores nao aceitos")