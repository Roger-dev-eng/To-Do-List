import json
import os

Tarefas = "tarefas.json"

def carregar_tarefas():
    if os.path.exists(Tarefas):
        with open(Tarefas, "r", encoding="utf-8") as f:
            return json.load(f)
    return[]
    
def salvar_tarefa(lista):
    with open(Tarefas, "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)

def adicionar_tarefa():
    lista = carregar_tarefas()
    add = input("\nEscreva a tarefa para adicionar: ")
    lista.append(add)
    salvar_tarefa(lista)
    print(f"\nTarefa '{add}' adicionada com êxito")  

def listar_tarefa():
    lista = carregar_tarefas()
    if lista:
        print("\nSuas tarefas:")
        for i, tarefa in enumerate(lista, 1):
            print(f"{i}. {tarefa}")
    else:
        print("\nNenhuma tarefa")

def remover_tarefa():
    lista = carregar_tarefas()
    if lista:
      listar_tarefa()
      try:
        id = int(input("Digite o número da tarefa que deseja remover: "))
        if 1 <= id <= len(lista):
            removida = lista.pop(id - 1)
            salvar_tarefa(lista)
            print(f"Tarefa '{removida}' removida com sucesso")
        else:
            print("número inválido")
      except ValueError:
          print("Digite apenas números")
    else:
        print("\nLista vazia")
