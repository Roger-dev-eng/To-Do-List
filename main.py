from lista import adicionar_tarefa, listar_tarefa, remover_tarefa, concluir_tarefa

while True:
  try:
    print("\n---LISTA DE AFAZERES---")
    print("1 = Adicionar tarefa")
    print("2 = Listar tarefas")
    print("3 = Remover tarefa")
    print("4 = Concluir tarefa")
    print("5 = Sair")
    escolha = int(input("Digite um número (1-5): "))
    if escolha == 1:
      add = input("\nEscreva a tarefa para adicionar: ")
      adicionar_tarefa(add)
    elif escolha == 2:
      listar_tarefa()
    elif escolha == 3:
      listar_tarefa()
      indice = int(input("Digite o número da tarefa que deseja remover: "))
      ESCOLHA = input("Tem certeza que deseja remover? (s/n) ")
      if ESCOLHA == "s":
        remover_tarefa(indice)
    elif escolha ==4:
      listar_tarefa()
      indice = int(input("Digite o número da tarefa que deseja concluir: "))
      concluir_tarefa(indice)
    elif escolha == 5:
      break
    else:
      print("Opção inválida. Tente novamente")
  except ValueError:
    print("\nDigite apenas números!")  