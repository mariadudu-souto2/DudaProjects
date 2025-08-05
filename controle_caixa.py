caixa = 0.0
historico = []

def entrada(valor):
    global caixa
    caixa += valor
    historico.append(f"Entrada: +R$ {valor:.2f}")

def saida(valor):
    global caixa
    caixa -= valor
    historico.append(f"Saída: -R$ {valor:.2f}")

def mostrar_caixa():
    print(f"\nSaldo atual: R$ {caixa:.2f}")

def mostrar_historico():
    print("\nHistórico de movimentações:")
    for mov in historico:
        print("-", mov)

def main():
    print("Sistema simples de Controle de Caixa")
    while True:
        print("\nEscolha uma opção:")
        print("1 - Entrada")
        print("2 - Saída")
        print("3 - Mostrar saldo")
        print("4 - Mostrar histórico")
        print("0 - Sair")

        opcao = input("Opção: ")
        if opcao == '0':
            break
        elif opcao == '1':
            try:
                val = float(input("Valor da entrada: R$ "))
                entrada(val)
            except ValueError:
                print("Valor inválido!")
        elif opcao == '2':
            try:
                val = float(input("Valor da saída: R$ "))
                saida(val)
            except ValueError:
                print("Valor inválido!")
        elif opcao == '3':
            mostrar_caixa()
        elif opcao == '4':
            mostrar_historico()
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()