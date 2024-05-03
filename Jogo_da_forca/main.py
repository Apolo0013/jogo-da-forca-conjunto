# Projeto Simples Jogo Da Forca Autores:  Apolo , Anark e Kadu

# Importações iniciais
from random import randint
from time import sleep
from banco import *
"""
Apolo:
Implementação da lógica do jogo:
Seleção aleatória de palavras de uma lista pré-definida.
Criação da estrutura de dados para armazenar a palavra secreta e as letras já escolhidas.
Contagem de erros e verificação de vitória/derrota.
Criação das funções principais do jogo, como iniciar_jogo(), adicionar_letra(), verificar_vitoria() et"""


# Funcoes

# Seleção aleatória de palavras de uma lista pré-definida.
def Plv_aleatoria(palavras):
    global escolhendo
    try:
        # Escolhendo a palvras que sera o implementado no jogo
        escolhendo = randint(0, len(palavras))
        palavras_escolhida = palavras[escolhendo]
    except IndexError:
        print('algo de errado')
    else:
        return palavras_escolhida


# Criação das funções principais do jogo, como iniciar_jogo(), adicionar_letra(), verificar_vitoria()
def iniciar_jogo():
    global chances, palavras_da_forca, escolhendo , palavras_es
    chances = 5
    # Palavra escolhida seu merda
    palavras_es = Plv_aleatoria(palavras=palavras_forca)
    palavras_da_forca = []  # Palavras que sera exbidar e ondem as letras corretas irar parece
    for c in range(0, len(palavras_es)):
        palavras_da_forca.append(['?'])

    while True:
        print(f'dica: {dicas[escolhendo]}')
        print(f'chances: {chances}')
        letra = input()  # Anark viado, variavel que o usuario vai inserir a letra, ou seja vai palpita pae
        # e botar .lower() no final e tenta pegar so a primeira letra, pq tem gaito que escreve mais que o esperado
        adicionar_letra(letra_digitada = letra)
        for letras in palavras_da_forca:
            print(letras[0], end = ' ')
        print()

        ganhou = verificar_vitoria(palavras_da_forca)

        if ganhou:
            for c in palavras_da_forca:
                for v in c:
                    print(v , end = '')
            print('voce ganhou')
            break

        if chances == 0:
            print('voce perdeu')
            break


# adicionar_letra(), vai verificar se a letra tem na palavra escolhida e retorna se tem ou nao tem a letra
def adicionar_letra(letra_digitada):
    global palavras_da_forca , palavras_es , chances
    tem = False  # Verificar se tem a letra que o usuario digitou
    for index, letras in enumerate(palavras_es):
        for letra in letras:
            if letra == letra_digitada:
                # se tive alguma letra tem sera verdadeiro
                del palavras_da_forca[index]
                tem = True
                palavras_da_forca.insert(index, letras)

    # A letra que o usuario digitou tem?
    if tem:
        print('sim tem')  # Kadu da um up nisso

    else:
        chances -= 1
        print('tem nao fdp')  # Mesma coisa


#aqui verificamos se o usuarios ganhou ou ainda esta jogando
def verificar_vitoria(palavra):
    up = 0 # Verificação se ele ganhou com numeros
    ganhou = False

    for ct in palavra:
        for letras in ct:
            if letras not in '?':
                up += 1

    if up == len(palavra):
        ganhou = True
        return ganhou

    else:
        ganhou = False
        return ganhou



if __name__ == '__main__':
    iniciar_jogo()
