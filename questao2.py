'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;'''

def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        c = a + b
        a = b
        b = c
    return c

while True:
    try:
        n = int(input('Digite um número inteiro: '))
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

if fibonacci(n):
    print('O número informado pertence à sequência de Fibonacci.')
else:
    print('O número informado não pertence à sequência de Fibonacci.')