teste_lista = ["Dimas", "Mariana", "Maria Luiza", "Meggie"]


def executar_busca_binaria(lista, valor):
    minimo = 0
    maximo = len(lista) - 1

    while minimo <= maximo:
        # Encontra o elemento que divide a lista ao meio
        meio = (minimo + maximo) // 2
        # Verifica se o valor procurado está a esquerda ou direita do valor central
        if valor < lista[meio]:
            maximo = meio - 1
        elif valor > lista[meio]:
            minimo = meio + 1
        else:
            return True  # Se o valor dor encontrado para aqui

    return False  # Se chegar até aqui, siginifica que o valor não foi encontrado


print(executar_busca_binaria(teste_lista, 'Dimas'))
