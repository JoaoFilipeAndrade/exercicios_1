"""
Declare uma lista para guardar as vendas do grupo central
Declara uma lista para guardar os nomes das cinco ilhas do grupo central
Peça dados ao utilizador e guarde-os na lista
Após o utilizador ter inserido os 5 valores apresente:
- Total das vendas
- O menor valor inserido
- O maior valor inserido
- A média das vendas
"""

ilhas = ['Terceira', 'Graciosa', 'Pico', 'Faial', 'São Jorge']

if __name__ == '__main__':
    vendas = [0, 0, 0, 0, 0]
    x = 0
    for ilha in ilhas:
        vendas[x] = (float(input(f'Insira as vendas para {ilha} ')))
        x += 1
    print(f'vendas={vendas}')

    x = 0
    while x < len(ilhas):
        vendas.append(float(input(f'Insira as vendas para {ilhas[x]} ')))
        x += 1
    print(f'vendas={vendas}')


    print(f'vendas={vendas}')

"""
    continuar = 's'
    while continuar == 's':
        ini = int(input('Insira o número inicial '))
        fim = int(input('Insira o número final '))
        primos = 0
        for n in range(ini, fim + 1):
            if divisores(n) == 2:
                primos += 1
        print(f'Entre {ini} e {fim} há {primos} de primos.')
        continuar = input('Repetir [s | n]? ')
    print(f'Adeus!')
"""
