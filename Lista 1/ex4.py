# Exercício 4: Escreva um programa que calcule e exiba o resultado da seguinte
# expressão matemática: (Dica: O usuário deverá informar os valores para
# as variáveis A, B e C) 
# A² * 5 – C / (B – A % 4)

print("Resolver a equação: A² * 5 – C / (B – A % 4)")

a = int(input("Insira o valor de A: "))
b = int(input("Insira o valor de B: "))
c = int(input("Insira o valor de C: "))

result = a ** 2 * 5 - c / (b - a % 4)

print(result)
