from crud import carregar_animais, buscar_animal

PERFIL_ADOTANTE = {
    ("Cachorro", "Dócil"):    "Famílias com crianças pequenas ou idosos. Ambiente tranquilo.",
    ("Cachorro", "Bravo"):    "Tutor experiente, sem crianças pequenas. Espaço amplo.",
    ("Cachorro", "Agitado"):  "Pessoas ativas, atletas ou famílias com quintal grande.",
    ("Cachorro", "Tímido"):   "Ambiente silencioso, tutor paciente, sem outros animais dominantes.",
    ("Cachorro", "Sociável"): "Qualquer perfil de família. Ótimo para apartamento com passeios regulares.",
    ("Gato", "Dócil"):        "Apartamentos, adultos solitários ou casais. Baixa manutenção.",
    ("Gato", "Bravo"):        "Tutor experiente com gatos. Espaço próprio sem forçar contato.",
    ("Gato", "Tímido"):       "Ambiente quieto, sem crianças barulhentas. Tutor paciente.",
    ("Gato", "Agitado"):      "Casa com espaço para explorar e brinquedos interativos.",
    ("Gato", "Sociável"):     "Ótimo para quem quer um segundo pet ou família numerosa.",
    ("Pássaro", "Sociável"):  "Famílias que ficam em casa. Interação frequente é essencial.",
    ("Roedor", "Dócil"):      "Crianças acima de 6 anos. Primeiro pet ideal.",
    ("Réptil", "Dócil"):      "Adultos com interesse em animais exóticos. Cuidados específicos.",
}

def _faixa_etaria(idade_str):
    idade_str = idade_str.lower()
    anos = 0
    meses = 0
    partes = idade_str.split()
    for idx, parte in enumerate(partes):
        if parte.isdigit():
            num = int(parte)
            proximo = partes[idx + 1] if idx + 1 < len(partes) else ""
            if "ano" in proximo:
                anos = num
            elif "mes" in proximo or "mês" in proximo:
                meses = num
    total_meses = anos * 12 + meses
    if total_meses <= 0:
        total_meses = anos * 12 if anos else 0
    if total_meses <= 6:
        return "filhote"
    elif total_meses <= 84:
        return "adulto"
    else:
        return "idoso"

CUIDADOS_POR_FASE = {
    "filhote": [
        "Vacinação completa (V8/V10 para cães, V4 para gatos) — consulte o veterinário.",
        "Socialização precoce com pessoas e outros animais.",
        "Alimentação com ração específica para filhotes (3-4 vezes ao dia).",
        "Vermifugação a cada 15 dias até os 3 meses.",
        "Evitar contato com animais não vacinados e ambientes externos até completar as vacinas.",
    ],
    "adulto": [
        "Vacinação anual em dia.",
        "Consulta veterinária de rotina ao menos 1x por ano.",
        "Ração balanceada para adultos. Controle de peso.",
        "Exercícios regulares para cães. Enriquecimento ambiental para gatos.",
        "Castração recomendada para controle populacional e saúde.",
    ],
    "idoso": [
        "Consultas veterinárias a cada 6 meses (check-up geriátrico).",
        "Exames de sangue e urina anuais para monitorar órgãos.",
        "Ração específica para idosos (menor teor de proteína/fósforo).",
        "Conforto ortopédico: camas adequadas, rampinhas de acesso.",
        "Atenção a sinais de dor, letargia ou mudança de comportamento.",
    ],
}

COMPATIBILIDADE = {
    "Cachorro": {
        "Cachorro": "Alta  — desde que apresentados gradualmente.",
        "Gato":     "Media — depende do comportamento de cada um.",
        "Passaro":  "Baixa — instinto predatório pode ser perigoso.",
        "Roedor":   "Baixa — alto risco; não recomendado sem supervisão.",
        "Reptil":   "Media — evitar contato direto.",
    },
    "Gato": {
        "Cachorro": "Media — gatos timidos podem se estressar muito.",
        "Gato":     "Alta  — especialmente se introduzidos jovens.",
        "Passaro":  "Baixa — instinto de caca muito presente.",
        "Roedor":   "Baixa — não recomendado.",
        "Reptil":   "Media — evitar contato direto.",
    },
    "Passaro": {
        "Cachorro": "Baixa — estresse para o passaro.",
        "Gato":     "Baixa — risco real de ataque.",
        "Passaro":  "Alta  — mesma especie convive bem.",
        "Roedor":   "Alta  — sem interacao direta, coexistem bem.",
        "Reptil":   "Media — manter separados.",
    },
    "Roedor": {
        "Cachorro": "Baixa — risco alto.",
        "Gato":     "Baixa — risco alto.",
        "Passaro":  "Alta  — sem contato, convivem.",
        "Roedor":   "Alta  — mesma especie geralmente se da bem.",
        "Reptil":   "Baixa — repteis podem cacar roedores.",
    },
    "Reptil": {
        "Cachorro": "Media — reptil pode se estressar.",
        "Gato":     "Media — gato pode atacar o reptil.",
        "Passaro":  "Media — manter separados.",
        "Roedor":   "Baixa — não recomendado.",
        "Reptil":   "Alta  — mesma especie, ambientes separados.",
    },
}

def _normalizar_especie(esp):
    mapa = {
        "Pássaro": "Passaro", "Réptil": "Reptil",
        "Cachorro": "Cachorro", "Gato": "Gato", "Roedor": "Roedor",
    }
    return mapa.get(esp, esp)

ATIVIDADES = {
    ("Cachorro", "Agitado"):  ["Corrida diaria", "Agility", "Buscar objeto ", "Natacao"],
    ("Cachorro", "Docil"):    ["Caminhadas curtas", "Sessoes de carinho", "Adestramento basico"],
    ("Cachorro", "Timido"):   ["Socializacao progressiva", "Passeios tranquilos", "Jogos de olfato"],
    ("Cachorro", "Sociavel"): ["Visitas a parques caninos", "Agility em grupo", "Brincadeiras com outros caes"],
    ("Cachorro", "Bravo"):    ["Adestramento com reforco positivo", "Exercicio fisico intenso", "Passeios individuais"],
    ("Gato", "Agitado"):      ["Brinquedo de vara", "Laser", "Caixa de papelao e tuneis", "Janela para observar"],
    ("Gato", "Timido"):       ["Esconderijos acolhedores", "Brincadeiras suaves e silenciosas"],
    ("Gato", "Sociavel"):     ["Interacao humana frequente", "Brinquedos interativos em grupo"],
    ("Passaro", "Sociavel"):  ["Interacao diaria fora da gaiola", "Ensino de palavras", "Brinquedos de madeira"],
    ("Roedor", "Docil"):      ["Roda de exercicio", "Labirinto de papelao", "Exploracao supervisionada"],
    ("Reptil", "Docil"):      ["Banho de sol controlado", "Enriquecimento com esconderijos", "Manuseio gradual"],
}

def _normalizar_comportamento(comp):
    mapa = {
        "Dócil": "Docil", "Bravo": "Bravo", "Tímido": "Timido",
        "Agitado": "Agitado", "Sociável": "Sociavel",
    }
    return mapa.get(comp, comp)

def _sugerir_adotante(especie, comportamento):
    return PERFIL_ADOTANTE.get(
        (especie, comportamento),
        f"Adotante atento às necessidades de {especie}s com comportamento {comportamento}."
    )

def _sugerir_cuidados(idade_str):
    fase = _faixa_etaria(idade_str)
    return fase, CUIDADOS_POR_FASE.get(fase, [])

def _sugerir_compatibilidade(especie_alvo, animais):
    chave_alvo = _normalizar_especie(especie_alvo)
    tabela = COMPATIBILIDADE.get(chave_alvo, {})
    presentes = {}
    for info in animais.values():
        esp = info.get("Espécie", "")
        if esp and esp != especie_alvo:
            presentes[esp] = presentes.get(esp, 0) + 1
    resultado = []
    for esp, qtd in presentes.items():
        chave = _normalizar_especie(esp)
        comp = tabela.get(chave)
        if comp:
            resultado.append(f"  {esp:<12} ({qtd} cadastrado(s)): {comp}")
    return resultado

def _sugerir_atividades(especie, comportamento):
    chave = (_normalizar_especie(especie), _normalizar_comportamento(comportamento))
    return ATIVIDADES.get(chave, ["Consulte o veterinario para atividades personalizadas."])

def exibir_sugestoes(usuario):
    animais = carregar_animais(usuario)
    if not animais:
        print("\nNenhum animal cadastrado.")
        return

    entrada = input("\nDigite o nome ou ID do animal: ").strip()
    nome = buscar_animal(animais, entrada)
    if not nome:
        print("Animal não encontrado.")
        return

    info = animais[nome]
    especie       = info.get("Espécie", "Outro")
    comportamento = info.get("Comportamento", "Dócil")
    idade_str     = info.get("Idade", "")
    saude         = info.get("Estado de saúde", "")

    print(f"\n{'='*52}")
    print(f"  SUGESTOES PERSONALIZADAS -- {nome.upper()}")
    print(f"{'='*52}")
    print(f"  Especie: {especie}  |  Comportamento: {comportamento}")
    print(f"  Idade  : {idade_str}  |  Saude: {saude}")
    print(f"{'─'*52}")

    print("\n  [PERFIL DE ADOTANTE IDEAL]")
    print(f"  {_sugerir_adotante(especie, comportamento)}")

    fase, cuidados = _sugerir_cuidados(idade_str)
    print(f"\n  [CUIDADOS ESPECIAIS - {fase.upper()}]")
    for c in cuidados:
        print(f"   * {c}")

    if saude == "Doente":
        print("   ! Animal doente: agende consulta veterinaria com urgencia!")
    elif saude == "Em recuperação":
        print("   ! Em recuperacao: limite atividades fisicas e monitore diariamente.")

    compat = _sugerir_compatibilidade(especie, animais)
    if compat:
        print(f"\n  [COMPATIBILIDADE COM ANIMAIS JA CADASTRADOS]")
        for linha in compat:
            print(linha)
    else:
        print(f"\n  [COMPATIBILIDADE] Nenhum outro animal cadastrado para comparar.")

    print(f"\n  [ATIVIDADES RECOMENDADAS]")
    for a in _sugerir_atividades(especie, comportamento):
        print(f"   * {a}")

    print(f"\n{'='*52}")
    input("  Pressione Enter para continuar...")

def sugestoes_para_todos(usuario):
    animais = carregar_animais(usuario)
    disponiveis = {n: i for n, i in animais.items()
                   if i.get("Status", "Disponível") == "Disponível"}

    if not disponiveis:
        print("\nNenhum animal disponivel para sugestoes.")
        return

    print(f"\n{'='*58}")
    print("  RESUMO DE SUGESTOES -- TODOS OS ANIMAIS DISPONIVEIS")
    print(f"{'='*58}")
    for nome, info in disponiveis.items():
        especie       = info.get("Espécie", "?")
        comportamento = info.get("Comportamento", "?")
        fase, _       = _sugerir_cuidados(info.get("Idade", ""))
        perfil        = _sugerir_adotante(especie, comportamento)
        print(f"\n  {nome} ({info.get('ID','?')}) -- {especie} / {comportamento} / {fase}")
        print(f"    Adotante ideal: {perfil[:65]}{'...' if len(perfil) > 65 else ''}")
    print(f"\n{'='*58}")
    input("  Pressione Enter para continuar...")

def menu_sugestoes(usuario):
    while True:
        print("\nABA DE SUGESTOES")
        print("[1] Ver sugestoes detalhadas de um animal")
        print("[2] Resumo de sugestoes (todos os disponiveis)")
        print("[0] Voltar ao menu principal")

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            exibir_sugestoes(usuario)
        elif opcao == "2":
            sugestoes_para_todos(usuario)
        elif opcao == "0":
            return "principal"
        else:
            print("Opcao invalida.")