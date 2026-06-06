# Grupo5-AdocaoPlus

Aplicação de linha de comando para gerenciar animais em um abrigo, registrar cuidados
e exibir alertas sobre procedimentos agendados (vacinas, banho, consultas, etc.).

**Principais funcionalidades**
- Gerenciar cadastro de animais (adicionar, visualizar, listar, editar, excluir).
- Registrar e visualizar cuidados/agendamentos por animal.
- Alertas regressivos que mostram cuidados próximos ou em atraso.

**Requisitos**
- Python 3.8+

**Como executar**
1. Abra um terminal na pasta do projeto.
2. Execute:

```bash
python src/main.py
```

Observação: o programa é uma aplicação de terminal que guarda os dados em memória
durante a execução (não há persistência em arquivo ou banco de dados).

**Estrutura do projeto**
- [src/main.py](src/main.py) — ponto de entrada e loop de navegação entre menus.
- [src/crud.py](src/crud.py) — operações de CRUD para animais e menus principais.
- [src/cuidados.py](src/cuidados.py) — registro e visualização de cuidados/agendamentos.
- [src/alertas_regressiva.py](src/alertas_regressiva.py) — lógica de alertas por data.

**Uso**
- O menu principal permite adicionar, visualizar, listar, editar e excluir animais.
- A seção de cuidados permite cadastrar agendamentos (tipo, data, responsável)
	e exibe alertas automáticos para itens próximos ou atrasados.

**Contribuições**
- Sugestões e melhorias são bem-vindas — abra uma issue ou envie um pull request.

**Licença**
- Sem licença explícita (adicione uma se desejar compartilhar publicamente).