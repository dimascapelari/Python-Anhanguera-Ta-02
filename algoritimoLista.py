# Forma simples
lista = [7, 4]

if lista[0] > lista[1]:
    aux = lista[1]
    lista[1] = lista[0]
    lista[0] = aux

print(lista)


# Recurso de atribuição composta do Python
lista2 = [5, -1]

if lista2[0] > lista2[1]:
    lista2[0], lista2[1] = lista2[1], lista2[0]

print(lista2)
