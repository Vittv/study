# Faça um programa onde 4 jogadores joguem um dado e recebam resultados aleatórios
# guarde os mesmos em um dicionário. Por fim coloque o mesmo em ordem, sabendo que
# o vencedor tirou o maior número no dado:

from random import randint
from time import sleep

jogadores = {}

print('Valores sorteados:')
for i in range(1, 5):
    jogadores[f'jogador{i}'] = randint(1, 6)
    print(f'O {f"jogador{i}"} tirou {jogadores[f"jogador{i}"]}')
    sleep(1)

print('Ranking dos jogadores:')

jogadores_ordem = dict(sorted(jogadores.items(), key=lambda item: item[1], reverse=True))
for lugar, (jogador, valor) in enumerate(jogadores_ordem.items(), start=1):
    print(f'{lugar}o lugar: {jogador} com {valor}')