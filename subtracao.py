#Atividade de criação de uma calculadora utilizando match/case

nome = input("Nome de usuário: ")

conta = input("Defina se quer: + somar,  - subtrair, * multiplicar ou / dividir: ")
#solicitando os valores para o cálculo.
valor1 = float(input("Digite o primeiro número: "))
valor2 = float(input("Digite o segundo número: "))

#Calculando a operação escolhida
match conta:
    case "subtracao" | "Subtracao" | "SUBTRACAO" | "":
        print(f"O resultado da subtração entre {valor1} e {valor2} é: {valor1 - valor2}")




