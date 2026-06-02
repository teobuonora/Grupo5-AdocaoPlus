animais={}

def adicionar_animal(nome_chave, info):

    animais[nome_chave]=info  
    print("\nAnimal adicionado com sucesso" )


    if nome_chave in animais:
        print("Esse animal já está cadastrado!")
        return

    animais[nome_chave] = info
    print("animal adicionado com sucesso")

def visualizar_animal(nome_chave):

    if nome_chave in animais:

        print(f"\nNome: {nome_chave}")

        for chave, valor in animais[nome_chave].items():
            print(f"{chave}: {valor}")

    else:
        print("Animal inválido")

def editar_animal():
    nome_editar = input("digite o nome do animal que deseja editar: ")


    nome_editar=input("Digite o nome do animal que deseja editar: ")

    if nome_editar in animais:

        print(f"Dados atuais: {animais[nome_editar]}")


        print("o que deseja editar?")

        print("O que deseja editar ? ")

        print("[1]- nome")
        print("[2]- espécie")
        print("[3]- raça")
        print("[4]- idade")
        print("[5]- estado de saúde")
        print("[6]- comportamento")
        print("[7]- data de chegada")

        campo = input("digite o número do campo: ")

        campo=input("Digite o número do campo: ")
        campos={"1": "Nome",
                "2": "Espécie",
                "3": "Raça",
                "4": "idade",
                "5": "estado de saúde",
                "6": "comportamento",
                "7": "data de chegada",
                
                }
        if campo in campos:
         chave_campo= campos[campo]
         novo_valor=input(f"digite a nova informação para {chave_campo}:  ")


        campos = {
            "2": "espécie",
            "3": "raça",
            "4": "idade",
            "5": "estado de saúde",
            "6": "comportamento",
            "7": "data de chegada"
        }

        if campo == "1":
            novo_nome = input("Digite o novo nome: ")

            if novo_nome in animais:
                print("Já existe um animal com esse nome!")
            else:
                animais[novo_nome] = animais.pop(nome_editar)
                print("Nome atualizado com sucesso!")
            

        elif campo in campos:

            chave_campo = campos[campo]

            novo_valor = input(
                f"Digite a nova informação para {chave_campo}: "
            )

            animais[nome_editar][chave_campo] = novo_valor

            print(
                f"Campo {chave_campo} atualizado com sucesso!"
            )

        else:
            print("Campo inválido!")

    else:
        print("Animal não encontrado!")


def excluir_animal():
    nome_excluir=input("digite o nome do animal que deseja excluir: ")
    if nome_excluir in animais:
        animais.pop(nome_excluir)
        print("animal excluído com sucesso")
    else:
        print("animal não encontrado")
    
    

while True:
    print("=====FUNÇÕES=====")
    print("[1]- adicionar animal")
    print("[2]- visualizar")
    print("[3]- editar")
    print("[4]- excluir")
    print("[5]- sair")

    try:
        funcao = int(input("digite um número equivalente a uma função: "))
    except ValueError:
        print("Digite apenas números!")
        continue
   
    if funcao == 1 :
      nome_chave=input("digite o nome do animal: ")

      info={
          "espécie": input("Espécie: "),
            "raça": input("Raça: "),
            "idade": int(input("Idade: ")),
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
