# Sistema de Matrícula e Frequência Escolar

## Descrição

Este projeto desenvolve um sistema de matrícula e controle de frequência para uma escola, permitindo a gestão eficiente de alunos e a geração de relatórios detalhados para as secretarias municipais. A aplicação opera principalmente offline, garantindo funcionalidade mesmo sem conexão constante à internet.

## Funcionalidades

- **Matrícula de Alunos:** Cadastro de alunos novos no sistema.
- **Gerenciamento de Frequência:** Registro diário da presença dos alunos e geração de relatórios mensais.
- **Relatórios:** Exportação de dados de frequência para arquivos Excel, utilizados como base de dados para secretarias municipais.
- **Perfil do Aluno:** Atualização e exclusão de informações dos alunos matriculados.
- **Dashboard:** Visualização de gráficos relacionados à demografia do aluno, participação no programa Bolsa Família e dados de frequência escolar.

## Tecnologias Utilizadas

- **Python:** Linguagem de programação principal.
- **PyQt 6:** Framework usado para desenvolver a interface gráfica do usuário.
- **PostgreSQL:** Sistema de gerenciamento de banco de dados relacional para armazenamento de dados.
- **CSV & Excel:** Manipulação de arquivos para exportação de dados.

## Configuração e Instalação

Para executar este projeto, você precisará instalar as seguintes dependências:

```bash
pip install pyqt6 psycopg2-binary openpyxl

-Execução:
python main.py
