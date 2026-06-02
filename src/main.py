
import os
os.system ("cls")
from crud import adicionar_animal, animais, visualizar_animal, editar_animal, excluir_animal

def adicionar_animal(nome_chave, info):
    animais[nome_chave]=info  
    print("animal adicionado com sucesso" )

def visualizar_animal(nome):
    if nome_chave in animais:
        print(f"{nome_chave}: {animais[nome_chave]}")
    else:
        print("animal inválido")

def editar_animal():
    nome_editar=input("digite o nome do animal que deseja editar: ")
    if nome_editar in animais:
        print(f"Dados atuais: {animais[nome_editar]}")
        print("oque deseja editar ? ")
        print("[1]- nome")
        print("[2]-espécie")
        print("[3]- raça")
        print("[4]- idade")
        print("[5]- estado de saúde")
        print("[6]- comportamento")
        print("[7]- data de chegada ")

        campo=input("digite o número do campo: ")
        campos={"1": "nome",
                "2": "espécie",
                "3": "raça",
                "4": "idade",
                "5": "estado de saúde",
                "6": "comportamento",
                "7": "data de chegada",
                
                }
        if campo in campos:
         chave_campo= campos[campo]
         novo_valor=input(f"digite a nova informação para {chave_campo}:  ")

        animais[nome_editar][chave_campo]=novo_valor
        print((f"campo {chave_campo} atualizado com sucesso!"))
          


def excluir_animal():
    nome_excluir=input("digite o nome do animal que deseja excluir: ")
    if nome_excluir in animais:
       return animais.pop(nome_excluir)


    

while True:
    print("=====FUNÇÕES=====")
    print("[1]- adicionar animal")
    print("[2]- visualizar")
    print("[3]- editar")
    print("[4]- excluir")
    print("[5]- sair")


    funcao=int(input("\ndigite um número equivalente a uma função: "))
   
    if funcao == 1 :
      nome_chave=input("\ndigite o nome do animal: ")

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
        nome=input("\nescolha o nome que deseja visualizar: ")

        nome=input("escolha o nome que deseja visualizar: ")

        nome=input("escolha o nome que deseja visualizar: ")

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



print("=====cadastro=======")
