__author__ = 'Joaquim Alves'
"""
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente,
uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada: A entrada contem três números inteiros.

Saída: Imprima a saída conforme foi especificado.
Exemplo de Entrada	Exemplo de Saída
7 21 -14               -14
                         7
                        21

                         7
                         21
                        -14

-14 21 7                -14
                          7
                         21

                        -14
                         21
                          7
"""
n1, n2, n3 = [int(i) for i in input().split(" ")]
valorLido1 = n1
valorLido2 = n2
valorLido3 = n3

lista = [n1,n2,n3]
lista.sort()

n1,n2,n3 = [int(i) for i in lista]

print(n1)
print(n2)
print(n3)
print()
print(valorLido1)
print(valorLido2)
print(valorLido3)
"""

if(n1 > n2):
    aux = n1
    n1 = n2
    n2 = aux
    if(n2 > n3):
        aux = n2
        n2 = n3
        n3 = aux
        if(n1 > n2):
            aux = n1
            n1 = n2
            n2 = aux
            print(n1)
            print(n2)
            print(n3)
            print()
            print(valorLido1)
            print(valorLido2)
            print(valorLido3)
        else:
            print(n1)
            print(n2)
            print(n3)
            print()
            print(valorLido1)
            print(valorLido2)
            print(valorLido3)
    else:
        print(n1)
        print(n2)
        print(n3)
        print()
        print(valorLido1)
        print(valorLido2)
        print(valorLido3)
else:
    if(n2 > n3):
        aux = n3
        n3 = n2
        n2 = aux
        if(n1 > n2):
            aux = n1
            n1 = n2
            n2 = aux
            print(n1)
            print(n2)
            print(n3)
            print()
            print(valorLido1)
            print(valorLido2)
            print(valorLido3)
        else:
            if(n2 < n1):
                aux = n1
                n1 = n2
                n2 = n1
                print(n1)
                print(n2)
                print(n3)
                print()
                print(valorLido1)
                print(valorLido2)
                print(valorLido3)
            else:
                print(n1)
                print(n2)
                print(n3)
                print()
                print(valorLido1)
                print(valorLido2)
                print(valorLido3)
                """