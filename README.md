#  Analisador de Dados CSV Profissional

Este projeto é uma ferramenta de linha de comando (CLI) desenvolvida em Python para realizar análises estatísticas rápidas em arquivos CSV. Ideal para quem precisa extrair insights de planilhas sem abrir softwares pesados como o Excel.

##  Funcionalidades
- **Leitura Dinâmica:** Carrega qualquer arquivo CSV presente no diretório.
- **Validação de Tipos:** Identifica automaticamente se a coluna escolhida é numérica antes de tentar calcular.
- **Estatísticas Essenciais:** Calcula média, valor máximo, valor mínimo e soma total.
- **Tratamento de Erros:** Sistema resiliente a arquivos inexistentes ou entradas inválidas do usuário.

##  Tecnologias
- **Python 3.x**
- **Pandas:** Utilizada para manipulação de DataFrames e cálculos estatísticos otimizados.
- **OS Module:** Para verificação de existência de arquivos no sistema.

##  Por que Pandas?
Em um cenário real, os dados podem ter milhões de linhas. O Pandas é construído sobre o NumPy, permitindo que operações matemáticas sejam realizadas de forma extremamente rápida, o que seria inviável usando loops `for` tradicionais do Python em grandes datasets.

##  Como testar
1. Coloque o seu arquivo `.csv` na mesma pasta do script.
2. Execute: `python analisador.py`
3. Siga as instruções no terminal para selecionar a coluna.
