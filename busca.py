vogais = 'aeiou'
resultado = vogais.index('e')
print(resultado)


# -------------------------------

teste_lista = ["Dimas", "Mariana", "Maria Luiza"]


def executar_busca_linear(lista, valor):
    for elemento in lista:
        if valor == elemento:
            return True
        return False


print(executar_busca_linear(teste_lista, 'Dimas'))
