import sys
filai=[]
filag=[]
filan=[]
senha= 1#Gerador de Senhas
while True:
    fila=int(input('''Para inserir uma pessoa na fila aperte[1]
Para fazer com que a fila ande aperte[2]
Para encerrar o programa aperte [3]:'''))#Menu de escolha para o usuário 
    if fila == 1:
        idoso=input("Vc é idoso[S/N]:").upper()
        gravida= input("Vc esta gravida[S/N]").upper()
        if idoso != "S" and gravida!="S":
            print("Sua senha é:",senha)
            filan.append(senha)#Coloca a pessoa na fila normal
            senha+=1
        if idoso=="S":
            print("Sua senha é:",senha)
            filai.append(senha)#Coloca a pessoa na fila dos idosos
            senha+=1
        if gravida=="S":
            print("Sua senha é:",senha)
            filag.append(senha)#Coloca a pessoa na fila das gravidas 
            senha+=1
    if fila == 2:
        if len(filai)>0: 
            filai.pop(0)#Remove o primeiro da fila dos idosos
        elif len(filag)>0:
            filag.pop(0)#Remove o primeiro da fila das gravidas
        elif len(filan)>0:
            filan.pop(0)#Remove o primeiro da fila dos normais 
    if fila == 3:
        input("Aperte qualquer tecla para sair do programa")
        sys.exit()#Função proporcianada pela biblioteca sys para sair do programa
    print('''------
      | {}
PyBank| {}
      | {}
-------       
    '''.format(filan,filai,filag))#Demonstração da fila