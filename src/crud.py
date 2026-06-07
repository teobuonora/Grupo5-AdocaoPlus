import os
from datetime import datetime

animais = {}

PASTA_DADOS = "dados"

_contador_id = 0

def _caminho(usuario):
    return os.path.join(PASTA_DADOS, f"{usuario}.txt")

def carregar_animais(usuario):
    global _contador_id
    animais = {}
    caminho = _caminho(usuario)
    if not os.path.exists(caminho):
        return animais

    with open(caminho, "r", encoding="utf-8") as f:
        bloco = {}
        nome_atual = None
        for linha in f:
            linha = linha.rstrip("\n")
            if linha.startswith("ANIMAL:"):
                nome_atual = linha[len("ANIMAL:"):].strip()
                bloco = {}
            elif linha == "---" and nome_atual:
                animais[nome_atual] = bloco

                id_val = bloco.get("ID", "0")
                try:
                    num = int(id_val.split("-")[1])
                    if num > _contador_id:
                        _contador_id = num
                except (IndexError, ValueError):
                    pass
                nome_atual = None
                bloco = {}
            elif nome_atual is not None:
                if linha.startswith("CUIDADO>"):
                    partes = linha[len("CUIDADO>"):].strip().split(" | ")
                    if len(partes) == 3:
                        if "cuidados" not in bloco:
                            bloco["cuidados"] = []
                        bloco["cuidados"].append({
                            "tipo":          partes[0],
                            "data_prevista": partes[1],
                            "responsavel":   partes[2],
                        })
                elif ":" in linha:
                    chave, _, valor = linha.partition(":")
                    bloco[chave.strip()] = valor.strip()
    return animais

def salvar_animais(usuario, animais):
    os.makedirs(PASTA_DADOS, exist_ok=True)
    caminho = _caminho(usuario)
    with open(caminho, "w", encoding="utf-8") as f:
        for nome, info in animais.items():
            f.write(f"ANIMAL: {nome}\n")
            for campo, valor in info.items():
                if campo == "cuidados":
                    for c in valor:
                        f.write(f"CUIDADO> {c['tipo']} | {c['data_prevista']} | {c['responsavel']}\n")
                else:
                    f.write(f"{campo}: {valor}\n")
            f.write("---\n")

def gerar_id():
    global _contador_id
    _contador_id += 1
    return f"{_contador_id}"

def selecionar_opcao(titulo, opcoes):
    print(f"\n{titulo}")
    for i, op in enumerate(opcoes, 1):
        print(f"  [{i}] {op}")
    escolha = input("Escolha o número: ").strip()
    if escolha.isdigit() and 1 <= int(escolha) <= len(opcoes):
        return opcoes[int(escolha) - 1]
    print("Opção inválida.")
    return None

def resolver_outro(valor, pergunta):
    if valor == "Outro":
        digitado = input(f"  {pergunta}: ").strip()
        if digitado:
            return digitado
        print("  Valor inválido, mantido como 'Outro'.")
    return valor

def buscar_animal(animais, entrada):
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

def adicionar_animal(usuario):
    animais = carregar_animais(usuario)

    nome_chave = input("\nNome do animal: ").strip()
    if not nome_chave:
        print("Nome inválido.")
        return

    especie = selecionar_opcao("Espécie:", ESPECIES)
    if especie is None:
        return
    especie = resolver_outro(especie, "Digite qual é a espécie")

    raca = selecionar_opcao(f"Raça ({especie}):", RACAS_POR_ESPECIE.get(especie, ["Outro"]))
    if raca is None:
        return
    raca = resolver_outro(raca, "Digite qual é a raça")

    idade = input("\nIdade (ex: 3 anos, 6 meses): ").strip()
    if not idade:
        print("Idade inválida.")
        return

    saude = selecionar_opcao("Estado de saúde:", SAUDES)
    if saude is None:
        return
    saude = resolver_outro(saude, "Digite qual é o estado de saúde")

    comportamento = selecionar_opcao("Comportamento:", COMPORTAMENTOS)
    if comportamento is None:
        return
    comportamento = resolver_outro(comportamento, "Digite qual é o comportamento")

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
    salvar_animais(usuario, animais)
    print(f"\nAnimal adicionado com sucesso! ID gerado: {novo_id}")

def visualizar_animal(usuario):
    animais = carregar_animais(usuario)
    entrada = input("\nDigite o nome ou ID do animal: ").strip()
    nome = buscar_animal(animais, entrada)
    if nome:
        print(f"\n{'─'*40}")
        print(f"  Nome: {nome}")
        for campo, valor in animais[nome].items():
            if campo not in ("cuidados",):
                print(f"  {campo}: {valor}")

        cuidados = animais[nome].get("cuidados", [])
        if cuidados:
            print(f"\n  {'─'*36}")
            print("  PROXIMOS CUIDADOS:")
            hoje = datetime.today()
            for c in cuidados:
                try:
                    data = datetime.strptime(c["data_prevista"], "%d/%m/%Y")
                    delta = (data - hoje).days
                    if delta < 0:
                        aviso = f"  (atrasado {abs(delta)} dia(s)!)"
                    elif delta == 0:
                        aviso = "  (HOJE!)"
                    else:
                        aviso = f"  (em {delta} dia(s))"
                except ValueError:
                    aviso = "  (data invalida)"
                print(f"   * {c['tipo']:<22} {c['data_prevista']}  Resp: {c['responsavel']}{aviso}")
        print(f"{'─'*40}")
    else:
        print("Animal não encontrado.")

def listar_animais(usuario):
    animais = carregar_animais(usuario)
    if not animais:
        print("\nNenhum animal cadastrado.")
        return
    print(f"\n  {'ID':<8} {'Nome':<20} {'Espécie':<12} {'Idade':<12} {'Status'}")
    print("  " + "─" * 62)
    for nome, info in animais.items():
        status = info.get("Status", "Disponível")
        print(f"  {info.get('ID','?'):<8} {nome:<20} "
              f"{info.get('Espécie','?'):<12} {info.get('Idade','?'):<12} {status}")

def _pedir_novo_valor(campo, animais, nome_editar):
    if campo == "1":
        val = selecionar_opcao("Nova espécie:", ESPECIES)
        return resolver_outro(val, "Digite qual é a espécie") if val else val
    elif campo == "2":
        especie_atual = animais[nome_editar].get("Espécie", "Outro")
        val = selecionar_opcao(
            f"Nova raça ({especie_atual}):",
            RACAS_POR_ESPECIE.get(especie_atual, ["Outro"])
        )
        return resolver_outro(val, "Digite qual é a raça") if val else val
    elif campo == "3":
        return input("Nova idade: ").strip()
    elif campo == "4":
        val = selecionar_opcao("Novo estado de saúde:", SAUDES)
        return resolver_outro(val, "Digite qual é o estado de saúde") if val else val
    elif campo == "5":
        val = selecionar_opcao("Novo comportamento:", COMPORTAMENTOS)
        return resolver_outro(val, "Digite qual é o comportamento") if val else val
    elif campo == "6":
        return input("Nova data (DD/MM/AAAA): ").strip()
    return None

def editar_animal(usuario):
    animais = carregar_animais(usuario)
    entrada = input("\nDigite o nome ou ID do animal: ").strip()
    nome_editar = buscar_animal(animais, entrada)
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

    novo_valor = _pedir_novo_valor(campo, animais, nome_editar)
    if not novo_valor:
        print("Valor inválido. Edição cancelada.")
        return

    animais[nome_editar][campos[campo]] = novo_valor
    salvar_animais(usuario, animais)
    print(f"Campo '{campos[campo]}' atualizado com sucesso!")

def excluir_animal(usuario):
    animais = carregar_animais(usuario)
    entrada = input("\nDigite o nome ou ID do animal: ").strip()
    nome_excluir = buscar_animal(animais, entrada)
    if nome_excluir:
        animais.pop(nome_excluir)
        salvar_animais(usuario, animais)
        print(f"Animal '{nome_excluir}' excluído com sucesso!")
    else:
        print("Animal não encontrado.")

def menu_animais(usuario):
    while True:
        print("\nMENU PRINCIPAL")
        print("[1] Adicionar animal")
        print("[2] Visualizar animal")
        print("[3] Listar todos os animais")
        print("[4] Editar animal")
        print("[5] Excluir animal")
        print("[6] Ir para Cuidados")
        print("[7] Ir para Adocao")
        print("[8] Ir para Sugestoes")
        print("[0] Sair do programa")

        funcao = input("Escolha uma função: ").strip()

        if funcao == "1":
            adicionar_animal(usuario)
        elif funcao == "2":
            visualizar_animal(usuario)
        elif funcao == "3":
            listar_animais(usuario)
        elif funcao == "4":
            editar_animal(usuario)
        elif funcao == "5":
            excluir_animal(usuario)
        elif funcao == "6":
            return "cuidados"
        elif funcao == "7":
            return "adocao"
        elif funcao == "8":
            return "sugestoes"
        elif funcao == "0":
            return "sair"
        else:
            print("Função inválida.")