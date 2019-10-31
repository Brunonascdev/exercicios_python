#Exercício 8: Escreva um programa que leia um valor em Reais (R$), leia também
#a cotação do Dólar e do Euro,
#realize o cálculo das respectivas conversões de
#moedas (de Reais para Dólares e de Reais para Euros)
#e exiba os resultados na tela.

valReais = float(input("Escreva a quantia em reais: "))
valDolar = float(input("Escreva a cotação atual do dólar: "))
valEuro = float(input("Escreva a cotação atual do euro: "))

resultDol = valReais / valDolar
resultEur = valReais / valEuro

print(f"Esse valor de reais convertido para dólares resulta em: {resultDol:.2f}")
print(f"Esse valor de reais convertido para euro resulta em: {resultEur:.2f}")
      

                 
