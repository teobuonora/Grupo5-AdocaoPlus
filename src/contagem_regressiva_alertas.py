from crud import adicionar_animal, visualizar_animal, editar_animal, excluir_animal, animais
from cadastro_e_atividade import cadastrar_cuidado, visualizar_cuidados
from datetime import datetime

def contagem_regressiva(animais):
    nome = input("Nome do animal: ").strip()
    if nome not in animais:
        print("Animal não encontrado.")
        return

    if "cuidados" not in animais[nome] or len(animais[nome]["cuidados"]) == 0:
        print(f"{nome} nao possui cuidados registrados.")
        return

    cuidados = animais[nome].get("cuidados", [])
    hoje = datetime.today()

    print(f"\n== Proximos cuidados de {nome} ==")
    for cuidado in cuidados:
        data_prev = datetime.strptime(cuidado['data_prevista'], "%d/%m/%Y")
        dias_restantes = (data_prev - hoje).days

        if dias_restantes < 0:
            alerta = f"ATRASADO ha {abs(dias_restantes)} dias"
        elif dias_restantes == 0:
            alerta = "HOJE"
        else:
            alerta = f"faltam {dias_restantes} dias"

        print(f"  {cuidado['tipo']} — {cuidado['data_prevista']} — Resp: {cuidado['responsavel']} — {alerta}")

while True:
    print("====contagem regressiva====")
    print("[1]- ver alertas de um animal")
    print("[2]- sair")
    opcao = int(input("escolha uma opcao: "))

    if opcao == 1:
        contagem_regressiva(animais)
    elif opcao == 2:
        print("voce saiu!")
        break