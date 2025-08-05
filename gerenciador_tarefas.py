tarefas = []

def adicionar_tarefa(tarefa):
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada.")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("Tarefas:")
        for i, t in enumerate(tarefas, 1):
            print(f"{i}. {t}")

def remover_tarefa(numero):
    if 1 <= numero <= len(tarefas):
        removida = tarefas.pop(numero - 1)
        print(f"Tarefa '{removida}' removida.")
    else:
        print("Número inválido.")

def main():
    print("Gerenciador simples de Tarefas")
    while True:
        print("\nMenu:")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Remover tarefa")
        print("0 - Sair")

        opcao = input("Opção: ")
        if opcao == '0':
            break
        elif opcao == '1':
            tarefa = input("Descrição da tarefa: ")
            adicionar_tarefa(tarefa)
        elif opcao == '2':
            listar_tarefas()
        elif opcao == '3':
            try:
                num = int(input("Número da tarefa a remover: "))
                remover_tarefa(num)
            except ValueError:
                print("Digite um número válido!")
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()