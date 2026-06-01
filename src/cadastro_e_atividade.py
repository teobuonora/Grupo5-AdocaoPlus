from crud import animais
from datetime import datetime
TIPOS_TAREFA = ["vacina", "banho", "consulta veterinária", "treino", "outro"]
 
 
def cadastrar_cuidado(animais):
    nome = input("Nome do animal: ")
    if nome not in animais:
        print("Animal não encontrado.")
        return
 
    print("Tipos de tarefa:")
    print("  [1] vacina")
    print("  [2] banho")
    print("  [3] consulta veterinária")
    print("  [4] treino")
    print("  [5] outro")
 
    opcao = input("Escolha o tipo: ")
    if opcao == "1":
        tipo = "vacina"
    elif opcao == "2":
        tipo = "banho"
    elif opcao == "3":
        tipo = "consulta veterinária"
    elif opcao == "4":
        tipo = "treino"
    elif opcao == "5":
        tipo = "outro"
    else:
        print("Opção inválida.")
        return
 
    
    data_prev   = input("Data prevista (DD/MM/AAAA): ")
    responsavel = input("Responsável: ")
 
    
    partes = data_prev.split("/")
    if len(partes) != 3 or not partes[0].isdigit() or not partes[1].isdigit() or not partes[2].isdigit():
        print("Data inválida. Use o formato DD/MM/AAAA.")
        return
 
    tarefa = {
        "tipo":          tipo,
        "data_prevista": data_prev,
        "responsavel":   responsavel,
    }
 
    if "cuidados" not in animais[nome]:
        animais[nome]["cuidados"] = []
 
    animais[nome]["cuidados"].append(tarefa)
    print(f"Cuidado '{tipo}' registrado para {nome}.")

def visualizar_cuidados(animais):
    nome = input("Nome do animal: ").strip()
    if nome not in animais:
        print("Animal não encontrado!")
        return
 
    if "cuidados" not in animais[nome] or len(animais[nome]["cuidados"]) == 0:
        print(f"{nome} não possui cuidados registrados.")
        return
 
    cuidados = animais[nome].get("cuidados", [])
 
    print(f"\n ==Cuidados de {nome}== ")
    for cuidado in cuidados:
        print(f"  {cuidado['tipo']} — {cuidado['data_prevista']} — Resp: {cuidado['responsavel']}")
        
while True:   
 print("====funcionalidades====")  
 print("[1]- cadastrar informações ")  
 print("[2]- visualizar informaçoes")
 print("[3]- sair ")   
 funcionalidade=int(input("escolha uma funcionalidade: "))

 if funcionalidade == 1:
    cadastrar_cuidado(animais)
 elif funcionalidade == 2:
    visualizar_cuidados(animais)
 elif funcionalidade == 3:
    print("você saiu!")
    break