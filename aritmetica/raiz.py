def raiz_quadrada(numero):
    if(numero < 0):
        raise ValueError("Não existe Raíz Real para Números Negativos!")
    elif(numero == 0):
        return (0)
    raiz = numero/2

    for _ in range(20):
        raiz = (1/2)*(raiz+(numero/raiz))

    return (raiz)

def raiz_cubica(numero):
    if(numero == 0):
        return (0)
    
    raiz = numero/3

    for _ in range(20):
        raiz = (1/3) * (2 * raiz + numero / (raiz ** 2))

    return (raiz)

def raiz_enesima(indice, radiciando):
    if (indice % 2 ==  0) and (radiciando < 0):
        raise ValueError("Não existe Raíz Real para Números Pares Negativos!")
    
    elif(indice <= 0):
        raise ValueError("Não existe Raíz de Índice Negativo")
    
    elif(radiciando == 0):
        return (0.0)
    
    raiz = radiciando/indice
    for _ in range(20):
        raiz = (1/indice) * ((indice - 1) * raiz + radiciando / (raiz ** (indice-1)))

    return (raiz)

print(raiz_cubica(-125))

