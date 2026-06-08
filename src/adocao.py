import os
from datetime import datetime
from crud import carregar_animais, salvar_animais, buscar_animal

PASTA_DADOS = "dados"
ARQUIVO_ADOCOES = os.path.join(PASTA_DADOS, "adocoes.txt")

def carregar_adocoes():
    adocoes = []

    if not os.path.exists(ARQUIVO_ADOCOES):
        return adocoes

    with open(ARQUIVO_ADOCOES, "r", encoding="utf-8") as f:
        bloco = {}

        for linha in f:
            linha = linha.strip()

            if linha == "---":
                if bloco:
                    adocoes.append(bloco)
                    bloco = {}

            elif ":" in linha:
                chave, _, valor = linha.partition(":")
                bloco[chave.strip()] = valor.strip()

        if bloco:
            adocoes.append(bloco)

    return adocoes


def salvar_adocoes(adocoes):
    os.makedirs(PASTA_DADOS, exist_ok=True)

    with open(ARQUIVO_ADOCOES, "w", encoding="utf-8") as f:
        for a in adocoes:
            for chave, valor in a.items():
                f.write(f"{chave}: {valor}\n")
            f.write("---\n")

def _validar_data(data_str):
    try:
        return datetime.strptime(data_str, "%d/%m/%Y")
    except ValueError:
        return None


def _validar_cpf(cpf):
    digitos = "".join(filter(str.isdigit, cpf))
    return len(digitos) == 11


def _formatar_cpf(cpf):
    d = "".join(filter(str.isdigit, cpf))
    return f"{d[:3]}.{d[3:6]}.{d[6:9]}-{d[9:]}"

def registrar_adocao(usuario):
    animais = carregar_animais(usuario)

    disponiveis = {
        n: i for n, i in animais.items()
        if i.get("Status", "Disponível") == "Disponível"
    }

    if not disponiveis:
        print("\nNenhum animal disponível para adoção no momento.")
        return

    print("\n── Animais disponíveis ──")
    print(f"  {'ID':<8} {'Nome':<20} {'Espécie':<12} {'Idade'}")
    print("  " + "─" * 52)

    for nome, info in disponiveis.items():
        print(f"  {info.get('ID','?'):<8} {nome:<20} {info.get('Espécie','?'):<12} {info.get('Idade','?')}")

    entrada = input("\nDigite o nome ou ID do animal: ").strip()
    nome = buscar_animal(animais, entrada)

    if not nome or animais[nome].get("Status") != "Disponível":
        print("Animal não encontrado ou não disponível.")
        return

    print(f"\n── Dados do adotante para '{nome}' ──")

    adotante = input("Nome do adotante: ").strip()
    if not adotante:
        print("Nome inválido.")
        return

    cpf_raw = input("CPF (somente números): ").strip()
    if not _validar_cpf(cpf_raw):
        print("CPF inválido.")
        return
    cpf = _formatar_cpf(cpf_raw)

    telefone = input("Telefone: ").strip()
    if not telefone:
        print("Telefone inválido.")
        return

    data_raw = input("Data da adoção (DD/MM/AAAA): ").strip()
    if not _validar_data(data_raw):
        print("Data inválida.")
        return

    animais[nome]["Status"] = "Adotado"
    animais[nome]["Adotante"] = adotante
    salvar_animais(usuario, animais)

    adocoes = carregar_adocoes()
    adocoes.append({
        "Animal": nome,
        "ID Animal": animais[nome].get("ID", "?"),
        "Espécie": animais[nome].get("Espécie", "?"),
        "Adotante": adotante,
        "CPF": cpf,
        "Telefone": telefone,
        "Data": data_raw,
        "Usuario": usuario,
    })

    salvar_adocoes(adocoes)

    print(f"\n✔ Adoção de '{nome}' registrada com sucesso!")

def cancelar_adocao(usuario):
    animais = carregar_animais(usuario)

    adotados = {
        n: i for n, i in animais.items()
        if i.get("Status") == "Adotado"
    }

    if not adotados:
        print("\nNenhum animal com status 'Adotado' encontrado.")
        return

    print("\n── Animais adotados ──")
    for nome, info in adotados.items():
        print(f"  {info.get('ID','?'):<8} {nome:<20} Adotante: {info.get('Adotante','?')}")

    entrada = input("\nDigite o nome ou ID para cancelar a adoção: ").strip()
    nome = buscar_animal(animais, entrada)

    if not nome or animais[nome].get("Status") != "Adotado":
        print("Animal não encontrado ou não está adotado.")
        return

    animais[nome]["Status"] = "Disponível"
    animais[nome].pop("Adotante", None)
    salvar_animais(usuario, animais)

    adocoes = carregar_adocoes()
    adocoes = [a for a in adocoes if a.get("Animal") != nome]
    salvar_adocoes(adocoes)

    print(f"Adoção de '{nome}' cancelada com sucesso!")

def menu_adocao(usuario):
    while True:
        print("\nABA DE ADOÇÃO")
        print("[1] Registrar adoção")
        print("[2] Cancelar adoção")
        print("[0] Voltar ao menu principal")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            registrar_adocao(usuario)

        elif opcao == "2":
            cancelar_adocao(usuario)

        elif opcao == "0":
            return "principal"

        else:
            print("Opção inválida.")