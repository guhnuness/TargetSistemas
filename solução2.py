'''''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
 escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence 
 ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
'''''
#Solução Exercício 2
def gerador_da_sequencia(g):
    if g < 0:
        return False
    
    a, b = 0, 1
    while a <= g:
        if a == g:
            return True
        a, b = b, a + b
    
    return False
num = int(input('Digite um número: \n'))

if gerador_da_sequencia(num):
    print(f" O número {num} Pertence a sequência de Fibonacci.")
else:
    print(f"O número {num} Não pertence a sequência de Fibonacci.")




