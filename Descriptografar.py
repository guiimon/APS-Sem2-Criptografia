import rsa
import os
import sys
while True:
    nomeChavePri = input("Digite o nome do arquivo .pem que contém a Chave Privada: ")
    if os.path.exists(nomeChavePri + ".pem") == True:
        arquivoPrivado = open(nomeChavePri+".pem", "rb")
        infodoArquivo = arquivoPrivado.read()
        arquivoPrivado.close()
        try:
            ChavePrivada = rsa.PrivateKey.load_pkcs1(infodoArquivo)
        except:
            print("Arquivo não é do padrão chave Privada, tente outro arquivo.")
        else:
            while True:
                print("Digite o caminho do arquivo txt com a mensagem criptografada. \nCaso esteja na mesma pasta que esse só escreva o nome do arquivo,")
                caminho = input("Caminho: ")
                if os.path.exists(caminho+".txt") == True:
                    arquivo = open(caminho+".txt","rb")
                    mensagemC = arquivo.read()
                    arquivo.close()

                    try:
                        mensagem = rsa.decrypt(mensagemC,ChavePrivada)
                    except:
                        print("Arquivo não é do padrão de mensagem criptografada, tente outro arquivo")
                    else:
                        print("A Mensagem descriptografada é: \n %s" % mensagem.decode('utf8'))
                        break
                else:
                    print("Arquivo informado não existe, tente outro arquivo.")
            break
    else:
        sys.exit("Arquivo informado não existe, tente outro nome de arquivo.")