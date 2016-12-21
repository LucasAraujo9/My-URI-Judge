__author__ = 'Joaquim Alves'
"""
Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

Entrada: O arquivo de entrada contém 100 números inteiros, positivos e distintos.
Saída: Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.

Exemplo de Entrada	Exemplo de Saída
2
113
45
34565
6
...
8                   34565
                        4
"""
maior = 0
maior2 = 0

for i in range(100):
    valor = int(input())
    maior = valor
    if(maior > maior2):
        maior2 = maior
        posicao = i+1

print(maior2)
print(posicao)