import os
import re

PASTA_DADOS = "dados"
ARQUIVO_USUARIOS = os.path.join(PASTA_DADOS, "usuarios.txt")

def carregar_usuarios():
    usuarios = {}
    if not os.path.exists(ARQUIVO_USUARIOS):
        return usuarios
    with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue
            partes = linha.split(" | ")
            if len(partes) == 3:
                nome, telefone, senha = partes
                usuarios[nome] = {"telefone": telefone, "senha": senha}
    return usuarios

def salvar_usuarios(usuarios):
    os.makedirs(PASTA_DADOS, exist_ok=True)
    with open(ARQUIVO_USUARIOS, "w", encoding="utf-8") as f:
        for nome, dados in usuarios.items():
            f.write(f"{nome} | {dados['telefone']} | {dados['senha']}\n")

def validar_telefone(tel):
    digitos = re.sub(r"\D", "", tel)
    return 10 <= len(digitos) <= 11

def formatar_telefone(tel):
    digitos = re.sub(r"\D", "", tel)
    if len(digitos) == 11:
        return f"({digitos[:2]}) {digitos[2:7]}-{digitos[7:]}"
    return f"({digitos[:2]}) {digitos[2:6]}-{digitos[6:]}"

def cabecalho(titulo):
    print("\n" + "═" * 40)
    print(f"  {titulo}")
    print("═" * 40)

def tela_cadastro():
    cabecalho("CADASTRO DE USUÁRIO")
    usuarios = carregar_usuarios()

    nome = input("  Nome completo : ").strip()
    if not nome:
        print("  ✗ Nome inválido.")
        return False
    if nome in usuarios:
        print(f"  ✗ Usuário '{nome}' já existe.")
        return False

    telefone_raw = input("  Telefone      : ").strip()
    if not validar_telefone(telefone_raw):
        print("  ✗ Telefone inválido. Use (XX) XXXXX-XXXX ou só dígitos.")
        return False
    telefone = formatar_telefone(telefone_raw)

    senha = input("  Senha         : ").strip()
    if len(senha) < 4:
        print("  ✗ Senha muito curta (mínimo 4 caracteres).")
        return False
    confirma = input("  Confirme senha: ").strip()
    if senha != confirma:
        print("  ✗ As senhas não coincidem.")
        return False

    usuarios[nome] = {"telefone": telefone, "senha": senha}
    salvar_usuarios(usuarios)
    print(f"\n  ✔ Usuário '{nome}' cadastrado com sucesso!")
    return True

def tela_login():
    cabecalho("LOGIN")
    usuarios = carregar_usuarios()

    if not usuarios:
        print("  Nenhum usuário cadastrado ainda.")
        return None

    nome = input("  Nome     : ").strip()
    if nome not in usuarios:
        print("  ✗ Usuário não encontrado.")
        return None

    tentativas = 3
    while tentativas > 0:
        senha = input("  Senha    : ").strip()
        if senha == usuarios[nome]["senha"]:
            print(f"\n  ✔ Bem-vindo(a), {nome}! Login realizado.")
            return nome
        tentativas -= 1
        if tentativas > 0:
            print(f"  ✗ Senha incorreta. Tentativas restantes: {tentativas}")
        else:
            print("  ✗ Senha incorreta. Acesso bloqueado.")
    return None

def tela_excluir_conta(usuario_logado):
    cabecalho("EXCLUIR CONTA")
    usuarios = carregar_usuarios()

    print(f"  Você está prestes a excluir a conta: {usuario_logado}")
    confirma = input("  Digite sua senha para confirmar: ").strip()
    if confirma != usuarios[usuario_logado]["senha"]:
        print("  ✗ Senha incorreta. Operação cancelada.")
        return False

    usuarios.pop(usuario_logado)
    salvar_usuarios(usuarios)
    print(f"  ✔ Conta '{usuario_logado}' excluída com sucesso.")
    return True

def menu_usuario(nome):
    while True:
        cabecalho(f"BEM-VINDO, {nome.upper()}")
        print("  [1] Ver meus dados")
        print("  [2] Excluir minha conta")
        print("  [0] Sair")
        op = input("  Opção: ").strip()

        if op == "1":
            usuarios = carregar_usuarios()
            dados = usuarios.get(nome, {})
            print(f"\n  Nome     : {nome}")
            print(f"  Telefone : {dados.get('telefone','?')}")
            print(f"  Senha    : {'*' * len(dados.get('senha',''))}")
        elif op == "2":
            excluido = tela_excluir_conta(nome)
            if excluido:
                return
        elif op == "0":
            print("  Até logo!")
            return
        else:
            print("  Opção inválida.")

def menu_login():
    while True:
        cabecalho("SISTEMA DE AUTENTICAÇÃO")
        print("  [1] Login")
        print("  [2] Cadastrar novo usuário")
        print("  [0] Sair")
        op = input("  Opção: ").strip()

        if op == "1":
            usuario = tela_login()
            if usuario:
                menu_usuario(usuario)
        elif op == "2":
            tela_cadastro()
        elif op == "0":
            print("\n  Programa encerrado.")
            break
        else:
            print("  Opção inválida.")