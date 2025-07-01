# 29 de junho de 2025
# Domingo, noite fria

lista = """\nVocê acabou de saber que um de seus convidados não poderá 
comparecer ao jantar, portanto será necessário enviar um novo conjunto
 de convites. Você deverá pensar em outra pessoa para convidar.
 * Comece com seu programa do Exercício 3.4 Acrescente uma instrução print
 no final de seu programa, especificando o nome do convidade que não
 poderá comparecer.
 * Modifique sua lista, substituindo o nome de convidado que não poderá
 comparecer pelo nome da nova pessoa que você está convidando.
 * Exiba um segundo conjunto de mensagens com o convite, uma para cada
 pessoa que continua presente em sua lista."""

print(lista)

convidados = ['Elvira', 'Diana', 'Nico Robin']
print(convidados)

print("\n")
print(convidados[0] + ", convido você para um jantar hoje a noite!")
print(convidados[1] + ", convido você para um jantar hoje a noite!")
print(convidados[2] + ", convido você para um jantar hoje a noite!")

print(convidados[2] + ", por incompatibilidade de agenda, não poderá comparecer ao nosso jantar.")

print("\nNova lista de convidados:")
novo_convidado = convidados.append('Srta Nani')
print(convidados[0] + ", convido você para um jantar hoje a noite!")
print(convidados[1] + ", convido você para um jantar hoje a noite!")
print(convidados[3] + ", convido você para um jantar hoje a noite!")
print("\n")
