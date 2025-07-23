def numero_primo(n):
    intervalo_divisores = range(2, n-1)

    for x in intervalo_divisores:
        if(n % x == 0):
            print("Não é primo")
            return 
        else:
            print("É primo")
            return(n)            

def mmc(a):
    pass

def mdc(a):
    pass

a = int(input("Digite um número: "))

numero_primo(a)
