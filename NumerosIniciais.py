import secrets


def testeNumero(num, k=40):
    if num <= 1 or num % 2 == 0:
        return False

    n = num - 1
    s = 0
    while n % 2 == 0:
        s += 1
        n //= 2
    for vezes in range(k):
        a = secrets.SystemRandom().randrange(2, num-1)
        b = pow(a,n,num)
        if b != 1 and b != num-1:
            bx = 1
            while bx < s and bx != num-1:
                b = pow(b,2,num)
                if b == 1:
                    return False
                bx+=1
            if b != num-1:
                return False
    return True

def tentaNumero(tamanho=200):
    c = secrets.SystemRandom()
    numero = 2 * (c.getrandbits(tamanho) // 2) + 1
    return numero

def criaNumero(tamanho=200):
    numero = tentaNumero(tamanho)
    while not testeNumero(numero):
        numero = tentaNumero(tamanho)
    return numero

