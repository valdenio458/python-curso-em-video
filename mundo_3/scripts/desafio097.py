"""
Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma
mensagem com tamanho adaptável. """


def escreva(txt):
    print('-' * len(txt))
    print(txt)
    print('-' * len(txt))


escreva('De acordo com o tamanho')
escreva('Curso em Vídeo')
escreva('Curso de Python no YouTube')
