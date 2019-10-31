#Exercício 7: Escreva um programa que leia o nome de duas pessoas e ao final
#exiba: 
#•	O nome das duas pessoas com todos os caracteres maiúsculos 
#•	A quantidade de caracteres de cada nome 
#•	Apenas os três primeiros caracteres de cada nome 

nomeUm = str(input("Insira o primeiro nome: "))
nomeDois = str(input("Insira o segundo nome: "))

print(nomeUm.upper())
print(nomeDois.upper())

print(len(nomeUm))
print(len(nomeDois))


print(nomeUm[0:3])
print(nomeDois[0:3])
