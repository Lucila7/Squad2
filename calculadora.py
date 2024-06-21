#Atividade de criação de uma calculadora utilizando match/case

nome = input("Nome de usuário: ")
conta = input("Defina se quer: + somar,  - subtrair, * multiplicar ou / dividir: ")
valor1 = float(input("Número 1: "))
valor2 = float(input("Número 2: "))

#Calculando a operação escolhida
match conta:
    case '+' | 'somar' :
        print(f'{nome}, a soma dos valores {valor1} e {valor2}:')
        print(valor1 + valor2)
