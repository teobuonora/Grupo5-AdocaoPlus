import os
os.system ("cls")

from crud import menu_animais
from cuidados import menu_cuidados
from alertas_regressiva import alertas_cuidados
aba = "principal"

alertas_cuidados()

while aba != "sair":
    if aba == "principal":
        aba = menu_animais()
    elif aba == "cuidados":
        aba = menu_cuidados()

print("\nPrograma encerrado.")