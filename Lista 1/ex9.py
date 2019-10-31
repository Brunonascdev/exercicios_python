#Exercício 9: Escreva um programa que leia dois números inteiros,
#sendo armazenados respectivamente nas variáveis A e B.
#O programa deverá inverter os valores entre as variáveis,
#de modo que o valor da variável A seja atribuído na
#variável B e vice-versa. Ao final exibir os valores de cada variável.

a = int(input("Insira o primeiro valor: "))
b = int(input("Insira o segundo valor: "))

aux = a
a = b
b = aux

print(f"A primeira variavel é igual a {a:.2f}")
print(f"A segunda variavel é igual a {b:.2f}")

