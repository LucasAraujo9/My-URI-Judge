__author__ = 'Joaquim Alves'
"""
Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma mensagem que
 indique se estes valores foram digitados em ordem crescente ou decrescente.

Entrada: A entrada contém vários casos de teste. Cada caso contém dois valores inteiros X e Y. A leitura deve ser
encerrada ao ser fornecido valores iguais para X e Y.

Saída: Para cada caso de teste imprima “Crescente”, caso os valores tenham sido digitados na ordem crescente,
caso contrário imprima a mensagem “Decrescente”.

Exemplo de Entrada	Exemplo de Saída
5 4
7 2
3 8
2 2
Decrescente
Decrescente
Crescente
"""

a = 1
lista = []
while(a > 0):
    X,Y = [int(i) for i in input().split(" ")]
    if( X == Y):
        break
    lista.append(X)
    lista.append(Y)

cont = 0
A = B = 0

for i in range(len(lista)):
    if cont == 0:
        A = lista[i]
    if cont == 1:
        B = lista[i]
    cont += 1
    if cont == 2:
        if A > B:
            print("Decrescente")
            cont = 0
        else:
            print("Crescente")
            cont = 0