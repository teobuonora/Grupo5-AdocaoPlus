from datetime import datetime
import crud

def verificar_data(data_str):
    try:
        return datetime.strptime(data_str, "%d/%m/%Y").date()
    except ValueError:
        return None

def alertas_cuidados(usuario):
    animais = crud.carregar_animais(usuario)
    hoje = datetime.today().date()
    encontrou = False

    print("\n== ALERTAS DE CUIDADOS ==")
    for nome, info in animais.items():
        for cuidado in info.get("cuidados", []):
            data = verificar_data(cuidado["data_prevista"])
            if data is None:
                continue

            dias = (data - hoje).days

            if dias < 0:
                print(f"  [ATRASADO] {nome} — {cuidado['tipo']} (previsto: {cuidado['data_prevista']}, {abs(dias)} dia(s) em atraso)")
                encontrou = True
            elif dias <= 7:
                print(f"  [PROXIMO]  {nome} — {cuidado['tipo']} (previsto: {cuidado['data_prevista']}, faltam {dias} dia(s))")
                encontrou = True

    if not encontrou:
        print("  Nenhum alerta no momento.")

def menu_relatorios(usuario):
    while True:
        alertas_cuidados(usuario)  
        print("\nRELATORIOS E ALERTAS")
        print("[0] Voltar ao menu principal")

        opcao = input("Escolha uma opcao: ").strip()
        if opcao == "0":
            return "principal"
        else:
            print("Opcao invalida.")