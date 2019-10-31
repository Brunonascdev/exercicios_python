#Exercício 8: Escreva um programa que calcule o fatorial de um número informado
#pelo usuário. Dica: O fatorial de um número N é dado pela fórmula:
#N! = 1 * 2 * 3 * 4 * 5 * ... * N

#num = int(input("Insira um número para saber seu fatorial: "))

#for i in reversed(range(1, num)):

def main():
    n = int(input("Digite o valor de n: "))
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1

    print("O valor de %d! é" %n, fat)

#-----
main()

    
    


