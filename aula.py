sessoes=[]
def cadastrar_sessoes():
    tema=str(input('entre com o tema da sessão: '))
    dia=str(input('digite qual o dia da sessão: '))
    responsavel=str(input('quem sera o responsavel: '))
    sessao= {
        'tema':tema,
        'dia':dia,
        'responsavel':responsavel,
         'realizada':False
    }
    sessoes.append(sessao)
    print('🙄sua sessao foi cadastrada com sucesso!🙄\n')

def consultar_sessoes():
    if len(sessoes)==0:
        print('nenhuma sessao foi cadastrada \n')
        return
    numero=1
    for sessao in sessoes:
        status= ' '
        if sessao['realizada']==True:
            status=['realizada']
        else:
            status='nao realizada'
        print(f"[{numero}] tema: {sessao['tema']} | dia: {sessao['dia']} ,"
              f" responsavel: {sessao['responsavel']} | status: {status}")
        numero+=1
    print()

def buscar_sessoes():
    termo=str(input('buscar por termo ou dia da semana: ')).lower()
    encontrado=[]
    for sessao in sessoes:
        if(termo in sessao['tema'].lower()) or (termo in sessao['dia'].lower()):
            encontrado.append(sessao)
    if len(encontrado)==0:
        print('nenhuma sessao foi cadastrada \n')
        return
    numero=1
    for sessao in encontrado:
        status= ' '
        if sessao['realizada']==True:
            status=['realizada']
        else:
            status='nao realizada'
        print(f"[{numero}] tema: {sessao['tema']} | dia: {sessao['dia']} ,"
              f" responsavel: {sessao['responsavel']} | status: {status}")
        numero+=1
    print()

def marcar_realizada():
    consultar_sessoes()
    if len(sessoes)==0:
        return
    try:
        numero=int(input('digite o numero do sessao para marcar como realizada: '))
        indice= numero-1

        if numero <= len(sessoes):
            sessoes[indice]["realizada"]= True
            print('sessao marcada como realizada \n')
        else:
            print('numero invalido.\n')
    except ValueError:
     print('entrada errada digite um numero.\n')

def exibir_menu():
    while True:
        print('=== sistema de sessoes de estudos ===')
        print('1 - cadastrar sessoes')
        print('2 - consultar sessoes')
        print('3 - buscar sessoes')
        print('4 - marcar realizada')
        print('5 - sair')

        escolha=str(input('escolha uma opçao'))
        if escolha == '1':
            cadastrar_sessoes()

        elif escolha == '2':
            consultar_sessoes()

        elif escolha == '3':
            buscar_sessoes()

        elif escolha == '4':
            marcar_realizada()

        elif escolha == '5':
            print('saindo do sistema ate a proxima')
            break
        else:
            print('opçao invalida. tente novamente. \n')

exibir_menu()