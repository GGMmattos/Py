#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavra = ('Caderno', 'Limao', 'borracha', 'Python', 'Mao')

for p in palavra:
    print(f"\nNa palavra {p.upper()} temos ", end='')
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=' ')
