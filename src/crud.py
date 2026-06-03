animais={}

def adicionar_animal(nome_chave, info):
    animais[nome_chave]=info  
    print("\nAnimal adicionado com sucesso" )

def visualizar_animal(nome_chave):
    if nome_chave in animais:
        print(f"{nome_chave}: {animais[nome_chave]}")
    else:
        print("Animal inválido")

def editar_animal():
    nome_editar=input("Digite o nome do animal que deseja editar: ")
    if nome_editar in animais:
        print(f"Dados atuais: {animais[nome_editar]}")
        print("O que deseja editar ? ")
        print("[1]- nome")
        print("[2]-espécie")
        print("[3]- raça")
        print("[4]- idade")
        print("[5]- estado de saúde")
        print("[6]- comportamento")
        print("[7]- data de chegada ")

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

        animais[nome_editar][chave_campo]=novo_valor
        print((f"campo {chave_campo} atualizado com sucesso!"))
          


def excluir_animal():
    nome_excluir=input("digite o nome do animal que deseja excluir: ")
    if nome_excluir in animais:
       return animais.pop(nome_excluir)
    
    
