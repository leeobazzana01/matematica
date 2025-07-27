def uniao_conjuntos(lista1, lista2):
    uniao = []
    for n in lista1:
        if(n not in uniao):
            uniao.append(n)
        
    for k in lista2:
        if(k not in uniao):
            uniao.append(k)
        
    uniao.sort()
    return (uniao)

def interseccao_conjuntos(lista1, lista2):
    interseccao = []
    
    for n in lista1:
        if(n in lista1) and (n in lista2):
            interseccao.append(n)

    interseccao.sort()
    return interseccao

def diferenca_cojuntos(lista1, lista2):
    diferenca_cojuntos = []

    for n in lista1:
        if(n not in lista2):
            diferenca_cojuntos.append(n)

    diferenca_cojuntos.sort()

    return(diferenca_cojuntos)

def complementar_conjuntos(lista1, lista2):
    complementar = []

    for n in lista1:
        if(n not in lista2):
            complementar.append(n)

    complementar.sort()
    
    return complementar

