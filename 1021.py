__author__ = 'Joaquim Alves'
"""
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o
menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2.
As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

Entrada: O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).
Saída: Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Exemplo de Entrada	Exemplo de Saída
576.73
NOTAS:
5 nota(s) de R$ 100.00
1 nota(s) de R$ 50.00
1 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
1 nota(s) de R$ 5.00
0 nota(s) de R$ 2.00
MOEDAS:
1 moeda(s) de R$ 1.00
1 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
2 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
3 moeda(s) de R$ 0.01"""

cem = cinq = vinte = dez = cinco = dois = um = cinqCentavos = vinteCinCentavos = dezCentavos = cincoCentavos = umCentavo = 0

valor = float(input())

if(valor >= 100):
    cem = int(valor / 100)
    valor = (valor - (cem * 100))
if(valor >= 50):
    cinq = int(valor / 50)
    valor = (valor - (cinq * 50))
if(valor >= 20):
    vinte = int(valor / 20)
    valor = (valor - (vinte * 20))
if(valor >= 10):
    dez = int(valor / 10)
    valor = (valor - (dez * 10))
if(valor >= 5):
    cinco = int(valor / 5)
    valor = (valor - (cinco * 5))
if(valor >= 2):
    dois = int(valor / 2)
    valor = (valor - (dois * 2))
if(valor >= 1):
    um = int(valor /1)
    valor = (valor - (um * 1))

if(valor >= 0.50):
    cinqCentavos = int(valor / 0.50)
    valor = (valor - (cinqCentavos * 0.50))
if(valor >= 0.25):
    vinteCinCentavos = int(valor / 0.25)
    valor = (valor - (vinteCinCentavos * 0.25))
if(valor >= 0.10):
    dezCentavos = int(valor / 0.10)
    valor = (valor - (dezCentavos * 0.10))
if(valor >= 0.05):
    cincoCentavos = int(valor / 0.05)
    valor = (valor - (cincoCentavos * 0.05))
if(valor >= 0.01):
    umCentavo = int(valor / 0.01)
    valor = (valor - (umCentavo * 0.01))

print("NOTAS:")
print("%d nota(s) de R$ 100.00"%(cem))
print("%d nota(s) de R$ 50.00"%(cinq))
print("%d nota(s) de R$ 20.00"%(vinte))
print("%d nota(s) de R$ 10.00"%(dez))
print("%d nota(s) de R$ 5.00"%(cinco))
print("%d nota(s) de R$ 2.00"%(dois))
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00"%(um))
print("%d moeda(s) de R$ 0.50"%(cinqCentavos))
print("%d moeda(s) de R$ 0.25"%(vinteCinCentavos))
print("%d moeda(s) de R$ 0.10"%(dezCentavos))
print("%d moeda(s) de R$ 0.05"%(cincoCentavos))
print("%d moeda(s) de R$ 0.01"%(umCentavo))
