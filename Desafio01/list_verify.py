def verify():
    from src import people_list

    lista = people_list.People
    nova_lista = []

    cont = cont_nome = p = 0

    for i in lista:
        if "nome" in i:
            if i["nome"] not in nova_lista:
                nova_lista.append(i["nome"])
            else:
                cont_nome += 1
        else:
            cont += 1

    print('-' * 60)
    print(f'{"Lista de nomes":^60}')
    print('-' * 60)

    if len(nova_lista) > 0:
        for j in nova_lista:
            print(f'Nome {p+1}: {j}')
            p += 1

    print('-' * 60)
    print(f'{"Relatório":^60}')
    print('-' * 60)

    print(f'{cont} registro(s) estava(m) sem o campo nome.')
    print(f'Houve {cont_nome} registro(s) com o valor do campo nome repedido(s).')
