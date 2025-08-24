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

def adicionar_tarefa(add):
    lista = carregar_tarefas()
    lista.append({"descricao": add, "status": False})
    salvar_tarefa(lista)
    print(f"\nTarefa '{add}' adicionada com êxito")  

def listar_tarefa():
    lista = carregar_tarefas()
    print(f"\nVocê tem {len(lista)} tarefa(s)")
    if lista:
        for i, tarefa in enumerate(lista, 1):
            status = "✅" if tarefa["status"] else "❌"
            print(f"{i}. {tarefa['descricao']} [{status}]")
    else:
        print("Nenhuma tarefa")

def concluir_tarefa(indice):
    lista = carregar_tarefas()
    if 1 <= indice <= len(lista):
        lista [indice - 1]["status"] = True
        salvar_tarefa(lista)
        print(f"Tarefa '{lista[indice - 1]['descricao']}' marcada como concluída")
    else:
        print("Número inválido")    

def remover_tarefa(indice):
    lista = carregar_tarefas()
    if lista:
      listar_tarefa()
      if 1 <= indice <= len(lista):
          removida = lista.pop(indice - 1)
          salvar_tarefa(lista)
          print(f"Tarefa '{removida['descricao']}' removida com sucesso")
      else:
          print("número inválido")
    else:
        print("\nLista vazia")
