# 01 de julho de 2025
# Terça-feira, noite fria

conhecendo = """\n3.8 - Conhecendo o mundo: Pense em pleo menos cinco lugares do mundo que
você gostaria de visitar.
1 -  Armazene as localidades em uma lista. Certifique-se de que a lista não esteja
em ordem alfabética.
2 - Utilize sorted() para exibir sua lista em ordem alfabética, sem modificar a
lista propriamente dita.
3 - Mostre que sua lista manteve sua ordem original exibindo-a.
4 - Utilize reverse() par amudar a ordem de sua lista. Exiba a lista para mostrar
que sua ordem mudou.
5 - Utilize reverse()  para mudar a ordem de sua lista novamente. Exiba a lista
para mostar que ela voltou à sua ordem original.
6 - Utilize sort() para mudar sua lista de modo que ela seja armazenada em 
ordem alfabética. Exiba a lista para mostrar que sua ordem mudou.
7 - Utilize sort() para mudar sua lista de modo que ela seja armazenada em
ordem alfabética inversa. Exiba a lista para mostrar que sua ordem mudou.
"""

lugares = ['índia', 'namíbia', 'amazônia', 'istambul', 'china']

print(conhecendo)

print("\nExibindo a lista em ordem alfabética:")
print(sorted(lugares))
print("Exibindo a lista original:")
print(lugares)
print("Exibindo a lista em ordem inversa:")
lugares.reverse()
print(lugares)
print("Restaurando a ordem da lista:")
lugares.reverse()
print(lugares)
print("Exibindo a lista em ordem alfabética:")
lugares.sort()
print(lugares)
print("Exibindo a lista com a ordem modificada:")
print(lugares)
print("Exibindo a lista em ordem inversa:")
lugares.sort(reverse=True)
print(lugares)
