doacoes = []

def registrar_doacao():
    print('--- Registrar Nova Doação ---')
    nome = input('nome do doador: ')
    tipo = input('tipo de doação (alimento, roupa, brinquedo, etc.): ')
    try:
        quantidade = int(input('Quantidade:'))
    except ValueError:
        print('Quantidade inválida!❌🥵 Registro cancelado.')
        return
    data = input('Data da doação (ex: 14/05/2025): ')
    entregue = input('A doação já foi entregue? (s/n): ').lower() == 's'

    doacao = {
        'id': len(doacoes) + 1,
        'doador': nome,
        'tipo': tipo,
        'quantidade': quantidade,
        'data': data,
        'entregue': entregue
    }

    doacoes.append(doacao)
    print('✅ Doação registrada com sucesso!✅👌😎')

def ver_todas_doacoes():
    print('--- lista de Todas as Doações ---')
    if not doacoes:
        print('nenhuma doação registrada.')
        return
    for d in doacoes:
        print(f"ID: {d['id']} | Doador: {d['doador']} | Tipo: {d['tipo']} | Qtd: {d['quantidade']} | Data: {d['data']} | Entregue: {'Sim' if d['entregue'] else 'Não'}")

def consultar_por_tipo():
    print('--- consultar Doações por Tipo ---')
    tipo = input('digite o tipo de doação que deseja consultar: ').lower()
    filtradas = [d for d in doacoes if d['tipo'].lower() == tipo]
    if not filtradas:
        print(f'Nenhuma doação do tipo "{tipo}" encontrada.')
        return
    for d in filtradas:
        print(f"ID: {d['id']} | Doador: {d['doador']} | Qtd: {d['quantidade']} | Data: {d['data']} | Entregue: {'Sim' if d['entregue'] else 'Não'}")

def marcar_como_entregue():
    print('\n--- Marcar Doação como Entregue ---')
    try:
        id_busca = int(input('Digite o ID da doação que foi entregue: '))
        for d in doacoes:
            if d['id'] == id_busca:
                d['entregue'] = True
                print('✅ Doação marcada como entregue!')
                return
        print('ID não encontrado.')
    except ValueError:
        print('ID inválido.')

def menu():
    while True:
        print('===== Sistema de Sessões de doaçoes =====')
        print('1. registrar doacao')
        print('2. ver todas doacoes ')
        print('3. consultar por tipo')
        print('4. marcar como entregue')
        print('5. menu')
        escolha= str(input('escolha uma opção'))
        if escolha=='1':
            registrar_doacao()
        elif escolha=='2':
            ver_todas_doacoes()
        elif escolha=='3':
            consultar_por_tipo()
        elif escolha=='4':
            marcar_como_entregue()
        elif escolha=='5':
            menu()
            break
        else:
            print('❌opção invalida. tente novamente🥵😒.')
menu()