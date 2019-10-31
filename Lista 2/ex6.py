#Exercício 6: Escreva um programa que calcule e exiba a média
#de 10 notas digitadas pelo usuário. Considerar notas válidas,
#somente valores entre 0 (zero) e 10 (dez). Se o usuário digitar
#algum valor inválido, deverá ser exibida uma mensagem informando o ocorrido.

media = 0

for i in range(1, 11):
    notas = float(input("Digite a {0}º nota: ".format(i)))
    if notas > 10:
        print("Digite uma nota válida!")
    elif notas < 0:
        print("Digite uma nota válida!")
    else:
        media = media + notas

resultado = media / 10
print(resultado)
                        
