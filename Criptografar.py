import decimal
def criptografar(codigo, publica1, publica2):
    resultado = decimal.Decimal(pow(codigo,publica1))
    resultado = resultado % publica2
    #resultado = (codigo**publica1) % publica2
    return resultado

nomearquivo = input("Digite o nome do arquivo com as chaves publicas: ")
arquivo = open(nomearquivo, "r")
chaves = []
linhas = arquivo.read().splitlines()
for linha in linhas:
    chaves.append(linha)
arquivo.close()
print(chaves[0])
print(chaves[1])
limitador = 1
while limitador != 0:
    print("Digite a mensagem a ser Criptografada*\n*Limite de 120 caracteres")
    mensagem = input("Mensagem: ")
    crtg = ""
    if len(mensagem) <= 120:
        limitador = 0
        for letra in mensagem:
            crtg = crtg.join(chr(criptografar(ord(letra),decimal.Decimal(chaves[0]),decimal.Decimal(chaves[1]))))
        print(str(crtg))
    else:
        print("mensagem ultrapassa o limite, tente novamente")