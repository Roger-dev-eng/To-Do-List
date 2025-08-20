lista = []

def adicionar_tarefa():
    add = input("\nEscreva a tarefa para adicionar: ")
    lista.append(add)
    print(f"\nTarefa '{add}' adicionada com êxito")

def listar_tarefa():
    if lista:
        print("\nSuas tarefas:")
        for i, tarefa in enumerate(lista, 1):
            print(f"{i}. {tarefa}")
    else:
        print("\nNenhuma tarefa")

def remover_tarefa():
    if lista:
      
      listar_tarefa()

      try:
        id = int(input("Digite o número da tarefa que deseja remover: "))
        if 1 <= id <= len(lista):
            removida = lista.pop(id - 1)
            print(f"Tarefa '{removida}' removida com sucesso")
        else:
            print("número inválido")
      except ValueError:
          print("Digite apenas números")
    else:
        print("\nLista vazia")
