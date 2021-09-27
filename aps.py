import os#Biblioteca usada para ler uma pasta e mostrar o que há nela.
#
#Função de criptografia por inserção
#
def cripto(escolha):
    y2=0
    y=input("digite a senha ou crie uma: ")
    for i in range(0,len(y)):
        y2=(ord(y[i])+y2)
    z=str(input("digite uma frase: "))
    msg=[]
    for i in range(0,len(z)):
        if y2>=1000:
            y2=ord(y[0])
        x=(ord(z[i])+(y2))
        msg.append(chr(x))
        y2=y2+(y2*2)
    print("".join(msg))
    mst="".join(msg)

    save=int(input('Deseja salvar?'
                   '\nSim[1]'
                   '\nNão[qualquer outro botão]'))
    if save==1:
       narq=str(input("Digite um nome para o arquivo(digite sem o '.txt'):"))
       f=open("criptografias/"+narq+".txt" , "w" , encoding='utf-8')
       f.write(mst)
       f.close()      
#
#Função de criptografia por arquuivo existente
#
def cripto2(escolha):
    msg=[]
    y=input("Digite a senha: ")
    y2=0
    for i in range(0,len(y)):
        y2=(ord(y[i])+y2)
    print(15*"-"+"Arquivos existentes"+(15*"-"))
    for _, _, arq in os.walk('descriptografias/'):
        for i in range(0,len(arq)):
            print(arq[i])
    print(50*"-")
    narq=str(input("Digite o nome do arquivo(digite sem o '.txt'): "))
    f=open("descriptografias/"+narq+".txt","r",encoding='utf-8')
    z=f.readline()
    for i in range(0,len(z)):
        if y2>=1000:
            y2=ord(y[0])
        x=(ord(z[i])+(y2))
        msg.append(chr(x))
        y2=y2+(y2*2)
    print("".join(msg))
    mst="".join(msg)
    f.close()

    save=int(input('Deseja salvar?'
                '\nSim[1]'
                '\nNão[qualquer outro botão]'))
    if save==1:
       narq=str(input("Digite um nome para o arquivo(digite sem o '.txt'):"))
       f=open("criptografias/"+narq+".txt","w",encoding='utf-8')
       f.write(mst)
       f.close()
#
#Função de descriptografia por inserção
#
def descripto(escolha):
    b2=0
    b=input("digite a senha: ")
    for i in range(0,len(b)):
        b2=(ord(b[i])+b2) 
    c=str(input("digite uma frase: "))
    msg=[]
    for i in range(0,len(c)):
        if b2>=1000:
            b2=ord(b[0])
        a=(ord(c[i])-(b2))
        if a<=0:
            print("não é possivel descriptografar.")
            break
        msg.append(chr(a))
        b2=b2+(b2*2)
    print("".join(msg))
    mst="".join(msg)
    if len(c)==len(mst):
        save=int(input('Deseja salvar?'
                      '\nSim[1]'
                      '\nNão[qualquer outro botão]'))
        if save==1:
           narq=str(input("Digite um nome para o arquivo(digite sem o '.txt'):"))
           f=open("descriptografias/"+narq+".txt","w",encoding='utf-8')
           f.write(mst)
           f.close()       
#
#Funçâo de Descriptografia por arquivo existente
#
def descript2(escolha):
    msg=[]
    b=input("Digite a senha: ")
    b2=0
    for i in range(0,len(b)):
        b2=(ord(b[i])+b2)
    print(15*"-"+"Arquivos existentes"+(15*"-"))
    for _, _, arq in os.walk('criptografias/'):
        for i in range(0,len(arq)):
            print(arq[i])
    print(50*"-")
    narq=str(input("Digite o nome do arquivo(digite sem o '.txt'):"))
    f=open("criptografias/"+narq+".txt","r",encoding='utf-8')
    c=f.readline()
    for i in range(0,len(c)):
        if b2>=1000:
            b2=ord(b[0])
        a=(ord(c[i])-(b2))
        if a<=0:
            print("não é possivel descriptografar.")
            break
        msg.append(chr(a))
        b2=b2+(b2*2)
    print("".join(msg))
    mst="".join(msg)
    f.close()
    
    if len(c)==len(mst):
        save=int(input('Deseja salvar?'
                    '\nSim[1]'
                    '\nNão[qualquer outro botão]'))
        if save==1:
           narq=str(input("Digite um nome para o arquivo(digite sem o '.txt'):"))
           f=open("descriptografias/"+narq+".txt","w",encoding='utf-8')
           f.write(mst)
           f.close()   
#
#Programa principal
#
escolha=1
while escolha==1 or escolha==2:
    escolha=int(input("Escolha o que deseja:"
                  "\n[1]Criptografia"
                  "\n[2]Descritografia"))
    if escolha==1:
        escop=int(input('Digite a opção que desejada:'
                     '\n[1]iserir texto para criptografar.'
                     '\n[2]criptografar arquivo existente.'))
        if escop==1:
            cripto(escolha)
        elif escop==2:
            cripto2(escolha)
        else:
            print("comando invalido.")
    elif escolha==2:
        escop=int(input('Digite a opção que desejada:'
                     '\n[1]iserir código para descriptografar.'
                     '\n[2]descriptografar arquivo existente.'))
        if escop==1:
            descripto(escolha)
        elif escop==2:
            descript2(escolha)
        else:
            print("comando invalido.")
    else:
        print("Comando invalido")
    cont= int(input('Deseja continuar?'
                   '\nSim[1]'
                   '\nNão[qualquer botão.]'))
    if cont==1:
        escolha=1
    else:
        print("fim")
        escolha=3
            
        
        




