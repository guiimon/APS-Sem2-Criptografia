import rsa
import os
import sys
"""
from Chaves import inversoMod
def criptografar(codigo, publica1, publica2):
    resultado = inversoMod(codigo**publica1,publica2)
    if resultado == None:
        return codigo
    else:
    #resultado = decimal.Decimal(pow(codigo,publica1))
    #resultado = resultado % publica2
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
            crtg = crtg+ crtg.join(chr(criptografar(ord(letra),decimal.Decimal(chaves[0]),decimal.Decimal(chaves[1]))))
        print(str(crtg))
    else:
        print("mensagem ultrapassa o limite, tente novamente")
"""
while True:
    NomeChavePub = input("Digite o nome do arquivo .pem que contém a Chave Publica: ")
    if os.path.exists(NomeChavePub+".pem") == True:
        arquivoPublico = open(NomeChavePub+".pem", "rb")
        infodoArquivo = arquivoPublico.read()
        arquivoPublico.close()
        try:
            ChavePublica = rsa.PublicKey.load_pkcs1(infodoArquivo)
        except:
            print("Arquivo não é do padrão de Chave Publica, tente outro arquivo.")
        else:
            while True:
                mensagem = input("Digite a mensagem a ser criptografada: ")
                if len(mensagem) <= 120:
                    criptografada = rsa.encrypt(mensagem.encode('utf8'),ChavePublica)
                    NomeMensagem = input("Digite o nome do arquivo para ser salva a mensagem criptografada: ")
                    arquivo = open(NomeMensagem+".txt","wb")
                    arquivo.write(criptografada)
                    arquivo.close()
                    print(f"Arquivo {NomeMensagem}.txt criado com sucesso.")
                    break
                else:
                    print("Mensagem acima do limite de caracteres permitidos, digite uma mensagem de até 120 caracteres.")
            break
    else:
        sys.exit("Arquivo informado não existe, tente outro nome de arquivo.")