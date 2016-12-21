__author__ = 'Joaquim Alves'
"""
Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando essas informações.

Entrada

A primeira linha da entrada contém um valor inteiro N (N < 10000), que indica o número de casos de teste.
Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).


Saída

Para cada caso, imprima quantos números estão dentro (in) e quantos valores estão fora (out) do intervalo.

Exemplo de Entrada	Exemplo de Saída
4
14
123
10
-25
2 in
2 out
"""


N = int(input())
contIn = 0
contOut = 0

for i in range(N):
    valor = int(input())
    if(valor >= 10 and valor <= 20):
        contIn += 1
    else:
        contOut += 1

print("%d in"%contIn)
print("%d out"%contOut)