# Exercício 6: Escreva um programa que leia um valor em Reais (R$),
# leia também a cotação do Dólar, realize o cálculo da conversão de moeda
# (de Reais para Dólares) e exiba na tela o resultado.

reais = float(input("Insira a quantidade em reais para saber sua quantia em dólares: "))
cotacao = float(input("Insira a cotação atual do dólar: "))
result = reais / cotacao

print(f"Este valor em dólares, na cotação atual, é: {result:.2f}")
