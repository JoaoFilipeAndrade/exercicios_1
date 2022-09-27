"""
Peça ao utilizador para inserir uma frase
Após o utilizador ter inderido a frase apresente:
 - Imprima a frase, mas com cada palavra invertida. Por exemplo 'Bom dia!' deve dar 'moB !aid'
 - Imprima a frase, mas com as maiusculas em minisculo e as minusculas em maiusculas.
"""


def reverse_pos(string):
    for elm in string.split():
        k = ''  # temporar string that holds the reversed strings
        for j in elm:
            k = j + k
        yield k


if __name__ == '__main__':
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    frase = input('Insere uma frase: ')
    x = 0
    novafrase = frase.split(' ')
    print(novafrase)

    new_frase = " ".join(novafrase)
    print(' '.join(reverse_pos(new_frase)))

    new_frase2 = " ".join(novafrase)
    print(new_frase.swapcase())
