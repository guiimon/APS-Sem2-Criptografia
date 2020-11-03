from NumerosIniciais import criaNumero
from Chaves import criaChave
p = criaNumero()

q = criaNumero()
while p == q:
    q = criaNumero()
#print(p)
#print(q)
z,y = criaChave(p,q)
#print(z)
#print(y)
privada = open("ChavePrivada.txt","w")
privada.write(str(z[0])+"\n"+str(z[1]))
privada.close()
publica = open("ChavePublica.txt","w")
publica.write(str(y[0])+"\n"+str(y[1]))
publica.close()
print("Criados arquivos ChavePublica.txt e ChavePrivada.txt com suas respectivas chaves!!")
