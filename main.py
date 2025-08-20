from lista import adicionar_tarefa, listar_tarefa, remover_tarefa

while True:
  print("---LISTA DE AFAZERES---")
  print("1 = Adicionar tarefa")
  print(" 2 = Listar tarefas")
  print("3 = Remover tarefa")
  print("4 = Sair")
  escolha = input(int("Digite um número (1-4): "))
  if escolha == 1:
    adicionar_tarefa()
  elif escolha == 2:
    listar_tarefa()
  elif escolha == 3:
    remover_tarefa()
  elif escolha == 4:
    break
  else:
    print("Opção inválida. Tente novamente")