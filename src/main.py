import os
os.system("cls")

from login import tela_login, tela_cadastro
from crud import menu_animais
from cuidados import menu_cuidados

def main():
    print("\n" + "═" * 40)
    print("  ABRIGO DE ANIMAIS — SISTEMA")
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

    print(f"\n  Acesso concedido. Entrando no sistema como '{usuario_logado}'...\n")

    
    aba = "principal"
    while aba != "sair":
        if aba == "principal":
            aba = menu_animais(usuario_logado)
        elif aba == "cuidados":
            aba = menu_cuidados(usuario_logado)

    print("\nPrograma encerrado.")

if __name__ == "__main__":
    main()
