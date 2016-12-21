__author__ = 'Joaquim Alves'
"""
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto.
As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada: O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída: Imprima o valor lido e em seguida a quantidade mínima de notas de cada tipo necessárias,
conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário
seu programa apresentará a mensagem: “Presentation Error”.

Exemplo de Entrada	Exemplo de Saída
576
5 nota(s) de R$ 100,00
1 nota(s) de R$ 50,00
1 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
1 nota(s) de R$ 5,00
0 nota(s) de R$ 2,00
1 nota(s) de R$ 1,00
"""
cem = cinq = vinte = dez = cinco = dois = um = 0

valor = int(input())
print(valor)

#if(valor >= 100):
cem = int(valor / 100)
valor = (valor - (cem * 100))
#if(valor >= 50):
cinq = int(valor / 50)
valor = (valor - (cinq * 50))
#if(valor >= 20):
vinte = int(valor / 20)
valor = (valor - (vinte * 20))
#if(valor >= 10):
dez = int(valor / 10)
valor = (valor - (dez * 10))
#if(valor >= 5):
cinco = int(valor / 5)
valor = (valor - (cinco * 5))
#if(valor >= 2):
dois = int(valor / 2)
valor = (valor - (dois * 2))
#if(valor >= 1):
um = int(valor /1)
valor = (valor - (um * 1))

print("%d nota(s) de R$ 100,00"%(cem))
print("%d nota(s) de R$ 50,00"%(cinq))
print("%d nota(s) de R$ 20,00"%(vinte))
print("%d nota(s) de R$ 10,00"%(dez))
print("%d nota(s) de R$ 5,00"%(cinco))
print("%d nota(s) de R$ 2,00"%(dois))
print("%d nota(s) de R$ 1,00"%(um))