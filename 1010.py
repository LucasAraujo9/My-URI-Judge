__author__ = 'Joaquim Alves'
"""
Neste problema deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1,
o código de uma peça 2, o número de peças 2, o valor unitário de cada peça 2 e calcula e mostra o valor a ser pago.

Entrada: O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores,
 respectivamente dois inteiros e um valor com 2 casas decimais.
Saída: A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de
deixar um espaço após os dois pontos e um espaço após o $. O valor deverá ser apresentado com 2 casas após o ponto.
12 1 5.30
16 2 5.10    VALOR A PAGAR: R$ 15.50
"""


codPeca,numPeca,valorUni = [float(i) for i in input().split(" ")]
codPeca2,numPeca2,valorUni2 = [float(i) for i in input().split(" ")]

total = ((numPeca * valorUni) + (numPeca2 * valorUni2))

print("VALOR A PAGAR: R$ %.2f"%(total))
