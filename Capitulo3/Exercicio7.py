# 01 de julho de 2025
# Terça-feira, madrugada fria

reduzindo_lista = """\n3.7 - Reduzindo a lista de convidados: Você acabou de descobrir que sua nova 
mesa de jantar não chegará a tempo para o jantar e tem espaço para somente
dois convidados.
* Comece com seu programa do Exercício 3.6. Acrescente uma nova linha que
mostre uma mensagem informando que você pode convidar apenas duas pessoas 
para o jantar.
* Utilize pop() para remover os convidados de sua lista, um de cada vez, até
que apenas dois nomes permaneçam em usa lista. Sempre que remover um 
nome de sua lista, mostre uma mensagem a essa pessoa, permitindo que ela
saiba que você sente muito por não poder convidá-la para o jantar.
* Apresente uma mensagem para cada uma das duas pessoas que continuam
na lista, permitindo que elas saibam que ainda estão convidadas.
* Utilize del para remover os dois últimos nomes de sua lista,de modo que você
tenha uma lista vazia. Mostre sua lista para garantir que você realmente tem
uma lista vazia no final de deu programa."""

print(reduzindo_lista)

convidados = ['Elvira', 'Diana', 'Nico Robin']

print("\nInserindo um convidado no início da lista:")
convidados.insert(0, 'Srta Nami')
print("Inserindo um convidado no meio da lista:")
convidados.insert(2, 'Beth')
print("Inserindo um convidado no final da lista:")
convidados.append("Vilma")
print(convidados)

print("\n")
print(convidados[0], ", você está convidada para um jantar!")
print(convidados[1], ", você está convidada para um jantar!")
print(convidados[2], ", você está convidada para um jantar!")
print(convidados[3], ", você está convidada para um jantar!")
print(convidados[4], ", você está convidada para um jantar!")
print(convidados[5], ", você está convidada para um jantar!")

print("\n")

print("Por motivos alheios a minha vontade, poderei convidar apenas duas pessoa para o jantar.")
print(convidados[5] + ", sinto informá-la que terei que adiar nosso jantar.")
convidados.pop()
print(convidados)

print("\n")
print(convidados[4] + ", sinto informá-la que terei que adiar nosso jantar.")
convidados.pop()
print(convidados)

print("\n")
print(convidados[3] + ", sinto informá-la que terei que adiar nosso jantar.")
convidados.pop()
print(convidados)

print("\n")
print(convidados[2] + ", sinto informá-la que terei que adiar nosso jantar.")
convidados.pop()
print(convidados)

print("\n")
print(convidados[0] + ", nosso jantar está confirmado para a próxima sexta-feira.")
print(convidados[1] + ", nosso jantar está confirmado para a próxima sexta-feira.")

print("\n")
print("Excluindo o primeiro ítem.")
del convidados[0]
print(convidados)
print("Excluindo o segundo ítem.")
del convidados[0]
print(convidados)
print("Lista final vazia.")
print(convidados)




