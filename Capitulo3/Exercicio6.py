# 01 de julho de 2025
# Terça-feira, madrugada fria

mais_convidados = """\nVocê acabou de encontrar uma mesa de jantar maior,
portanto agora tem mais espaço disponível. Pense em mais três convidados
para o jantar.
* Comece com seu programa do Exercíco 3.4 ou do Exercício 3.5. Acrescente
uma instrução print no final de seu programa informando às pessoas que 
você encontrou uma mesa de jantar maior.
* Utilize insert() para adicionar um novo convidado no início de sua lista.
* Utilize insert() para adicionar um novo convidado no meio de sua lista.
* Utilize append() para adicionar um novo convidado no final de sua lista.
* Exiba um conjunto de mensagens de convite, uma p ara cada pessoa que está 
em sua lista."""


convidados = ['Elvira', 'Diana', 'Nico Robin']

print(mais_convidados)

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