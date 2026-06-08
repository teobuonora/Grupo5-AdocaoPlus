import os
os.system("cls" if os.name == "nt" else "clear")

from login import tela_login, tela_cadastro
from crud import menu_animais
from cuidados import menu_cuidados
from adocao import menu_adocao
from sugestoes import menu_sugestoes


def main():
    print("\n" + "═" * 40)
    print("  ADOCAO+ -- SISTEMA DE ABRIGO")
    print("═" * 40)
    print("  Faça login ou cadastre-se para continuar.")

    usuario_logado = None

    while not usuario_logado:
        print("\n  [1] Login")
        print("  [2] Cadastrar novo usuário")
        print("  [0] Sair")

        op = input("  Opção: ").strip()

        if op == "1":
            usuario_logado = tela_login()

        elif op == "2":
            tela_cadastro()

        elif op == "0":
            print("\n  Programa encerrado.")
            return

        else:
            print("  Opção inválida.")

    print(f"\n  Acesso concedido. Entrando como '{usuario_logado}'...\n")

    aba = "principal"

    while aba != "sair":

        if aba == "principal":
            aba = menu_animais(usuario_logado)

        elif aba == "cuidados":
            aba = menu_cuidados(usuario_logado)

        elif aba == "adocao":
            aba = menu_adocao(usuario_logado)

        elif aba == "sugestoes":
            aba = menu_sugestoes(usuario_logado)

        else:
            aba = "principal"

    print("\nPrograma encerrado.")


if __name__ == "__main__":
    main()
