__author__ = 'joaquim'
"""
 URI Online Judge | 1131
Grenais

Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1

A Federação Gaúcha de Futebol contratou você para escrever um programa para fazer uma estatística do resultado de vários
GRENAIS. Escreva um programa para ler o número de gols marcados pelo Inter e pelo Grêmio em um GRENAL. Logo após escrever
a mensagem "Novo grenal (1-sim 2-nao)" e solicitar uma resposta. Se a resposta for 1, o algoritmo deve ser executado
novamente solicitando o número de gols marcados pelos times em uma nova partida, caso contrário deve ser encerrado imprimindo:

- Quantos GRENAIS fizeram parte da estatística.
- O número de vitórias do Inter.
- O número de vitórias do Grêmio.
- O número de Empates.
- Uma mensagem indicando qual o time que venceu o maior número de GRENAIS (ou "Nao houve vencedor", caso termine empatado).
Entrada

O arquivo de entrada contém 2 valores inteiros, correspondentes aos gols marcados pelo Inter e pelo Grêmio respectivamente.
Em seguida háverá um inteiro (1 ou 2), correspondente à repetição do programa.
Saída

Após cada leitura dos gols, deve ser impressa a mensagem "Novo grenal (1-sim 2-nao)".
Quando o algoritmo for encerrado deve ser mostrado as estatísticas conforme a descrição apresentada acima.
Obs: a palavra "Gremio" deve ser impressa sem acento, conforme o exemplo abaixo.
Exemplo de Entrada 	Exemplo de Saída

3 2
1
2 3
1
3 1
2
Novo grenal (1-sim 2-nao)
Novo grenal (1-sim 2-nao)
Novo grenal (1-sim 2-nao)
3 grenais
Inter:2
Gremio:1
Empates:0
Inter venceu mais
"""
a = 0
contGrenais = 0
contInter = 0
contGremio = 0
contEmpates = 0
g1 = 0
g2 = 0

while(1):
    g1,g2 = [int(i) for i in input().split(" ")]

    contGrenais += 1

    print("Novo grenal (1-sim 2-nao)")
    a = int(input())

    if g1 > g2:
        contInter += 1
    elif g2 > g1:
        contGremio += 1
    else:
        contEmpates += 1
    if a == 2:
        break

print("%d grenais" %contGrenais)
print("Inter:%d" %contInter)
print("Gremio:%d" %contGremio)
print("Empates:%d" %contEmpates)

if contInter > contGremio:
    print("Inter venceu mais")
elif contGremio > contInter:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")