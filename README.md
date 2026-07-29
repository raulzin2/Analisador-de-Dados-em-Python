Analisador de Dados CSV Profissional
Ferramenta para análises estatísticas rápidas em arquivos de dados tabulares. Ideal para extrair insights (média, máximo, mínimo, soma) sem abrir softwares pesados como o Excel. Disponível em duas versões: a original via terminal (CLI, com Pandas) e uma interface web que reproduz a mesma lógica direto no navegador.
Funcionalidades
Leitura Dinâmica: carrega um arquivo de dados e identifica automaticamente suas colunas.
Validação de Tipos: identifica se a coluna escolhida é numérica antes de tentar calcular.
Estatísticas Essenciais: calcula média, valor máximo, valor mínimo e soma total.
Tratamento de Erros: resiliente a arquivos inexistentes, formatos inválidos ou colunas não numéricas.
Estrutura do repositório
```
analisador-de-dados/
├── cli/
│   └── analisador.py       # versão original, via terminal (Pandas)
├── web/
│   └── index.html          # interface web (HTML/CSS/JS + Papa Parse + SheetJS)
└── dados-exemplo/
    ├── vendas_teste.csv     # dataset de teste (usar com a versão CLI)
    └── vendas_teste.xlsx    # mesmo dataset em Excel, com fórmulas de resumo para conferência
```
Versão CLI
Tecnologias
Python 3.x
Pandas: manipulação de DataFrames e cálculos estatísticos otimizados (construído sobre o NumPy — muito mais rápido que loops `for` tradicionais em datasets grandes).
OS Module: verificação de existência de arquivos no sistema.
Como testar
Copie `dados-exemplo/vendas_teste.csv` para dentro da pasta `cli/` (o script busca o arquivo no diretório atual).
Execute:
```bash
   cd cli
   python3 analisador.py
   ```
Informe o nome do arquivo (`vendas_teste.csv`) e siga as instruções para escolher a coluna.
Versão Web
Interface simples em HTML/CSS/JS que roda direto no navegador, sem instalação e sem back-end. Aceita upload de `.csv` ou `.xlsx`/`.xls` (usa as bibliotecas Papa Parse e SheetJS via CDN só para leitura do arquivo). Reproduz a mesma lógica da versão CLI: lista as colunas, valida se são numéricas e calcula os mesmos indicadores. Nada é enviado a um servidor — o processamento acontece todo localmente, no navegador.
Como executar
Basta abrir o arquivo `web/index.html` em qualquer navegador e arrastar (ou selecionar) um dos arquivos de `dados-exemplo/`.
Dataset de teste
`dados-exemplo/vendas_teste.xlsx` (e sua versão `.csv` equivalente) simula vendas de uma loja de eletrônicos, com colunas numéricas (`Quantidade`, `Preco_Unitario`, `Total`) e colunas de texto (`Produto`, `Categoria`, `Regiao`, `Data_Venda`) — estas últimas servem para testar o tratamento de "coluna não numérica". A planilha `.xlsx` já traz, ao final, um resumo com fórmulas (`MÉDIA`, `MÁXIMO`, `MÍNIMO`, `SOMA`) para conferir se o analisador está calculando certo.
Autor
Projeto desenvolvido como exercício acadêmico de análise de dados com Python e Pandas.

LINK: file:///C:/Users/Raul%20Teot%C3%B4nio/Downloads/analisador-de-dados/analisador-de-dados/web/index.html
