import crud
from alertas_regressiva import alertas_cuidados

TIPOS_CUIDADO = ["Vacina", "Banho", "Consulta veterinária", "Treino", "Outro"]
RESPONSAVEIS  = ["Veterinário", "Tutor", "Funcionário do abrigo", "Voluntário", "Outro"]

def cadastrar_cuidado(usuario):
    animais = crud.carregar_animais(usuario)
    entrada = input("\nDigite o nome ou ID do animal: ").strip()
    nome = crud.buscar_animal(animais, entrada)
    if not nome:
        print("Animal não encontrado.")
        return

    tipo = crud.selecionar_opcao("Tipo de cuidado:", TIPOS_CUIDADO)
    if tipo is None: return
    tipo = crud.resolver_outro(tipo, "Digite qual é o tipo de cuidado")

    data_prev = input("\nData prevista (DD/MM/AAAA): ").strip()
    partes = data_prev.split("/")
    if len(partes) != 3 or not all(p.isdigit() for p in partes):
        print("Data inválida. Use o formato DD/MM/AAAA.")
        return

    responsavel = crud.selecionar_opcao("Responsável:", RESPONSAVEIS)
    if responsavel is None: return
    responsavel = crud.resolver_outro(responsavel, "Digite qual é o responsável")

    if "cuidados" not in animais[nome]:
        animais[nome]["cuidados"] = []

    animais[nome]["cuidados"].append({
        "tipo":          tipo,
        "data_prevista": data_prev,
        "responsavel":   responsavel,
    })
    crud.salvar_animais(usuario, animais)
    print(f"Cuidado '{tipo}' registrado para {nome}.")

def visualizar_cuidados(usuario):
    animais = crud.carregar_animais(usuario)
    entrada = input("\nDigite o nome ou ID do animal: ").strip()
    nome = crud.buscar_animal(animais, entrada)
    if not nome:
        print("Animal não encontrado.")
        return

    cuidados = animais[nome].get("cuidados", [])
    if not cuidados:
        print(f"{nome} não possui cuidados registrados.")
        return

    print(f"\n== Cuidados de {nome} ({animais[nome].get('ID','?')}) ==")
    for i, c in enumerate(cuidados, 1):
        print(f"  {i}. {c['tipo']:<25} {c['data_prevista']}  —  Resp: {c['responsavel']}")

def menu_cuidados(usuario):
    while True:
        alertas_cuidados(usuario)
        print("\nABA DE CUIDADOS")
        print("[1] Cadastrar cuidado")
        print("[2] Visualizar cuidados")
        print("[0] Voltar ao menu principal")

        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastrar_cuidado(usuario)
        elif opcao == "2":
            visualizar_cuidados(usuario)
        elif opcao == "0":
            return "principal"
        else:
            print("Opção inválida.")