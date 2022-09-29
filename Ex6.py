ilhas = ['Terceira', 'Pico', 'Faial', 'São Jorge', 'Graciosa', 'Flores', 'Corvo']
tipos = ['Gasolina', 'Gasóleo']
vendas = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

if __name__ == '__main__':
    # Obter input
    for x in range(len(vendas)):
        for y in range(len(vendas[x])):
            while True:
                try:
                    vendas[x][y] = int(input(f'Insira vendas de {tipos[x]} para a ilha {ilhas[y]}: '))
                    break
                except ValueError:
                    print(f'Insira um valor válido para vendas de {tipos[x]} na ilha {ilhas[y]}')
    for venda in vendas:
        print(venda)

    # Imprimir vendas por tipo
    for x in range(len(vendas)):
        total = 0
        for y in range(len(vendas[x])):
            total += vendas[x][y]
        print(f'Total de vendas para {tipos[x]} = {total}')

    # Imprimir vendas por ilha
    z = 0
    for y in range(len(vendas[z])):
        z += 1
        total = 0
        for x in range(len(vendas)):
            total += vendas[x][y]
        print(f'Total de vendas para {ilhas[y]} = {total}')