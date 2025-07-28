from functools import reduce

def numero_primo(lista_numeros):
    lista_primos = []
    for numero in lista_numeros:
        if numero < 2:
            continue
        eh_primo = True
        for x in range(2, int(numero**0.5) + 1):
            if numero % x == 0:
                eh_primo = False
                break
        if eh_primo:
            lista_primos.append(numero)
    lista_primos.sort()
    return lista_primos

def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

def mdc_lista(lista_numeros):
    return reduce(mdc, lista_numeros)

def mmc(a, b):
    return abs(a * b) // mdc(a, b)

def mmc_lista(lista_numeros):
    return reduce(mmc, lista_numeros)

