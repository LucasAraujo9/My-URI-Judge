__author__ = 'Joaquim Alves'
"""
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares,
quantos valores digitados foram positivos e quantos valores digitados foram negativos.

Entrada: O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída: Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.

Exemplo de Entrada	Exemplo de Saída
-5
0
-3
-4
12

3 valor(es) par(es)
2 valor(es) impar(es)
1 valor(es) positivo(s)
3 valor(es) negativo(s)
"""
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

cont = 0
contImpar = 0
contP = 0
contN = 0

if(n1 % 2 == 0):
    cont += 1
else:
    contImpar += 1
if(n2 % 2 == 0):
    cont += 1
else:
    contImpar += 1
if(n3 % 2 == 0):
    cont += 1
else:
    contImpar += 1
if(n4 % 2 == 0):
    cont += 1
else:
    contImpar += 1
if(n5 > 0):
    cont += 1
else:
    contImpar += 1
if(n1 > 0):
    contP += 1
else:
    if(n1 < 0):
        contN += 1
if(n2 > 0):
    contP += 1
else:
    if(n2 < 0):
        contN += 1
if(n3 > 0):
    contP += 1
else:
    if(n3 < 0):
        contN += 1
if(n4 > 0):
    contP += 1
else:
    if(n4 < 0):
        contN += 1
if(n5 > 0):
    contP += 1
else:
    if(n5 < 0):
        contN += 1

print("%d valor(es) par(es)"%cont)
print("%d valor(es) impar(es)"%contImpar)
print("%d valor(es) positivo(s)"%contP)
print("%d valor(es) negativo(s)"%contN)
