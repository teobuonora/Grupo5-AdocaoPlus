import os
os.system ("cls")

from crud import menu_animais
from cuidados import menu_cuidados

aba = "principal"

while aba != "sair":
    if aba == "principal":
        aba = menu_animais()
    elif aba == "cuidados":
        aba = menu_cuidados()

print("\nPrograma encerrado.")