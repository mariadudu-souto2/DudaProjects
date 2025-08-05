def media(valores):
    return sum(valores) / len(valores) if valores else 0

def minimo(valores):
    return min(valores) if valores else None

def maximo(valores):
    return max(valores) if valores else None

def main():
    print("Analisador simples de dados")
    valores = []

    while True:
        entrada = input("Digite um número (ou 'sair' para encerrar): ")
        if entrada.lower() == 'sair':
            break
        try:
            num = float(entrada)
            valores.append(num)
        except ValueError:
            print("Número inválido, tente novamente.")

    if valores:
        print(f"Média: {media(valores):.2f}")
        print(f"Mínimo: {minimo(valores)}")
        print(f"Máximo: {maximo(valores)}")
    else:
        print("Nenhum dado fornecido.")

if __name__ == "__main__":
    main()