"""
Declare uma lista para guardar as vendas de gasolina e gas´´eo no grupo oriental
Apresente:
- Total das vendas
- O total de vendas de gasolina
- O total de vendas de gasóleo
- O total de vendas para cada ilha

Exemplo da estrutura de armazenamento das vendas:

    vendas = [
         TER PIC  FAI  GRA  SJR
        [10, 20 , 30, 40 , 50], #Gasolina
        [15, 25, 35, 45, 55]    #Gasoleo
    ]

    ou então:

    vendas = [
         Gasoleo
          |  Gasolina
        [10, 15], TER
        [20, 25], PIC
        [30, 35], FAI
        [40, 45], GRA
        [50, 55]  SJR
    ]
"""

if __name__ == '__main__':
    vendas = [
        [1, 2, 3, 4, 5],
        [10, 11, 12, 13, 14]
    ]
    print(vendas)

    for venda in vendas:
        print(venda)
        for v in venda:
            print(v)

    x = 0
    y = 0

    print(f'vendas[x][y]={vendas[x][y]}')

    for x in range(2):
        for y in range(5):
            print(f'vendas[{x}][{y}]={vendas[x][y]}')
            print('xxxx')

    print()
    for x in range(len(vendas)):
        for y in range(len(vendas[0])):
            print(f'vendas[{x}][{y}]={vendas[x][y]}')
        print('xxxx')

    # total de vendas
    total_vendas = 0
    for x in range(2):
        total_linha = 0
        for y in range(5):
            #print(f'vendas[{x}][{y}]={vendas[x][y]}')
            total_vendas = total_vendas + vendas[x][y]
            total_linha = total_linha + vendas[x][y]
        print(f'total_linha={total_linha}')
    print(f'total_vendas={total_vendas}')
