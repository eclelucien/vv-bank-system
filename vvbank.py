class tcadastro:
  nome=' '
  sobrenome=' '
  senha=0
  cpf=0
  numero_de_cartao=0
  Saldo=0
 


lista=[]

senharoot=123456


#Funçao para validar CPF 
import re

def isCpfValid(cpf):

    if not isinstance(cpf,str):
        return False

    cpf = re.sub("[^0-9]",'',cpf)

    for i in range(1, 10):
        if cpf == str(i)*11:
            return False

    if len(cpf) != 11:
        return False

    sum = 0
    weight = 10

    """ Calculating the first cpf check digit. """
    for n in range(9):
        sum = sum + int(cpf[n]) * weight

        weight = weight - 1

    verifyingDigit = 11 -  sum % 11

    if verifyingDigit > 9 :
        firstVerifyingDigit = 0
    else:
        firstVerifyingDigit = verifyingDigit

    sum = 0
    weight = 11
    for n in range(10):
        sum = sum + int(cpf[n]) * weight

        weight = weight - 1

    verifyingDigit = 11 -  sum % 11

    if verifyingDigit > 9 :
        secondVerifyingDigit = 0
    else:
        secondVerifyingDigit = verifyingDigit

    if cpf[-2:] == "%s%s" % (firstVerifyingDigit,secondVerifyingDigit):
        return True
    return False





#Funcao para altera os dad  os dos clientes
def altera(Lista):
	print()
	print('Nome:',Lista[i].nome)
	print('Sobrenome:',Lista[i].sobrenome)
	print('cpf:',Lista[i].cpf)
	print('Numero de cartao:',Lista[i].numero_de_cartao)
	print('Credito do cliente:',Lista[i].Saldo)
	print()
	print('='*30)
	print('Digite 1 para alterar nome')
	print('Digite 2 para alterar sobrenome')
	print('='*30)
	print()
	modificacao=int(input('Digite a opcao desejada:'))
	if modificacao==1:
		novo_nome=input('Novo Nome:')
		Lista[i].nome=novo_nome
	elif modificacao==2:
		novo_sobrenome=input('Novo Sobrenome:')
		Lista[i].sobrenome=novo_sobrenome
	
	print()
	print()
	print('Nome:',Lista[i].nome)
	print('Sobrenome:',Lista[i].sobrenome)
	print('cpf:',Lista[i].cpf)
	print('Numero de cartao:',Lista[i].numero_de_cartao)
	print('Credito do cliente:',Lista[i].Saldo)
	print()




def alteraSaldo(Lista):
  print("1- para liberar mais credito na conta")
  print("1- para reduzir credito na conta")
  change=int(input("Opção: "))
  if change==1:
    novo_valor=int(input("Quer adicionar quanto: "))
    Lista[i].Saldo+novo_valor
    print("Credito liberado")
  if change==2:
    new_valor=int(input("Quer reduzir o saldo de quanto: "))
    Lista[i].Saldo-new_valor
    print("Credito reduzido")
    
def verifynumero(numero, Lista):
    for i in range(len(Lista)):
      if numero == Lista[i].numero_de_cartao:
        return False
      else:
        return True

def verifycpf(numero, Lista):
    for i in range(len(Lista)):
      if numero == Lista[i].cpf:
        return False
      else:
        return True

    
  


def exclui(Lista):
		Lista.remove(Lista[i])
		print()




def insere(Lista):
  print('='*30)
  print('Insere o cliente!')
  print('='*30)
  cad=tcadastro()
  cad.nome=input('Nome do cliente: ')
  cad.sobrenome=input('Sobrenome do cliente: ')
  cad.senha=int(input("cadastre uma senha, (um numero de 6 digitos)*: "))
  cad.cpf=input('cpf do cliente (com os pontos(.) ): ')
  while isCpfValid(cad.cpf) == False:
    print()
    print("O Cpf digitado não é valido")
    print("Por favor tente de novo")
    cad.cpf=input("Digite o cpf do cliente (com os pontos(.)): ")
  while verifycpf(cad.cpf, Lista) == False:
    print()
    print("Oupss! Esse Cpf já foi cadastrado no sistema")
    print("Por favor tente um outro")
    cad.cpf=input("Digite o cpf do cliente (com os pontos(.)): ")
    
  cad.numero_de_cartao=int(input('O numero do cartão: '))
  while verifynumero(cad.numero_de_cartao, Lista) == False:
    print()
    print("Oupss! Esse numero de cartão já existe no sistema")
    print("Por favor tente um outro")
    cad.numero_de_cartao=int(input('O numero do cartão: '))

  cad.Saldo=999999
  Lista.append(cad)
  print()
  print('O cliente foi adicionado no sistema com sucesso.')
  print()
  
  return Lista

#Criando as categorias para armazenar as compras do cliente
farmacia=0
compinter=0
mercado=0 
outras=0

op=1
while op !=0:
  print("="*45)
  print("--vvbank--")
  print("Digite 1 para se conectar como usuario root")
  print("Digite 2 para se conectar como simple usuario")
  print('Digite 3 para Sair ')
  print("="*45)
  primop=int(input("Sua opação: "))
  if primop ==1:
    print("="*36)
    sen=int(input("Digite a sua senha de acesso:"))
    print("="*36)
    print()
    print()
    if sen==senharoot:

      alp=0

      while alp==0:
        print("="*65)
        print("*"*13, "Bem vindo no sistema bancario CCBANK", "*"*14)
        print("="*65)
        print("Escolhe uma operação")
        print()
        print("Digite 1 para inserir novo cliente  ")
        print("Digite 2 para alterar  dados de cliente ")
        print("Digite 3 para excluir cliente  ")
        print("Digite 4 para listar cliente  ")
        print("Digite 5 para alerar credito de  cliente ")
        print("Digite 6 para sair  ")
        print()
        print("=*"*30)
        print()
        opcao=int(input("Digite uma opcao : "))
        
      
        if opcao==1:
          insere(lista)
          print()
        if opcao==2:
          cpf_buscar=input("Digite o cpf do cliente para alterar seus dados: ")

          for i in range(len(lista)):
            if cpf_buscar ==lista[i].cpf:
              print()
              altera(lista)
            else:
              print("Esse cpf nao existe no sistema ...! ")
              print()

        if opcao==2 and len(lista)==False:
          print('Infelizmente, nao temos cliente...!')
        
        if opcao==3:
          cpf_buscar=input("Digite um cpf para excluir o cliente ! ")
          for i in range(len(lista)):
            if cpf_buscar==lista[i].cpf:
              exclui(lista)
              print()
            else:
              print('Esse cpf não existe no sistema')
            
        if opcao==3 and (len(lista))==False:
          print('Infelizmente, nao temos cliente')

        if opcao==4:
          for i in range(len(lista)):
            print('Nome:',lista[i].nome)
            print('Sobrenome:',lista[i].sobrenome)
            print('cpf:',lista[i].cpf)
            print('Numero do cartão:',lista[i].numero_de_cartao)
            print('credito do cliente:',lista[i].Saldo)		
            print()	

        if opcao==4 and (len(lista))==False:
          print('Infelizmente, nao temos cliente')

        if opcao==5:
          cpf_buscar=input('Digite o cpf do cliente:')
          for i in range(len(lista)):
            if cpf_buscar==lista[i].cpf:
              alteraSaldo(lista)
            else:
              print('Esse cpf nao existe no sistema..!')
        if opcao==5 and (len(lista))==False:
          print('Infelizmente, nao temos cliente')
        print()
        
        if opcao==6:
          print("Obrigado..!")
          alp=1
          
        if opcao>6:
          print('Opa! não temos nada para a sua opção!')
          print()
    else:
      print('Senha incorreto, Obrigado por ter tentado')
      
    
  if primop==2:
    print("="*36)
    cpf_usuario=input("Seu cpf: ")
    senha_usuario=int(input("Sua senha de acesso: "))
    if len(lista) == False:
      print()
      print("Oupss!")
      print("Parece que você não foi cadastrado ainda.")
      print()
      print()


    for i in range(len(lista)):
          if cpf_usuario ==lista[i].cpf and senha_usuario ==lista[i].senha:
            print("")
            print("="*36)
            print("Bom dia", lista[i].nome)
            print("Seu limite de credito: ", lista[i].Saldo)
            print("="*36)
            print()
            print()
            
            pag=1
            while pag!=0:

              print("Digite 1 para fazer pagamento")
              print("Digite 2 para historico de compras")
              print("Digite 0 para sair")

              print()
              opcao=int(input("Escolhe uma opção por favor: "))

              if opcao==1:
                pag_usuario=int(input("Quer pagar quanto: "))
                if pag_usuario > lista[i].Saldo:
                  print("Opa..! Seu limite esta estourado você nao pode realizar esse pagamento ")
                else:
                  lista[i].Saldo =  lista[i].Saldo-pag_usuario
                  print()
                  print("Agora escolhe a categoria do seu pagamento")
                  print()
                  print("Digite 1 para Farmàcia")
                  print(" 2 para Supermercado")
                  print(" 3 para Compra Internacional")
                  print(" 4 para outras categorias")
                  print()
                  categ=int(input("Categoria: "))

                  if categ==1:
                    farmacia+=pag_usuario

                  if categ==2:
                    mercado+=pag_usuario
                  if categ==3:
                    compinter+=pag_usuario
                  if categ == 4:
                    outras+=pag_usuario
              if opcao==2:
                print("="*36)
                print("Você gastou: ")
                print()
                print("R$", farmacia, "Na categoria farmacia ")
                print("R$", mercado, "Na categoria Mercado ")
                print("R$", compinter, "Na categoria Compras internacional ")
                print("R$", outras, "Em outras categoria ")
                print()
                print()
              if opcao==0:
                print("Obrigado por ter usado nosso sistema!")
                print()
                pag=0
                

          else:
              print("Cpf ou senha digitado incorreto ...! ")
              print()


  if primop==3:
    print('Obrigado por ter usado nosso sistema..!')
    print("="*36)
    break
  else:

    if primop > 3 or primop <  3:
      
      print()
      #print("Essa opçao não existe, escolhe entre (1 - 2 e 3)")
