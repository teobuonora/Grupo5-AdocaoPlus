# Grupo5-AdocaoPlus

Sistema CLI de abrigo animal para controle de animais, cuidados, adoções e sugestões.

## Visão geral

O projeto oferece um fluxo completo para usuários autenticados:
- autenticação por login/cadastro de usuário,
- cadastro, edição, visualização e exclusão de animais,
- registro de cuidados agendados e alertas regressivos,
- registro e cancelamento de adoções,
- sugestões personalizadas de adotante, cuidados, compatibilidade e atividades.

## Requisitos

- Python 3.8+
- Terminal / linha de comando

## Como executar

1. Abra o terminal na pasta raiz do projeto.
2. Execute:

```bash
python src/main.py
```

## Estrutura do projeto

- `src/main.py` — ponto de entrada; gerencia login e navegação entre as abas.
- `src/login.py` — cadastro e login de usuários; valida telefone e senha.
- `src/crud.py` — operações de CRUD para animais e menu principal.
- `src/cuidados.py` — cadastro e visualização de cuidados e integração de alertas.
- `src/alertas_regressiva.py` — alertas de cuidados próximos ou atrasados.
- `src/adocao.py` — registro e cancelamento de adoções com histórico.
- `src/sugestoes.py` — sugestões de perfil de adotante, cuidados, compatibilidade e atividades.

## Persistência de dados

Os dados são gravados em arquivos de texto dentro da pasta `dados/`:
- `dados/usuarios.txt` — usuários cadastrados.
- `dados/<usuario>.txt` — animais e cuidados por usuário.
- `dados/adocoes.txt` — histórico de adoções.

A pasta `dados/` é criada automaticamente quando o sistema salva informações.

## Funcionalidades principais

### Login e cadastro
- Cadastro de usuário com validação de telefone e confirmação de senha.
- Login com até 3 tentativas de senha.

### Gestão de animais
- Adicionar animal com informações de espécie, raça, idade, saúde, comportamento e chegada.
- Visualizar animal por nome ou ID.
- Listar todos os animais cadastrados.
- Editar campos do animal.
- Excluir animal do cadastro.

### Cuidados e alertas
- Registrar cuidados com tipo, data prevista e responsável.
- Visualizar lista de cuidados cadastrados.
- Alertas automáticos para cuidados próximos ou atrasados.

### Adoção
- Registrar adoção de animais disponíveis.
- Validar CPF do adotante e gravar dados de contato.
- Cancelar adoções e devolver o animal ao status disponível.

### Sugestões
- Sugestões personalizadas baseadas em espécie, comportamento, idade e saúde.
- Recomendações de adotante ideal, cuidados especiais, compatibilidade e atividades.

## Observações

- Aplicação de terminal CLI.
- Dados armazenados em arquivos de texto simples.
- Recomendado executar em Python 3.8 ou superior.
