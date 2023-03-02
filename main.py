
#    1. Multiplicação de dois números naturais, através de somas sucessivas (Ex.: 6 ∗ 4 = 4 + 4 + 4 + 4 + 4 + 4).
def exec1(a, b):
    if a <= 0:
        return 0
    return b + exec1(a - 1, b)


print("6 x 4= ", exec1(6, 4))

# 1. Soma de dois números naturais, através de incrementos sucessivos (Ex.: 3 + 2 = + + (+ + + 1)).
def exec2(a, b):
    if (a > 0):
        return 1 + exec2(a-1, b)
    if (b > 0):
        return 1 + exec2(a, b - 1)
    
    return 0

print(exec2(4, 5))

# Cálculo de 1 + 1/2 + 1/3 + 1/4 + ... + 1/(n-1) + 1/N.
def exec3(n):
    if n <= 1:
        return 1
    return 1/n + exec3(n-1)

print(exec3(5))


# Inversão de uma string.
def exec4(palavra):
    if palavra == "":
        return ""
    
    return palavra[-1] + exec4(palavra[0: len(palavra) - 1])

print(exec4("melhoras"))


#    1. Gerador da sequência dada por:
#          * F(1) = 1
#          * F(2) = 2
#          * F(n) = 2 ∗ F(n − 1) + 3 ∗ F(n − 2).
def exec5(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return  2 * exec5(n - 1) + 3*exec5(n - 2)

print(exec5(5))

# 1.  Gerador de Sequência de Ackerman:
#          * A(m, n) = n + 1, se m = 0
#          * A(m, n) = A(m − 1, 1), se m != 0 e n = 0
#          * A(m, n) = A(m − 1, A(m, n − 1)), se m != 0 e n != 0.

def exec6(m, n):
    if m == 0:
        return n+1
    
    if n == 0:
        return exec6(m-1, 1)
    
    return exec6(m-1, exec6(m, n-1))

print(exec6(3, 4))


# A partir de um vetor de números inteiros, calcule a soma e o produto dos elementos
# do vetor.

def exec7(vetor):
    if (len(vetor) == 0):
        return 0
    if (len(vetor) == 1):
        return vetor[0]
   
    return vetor[0] + exec7(vetor[1:])


print(exec7([1,2,3,4]))


#    1. Verifique se uma palavra é palíndromo (Ex. aba, abcba, xyzzyx).
def exec8(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    
    return exec8(word[1:(len(word) -1)])

print(exec8("ana"))
print(exec8("banana"))
print(exec8("abcba"))


# 1. Dado um número n, gere todas as possíveis combinações com as n primeiras letras
# do alfabeto. Ex.: n = 3. Resposta: ABC, ACB, BAC, BCA, CAB, CBA.
alfabeto = "abcdefghijklmnopqrstuvwxyz"
def exec9(n):
    global alfabeto
    alf = alfabeto[0: n]

    return exec9_aux(alf)
    

def exec9_aux(alf):
    if (len(alf) == 1):
        return alf

    combinacoes = []

    for l in alf:
        c = exec9_aux(alf.replace(l, ""))
        for x in c:
            combinacoes.append(l + x)
    
    return combinacoes
    

print(exec9(3))
print(exec9(4))

# Defina uma sequência de Fibonacci generalizada, de f0 a f1 como sequência
# fibg(f0, f1, 0), fibg(f0, f1, 1), fibg(f0, f1, 2), ..., onde:
#          * fibg(f0, f1, 0) = f0
#          * fibg(f0, f1, 1) = f1
#          * fibg(f0, f1, n) = fibg(f0, f1, n − 1) + fibg(f0, f1, n − 2), se n > 1.
def exec10(f0, f1, n):
    if (n == 0):
        return f0
    if (n == 1):
        return f1

    return exec10(f0, f1, n - 1) + exec10(f0, f1, n-2)
