from crud import adicionar_animal, animais, visualizar_animal, editar_animal, excluir_animal

while True:
    print("=====FUNÇÕES=====")
    print("[1]- adicionar animal")
    print("[2]- visualizar")
    print("[3]- editar")
    print("[4]- excluir")
    print("[5]- sair")

    funcao=int(input("digite um número equivalente a uma função: "))
   
    if funcao == 1 :
      nome_chave=input("digite o nome do animal: ")

      info={
          "espécie": input("Espécie: "),
            "raça": input("Raça: "),
            "idade": input("Idade: "),
            "estado de saúde": input("Estado de saúde: "),
            "comportamento": input("Comportamento: "),
            "data de chegada": input("Data de chegada: ")
        }
      adicionar_animal(nome_chave,info)


    elif funcao == 2:
        nome=input("escolha o nome que deseja visualizar: ")
        visualizar_animal(nome)
    elif funcao == 3:
        editar_animal()
    elif funcao == 4:
        excluir_animal()
    elif funcao == 5:
        print("você saiu !")
        break
    else:
        print("função inválida")

