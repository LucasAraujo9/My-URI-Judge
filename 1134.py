__author__ = 'joaquim'
"""
 URI Online Judge | 1134
Tipo de Combustível

Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1

Um Posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes. Escreva um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma: 1.Álcool 2.Gasolina 3.Diesel 4.Fim). Caso o usuário informe um código inválido (fora da faixa de 1 a 4) deve ser solicitado um novo código (até que seja válido). O programa será encerrado quando o código informado for o número 4.
Entrada

A entrada contém apenas valores inteiros e positivos.
Saída

Deve ser escrito a mensagem: "MUITO OBRIGADO" e a quantidade de clientes que abasteceram cada tipo de combustível, conforme exemplo.
Exemplo de Entrada 	Exemplo de Saída

8
1
7
2
2
4
MUITO OBRIGADO
Alcool: 1
Gasolina: 2
Diesel: 0
"""

contA = 0
contG = 0
contD = 0
cont = 0

def entradaInputs():
    global contA
    global contG
    global contD
    global cont
    x = int(input())

    if x > 4 or x < 1:
        return  entradaInputs()
    
    if x == 1:
        contA += 1
    elif x == 2:
        contG += 1
    elif x == 3:
        contA += 1
    if x == 4:
        print("MUITO OBRIGADO")
        print("Alcool:", contA)
        print("Gasolina:", contG)
        print("Diesel:", contD)
        cont += 1
    if cont != 1:
        return entradaInputs()

def main():
    entradaInputs()

if __name__ == "__main__":main()