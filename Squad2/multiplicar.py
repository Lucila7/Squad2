multiplicar = input("Defina se quer: + somar,  - subtrair, * multiplicar ou / dividir: ")
valor1 = float(input("Número 1: "))
valor2 = float(input("Número 2: "))

match multiplicar:
    case 'multiplicar':
        print(f'{valor1} * {valor2}')
        print(valor1 + valor2)