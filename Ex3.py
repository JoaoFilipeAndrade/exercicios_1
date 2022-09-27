"""
Complete o programa

Pergunte ao utilizador quantos números quer
Pergunte ao utilizador qual é o intervalo para obter numeros aleatórios
Pergunte se deseja ver apenas pares, apenas impares ou apenas primos
Mostre todos os números aleatórios
Mostre todos os números que satisfazem o pedido do utilizador
"""
import random


def get_random(ini, fim):
    """
    Esta função devolve um número aleatório entre ini e fim inclusive
    :param ini: inicío do intervalo
    :param fim: fim do intervalo
    :return: número aleatório
    """
    return random.randrange(ini, fim + 1)


if __name__ == '__main__':
    while True:
        try:
            quantos = int(input('Quantos? '))
            break
        except ValueError:
            print('Insere valores válidos!')

    while True:
        try:
            ini = int(input('Valor inicial? '))
            fim = int(input('Valor final? '))
            if fim < ini:
                print("O valor final não pode ser menor que o inicial")
                continue
            break
        except:
            print('Insere valores válidos')


