def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

def main():
    print("Calculadora simples")
    while True:
        print("\nEscolha a operação:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("0 - Sair")

        opcao = input("Opção: ")
        if opcao == '0':
            break
        if opcao not in ['1','2','3','4']:
            print("Opção inválida!")
            continue

        try:
            x = float(input("Digite o primeiro número: "))
            y = float(input("Digite o segundo número: "))
        except ValueError:
            print("Digite um número válido!")
            continue

        if opcao == '1':
            print("Resultado:", soma(x, y))
        elif opcao == '2':
            print("Resultado:", subtrai(x, y))
        elif opcao == '3':
            print("Resultado:", multiplica(x, y))
        elif opcao == '4':
            print("Resultado:", divide(x, y))

if __name__ == "__main__":
    main()