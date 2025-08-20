lista = []

def adicionar_tarefa():
    add = input("Escreva a tarefa para adicionar: ")
    add.append(lista)
    print(f"Trefa ,{add}, adicionada com êxito")

def listar_tarefa():
    if lista:
        print("\nSuas tarefas:")
        for i, tarefa in enumerate(lista, 1):
            print(f"{i}. {tarefa}")
    else:
        print("Nenhuma tarefa")

def remover_tarefa():
    listar_tarefa()




