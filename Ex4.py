"""
Declare uma lista para guardar as vendas do grupo central
Declara uma lista para guardar os nomes das cinco ilhas do grupo central
Peça dados ao utilizador e guarde-os na lista
Após o utilizador ter inserido os 5 valores apresente:
- Total das vendas
- O menor valor inserido assim como as respetivas ilhas
- O maior valor inserido assim como as respetivas ilhas
- A média das vendas
"""

from builtins import sum

ilhas = ['da Terceira', 'da Graciosa', 'do Pico', 'do Faial', 'de São Jorge']

if __name__ == '__main__':
    maior_ilhas = []
    menor_ilhas = []
    vendas = []

    for ilha in ilhas:
        vendas.append((int(input(f'Insira as vendas para {ilha} '))))

    menor = vendas[0]
    maior = vendas[0]

    for x in range(0, len(vendas)):

        if vendas[x] == menor:
            menor_ilhas.append(ilhas[x])

        elif vendas[x] < menor:
            menor = vendas[x]
            menor_ilhas.append(ilhas[x])

            if vendas[x-1] == vendas[0]:
                menor_ilhas.pop(0)

        if vendas[x] == maior:
            maior_ilhas.append(ilhas[x])

        elif vendas[x] > maior:
            maior = vendas[x]
            maior_ilhas.append(ilhas[x])

            if vendas[x-1] == vendas[0]:
                maior_ilhas.pop(0)

    print(f'O maior é {maior} e a(s) respetiva(s) Ilha(s) são(é) {"a Ilha " + " a Ilha ".join(maior_ilhas)}.')
    print(f'O menor é {menor} e a(s) respetiva(s) Ilha(s) são(é) {"a Ilha " + " a Ilha ".join(menor_ilhas)} .')
    ''' print(f'O maior é {max(vendas)} e o menor é {min(vendas)}.')
        print(f'O maior é {sorted(vendas)[4]} e o menor é {sorted(vendas)[0]}.')
    '''
    total = 0
    for v in vendas:
        total += v

    media = total / len(vendas)

    print(f'O total é {sum(vendas)} e a média é {media}.')
