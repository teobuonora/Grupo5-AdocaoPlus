animais = {}
_contador_id = 0

def gerar_id():
    global _contador_id
    _contador_id += 1
    return f"ANI-{_contador_id:03d}"

def selecionar_opcao(titulo, opcoes):
    print(f"\n{titulo}")
    for i, op in enumerate(opcoes, 1):
        print(f"  [{i}] {op}")
    escolha = input("Escolha o número: ").strip()
    if escolha.isdigit() and 1 <= int(escolha) <= len(opcoes):
        return opcoes[int(escolha) - 1]
    print("Opção inválida.")
    return None

def buscar_animal(entrada):
    entrada = entrada.strip()
    if entrada in animais:
        return entrada
    for nome, info in animais.items():
        if info.get("ID", "").upper() == entrada.upper():
            return nome
    return None

RACAS_POR_ESPECIE = {
    "Cachorro": ["Labrador", "Golden Retriever", "Bulldog", "Pastor Alemão",
                 "Poodle", "Pit Bull", "Shih Tzu", "SRD (sem raça definida)", "Outro"],
    "Gato":     ["Persa", "Siamês", "Maine Coon", "Ragdoll",
                 "SRD (sem raça definida)", "Outro"],
    "Pássaro":  ["Calopsita", "Periquito", "Canário", "Papagaio", "Outro"],
    "Réptil":   ["Iguana", "Tartaruga", "Gecko", "Cobra", "Outro"],
    "Roedor":   ["Hamster", "Cobaia", "Camundongo", "Chinchila", "Outro"],
    "Outro":    ["Outro"],
}

ESPECIES       = list(RACAS_POR_ESPECIE.keys())
SAUDES         = ["Saudável", "Doente", "Em recuperação", "Em observação"]
COMPORTAMENTOS = ["Dócil", "Bravo", "Tímido", "Agitado", "Sociável"]

def adicionar_animal():
    nome_chave = input("\nNome do animal: ").strip()
    if not nome_chave:
        print("Nome inválido.")
        return

    especie = selecionar_opcao("Espécie:", ESPECIES)
    if especie is None:
        return

    raca = selecionar_opcao(f"Raça ({especie}):", RACAS_POR_ESPECIE.get(especie, ["Outro"]))
    if raca is None:
        return

    idade = input("\nIdade (ex: 3 anos, 6 meses): ").strip()
    if not idade:
        print("Idade inválida.")
        return

    saude = selecionar_opcao("Estado de saúde:", SAUDES)
    if saude is None:
        return

    comportamento = selecionar_opcao("Comportamento:", COMPORTAMENTOS)
    if comportamento is None:
        return

    data_chegada = input("\nData de chegada (DD/MM/AAAA): ").strip()

    novo_id = gerar_id()
    animais[nome_chave] = {
        "ID":              novo_id,
        "Espécie":         especie,
        "Raça":            raca,
        "Idade":           idade,
        "Estado de saúde": saude,
        "Comportamento":   comportamento,
        "Data de chegada": data_chegada,
    }
    print(f"\nAnimal adicionado com sucesso! ID gerado: {novo_id}")

def visualizar_animal():
    entrada = input("\nDigite o nome ou ID do animal: ").strip()
    nome = buscar_animal(entrada)
    if nome:
        print(f"\n{'─'*35}")
        print(f"  Nome: {nome}")
        for campo, valor in animais[nome].items():
            if campo != "cuidados":
                print(f"  {campo}: {valor}")
        print(f"{'─'*35}")
    else:
        print("Animal não encontrado.")

def listar_animais():
    if not animais:
        print("\nNenhum animal cadastrado.")
        return
    print(f"\n  {'ID':<10} {'Nome':<20} {'Espécie':<12} {'Idade'}")
    print("  " + "─" * 55)
    for nome, info in animais.items():
        print(f"  {info.get('ID','?'):<10} {nome:<20} "
              f"{info.get('Espécie','?'):<12} {info.get('Idade','?')}")


def _pedir_novo_valor(campo, nome_editar):
    """Pede o novo valor para cada campo de forma adequada, sem lambda."""
    if campo == "1":
        return selecionar_opcao("Nova espécie:", ESPECIES)

    elif campo == "2":
        especie_atual = animais[nome_editar].get("Espécie", "Outro")
        return selecionar_opcao(
            f"Nova raça ({especie_atual}):",
            RACAS_POR_ESPECIE.get(especie_atual, ["Outro"])
        )

    elif campo == "3":
        return input("Nova idade: ").strip()

    elif campo == "4":
        return selecionar_opcao("Novo estado de saúde:", SAUDES)

    elif campo == "5":
        return selecionar_opcao("Novo comportamento:", COMPORTAMENTOS)

    elif campo == "6":
        return input("Nova data (DD/MM/AAAA): ").strip()

    return None

def editar_animal():
    entrada = input("\nDigite o nome ou ID do animal: ").strip()
    nome_editar = buscar_animal(entrada)
    if not nome_editar:
        print("Animal não encontrado.")
        return

    print(f"\nDados atuais de '{nome_editar}':")
    for campo, valor in animais[nome_editar].items():
        if campo != "cuidados":
            print(f"  {campo}: {valor}")

    campos = {
        "1": "Espécie",
        "2": "Raça",
        "3": "Idade",
        "4": "Estado de saúde",
        "5": "Comportamento",
        "6": "Data de chegada",
    }

    print("\nO que deseja editar?")
    for k, label in campos.items():
        print(f"  [{k}] {label}")

    campo = input("Número do campo: ").strip()
    if campo not in campos:
        print("Opção inválida.")
        return

    novo_valor = _pedir_novo_valor(campo, nome_editar)

    if not novo_valor:
        print("Valor inválido. Edição cancelada.")
        return

    animais[nome_editar][campos[campo]] = novo_valor
    print(f"Campo '{campos[campo]}' atualizado com sucesso!")


def excluir_animal():
    entrada = input("\nDigite o nome ou ID do animal: ").strip()
    nome_excluir = buscar_animal(entrada)
    if nome_excluir:
        animais.pop(nome_excluir)
        print(f"Animal '{nome_excluir}' excluído com sucesso!")
    else:
        print("Animal não encontrado.")

def menu_animais():
    while True:
        print("MENU PRINCIPAL")
        print("[1] Adicionar animal")
        print("[2] Visualizar animal")
        print("[3] Listar todos os animais")
        print("[4] Editar animal")
        print("[5] Excluir animal")
        print("[6] Ir para Cuidados")
        print("[0] Sair do programa")

        funcao = input("Escolha uma função: ").strip()

        if funcao == "1":
            adicionar_animal()
        elif funcao == "2":
            visualizar_animal()
        elif funcao == "3":
            listar_animais()
        elif funcao == "4":
            editar_animal()
        elif funcao == "5":
            excluir_animal()
        elif funcao == "6":
            return "cuidados"
        elif funcao == "0":
            return "sair"
        else:
            print("Função inválida.")
