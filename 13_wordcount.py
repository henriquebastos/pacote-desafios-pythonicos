"""
O main() abaixo já esta definido e completo. Ele chama as funções
print_words() e print_top() que você escreveu.

1. Para a flag --count, implemente a função print_words(filename) que conta
quão frequentemente cada palavra aparace no texto e imprime
word1 count1
word2 count2
...

Imprima a lista acima em ordem crescente por palavra(o Python ira ordenar
a pontuação para vir antes das letras, sem problemas). Armazene todas as palavras
em caixa baixa, assim, as palavras 'The' e 'the' irão contar como a mesma palavra.

2. Para a flag --topcount, implemente a função print_top(filename), que é similar
a print_words(), porém imprime apenas as 20 palavras mais comuns ordenadas, de 
modo que a palavra mais comum aparece primeiro, seguida da segunda mais comum,
e assim por diante.

Use str.split() (sem argumentos) para fazer o split em todo espaço em branco.

Workflow: Não construa todo o programa. Uma coisa de cada vez, imprime sua
estrutura de dados e depois sys.exit(0). Quando isso estiver funcionando,
tente seu proximo marco.

Opcional: defina uma função auxiliar que evita código duplicado dentro 
de print_words() e print_top().
"""

import sys


# +++ SUA SOLUÇÃO +++
# Defina as funções print_words(filename) e print_top(filename).
# Você pode escrever uma função auxiliar para ajudar a ler o arquivo
# e montar e retornar o dicioario word/count.
# Depois print_words() e print_top() podem apenas invocar essa função.

###

# Este comando basico é disponibilizado, e invoca as funções print_words()
# e print_top() que você deve definir.
def main():
    if len(sys.argv) != 3:
        print('Utilização: ./13_wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
