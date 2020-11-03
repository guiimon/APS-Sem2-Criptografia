import secrets
c = secrets.SystemRandom()
def mdc (valor1, valor2):
    while valor2 != 0:
        resto = valor1 % valor2
        valor1 = valor2
        valor2 = resto
    #print(f"valor1: {valor1}")
    #print(f"valor2: {valor2}")
    return valor1

def inversoMod(testado, fimbloco):
    if mdc(testado, fimbloco) != 1:
        return None
    u1, u2, u3 = 1, 0, testado
    v1, v2, v3 = 0, 1, fimbloco

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % fimbloco

def coprimo(testado, tamanho=200):
    while True:
        cp = c.randrange(2**(tamanho-1),2**(tamanho))
        if mdc(cp,testado) == 1:
            break
    return cp
def criaChave(p, q):
    n = p*q
    n2 = (p-1)*(q-1)
    z = coprimo(n2)
    d = inversoMod(z,n2)
    chavesPublicas = [n,z]
    chavesPrivadas = [n,d]
    return (chavesPrivadas,chavesPublicas)


#tem que terminar essa função ainda
