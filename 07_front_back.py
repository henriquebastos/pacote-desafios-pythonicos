"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""
def front_back(a, b):
    # +++ SUA SOLUÇÃO +++
    # Even Numbers
    if len(a) % 2 == 0:
        front_a = a[:len(a) // 2]
        back_a = a[len(a) // 2:]
        front_b = b[:len(b) // 2]
        back_b = b[len(b) // 2:]
    # Odd Numbers
    if len(a) % 2 != 0:
        front_a = a[:(len(a) // 2)+1]
        back_a = a[(len(a) // 2)+1:]
        front_b = b[:(len(b) // 2)+1]
        back_b = b[(len(b) // 2)+1:]
    # Even and Odd Numbers
    if len(a) % 2 == 0 and len(b) % 2 != 0:
        front_a = a[:len(a) // 2]
        back_a = a[len(a) // 2:]
        front_b = b[:(len(b) // 2)+1]
        back_b = b[(len(b) // 2)+1:]
    return front_a + front_b + back_a + back_b 

# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')
