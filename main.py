import rsa
import os
import sys
print("Criando chaves criptográficas...")
pubkey,privkey = rsa.newkeys(2048)

while True:
    nomePub = input("Digite o nome do arquivo .pem que terá a chave Publica: ")
    nomePriv = input("Digite o nome do arquivo .pem que terá a chave Privada: ")
    if os.path.exists(f"{nomePub}.pem") or os.path.exists(f"{nomePriv}.pem"):
        sys.exit(f"Já existe um arquivo com o nome {nomePub}.pem ou com o nome {nomePriv}.pem use outro nome ou apague os arquivos existentes e tente novamente!")
    else:
        publica = rsa.PublicKey.save_pkcs1(pubkey, "PEM")
        q = open(nomePub+".pem", "wb")
        q.write(publica)
        q.close()

        privada = rsa.PrivateKey.save_pkcs1(privkey,"PEM")
        r = open(nomePriv+".pem", "wb")
        r.write(privada)
        r.close()

        print(f"Criados arquivos {nomePub}.pem e {nomePriv}.pem com suas respectivas chaves!!")
        break
"""
--- Antiga criação de Chaves ---
from NumerosIniciais import criaNumero
from Chaves import criaChave
p = criaNumero()

q = criaNumero()
while p == q:
    q = criaNumero()
print(p)
print(q)
z,y = criaChave(p,q)
print(z)
print(y)
privada = open("ChavePrivada.txt","w")
privada.write(str(z[0])+"\n"+str(z[1]))
privada.close()
publica = open("ChavePublica.txt","w")
publica.write(str(y[0])+"\n"+str(y[1]))
publica.close()
"""