import pandas as pd
import os

# ==========================================
# Analisador de Dados Simples (CSV + Python)
# Focado em análise estatística básica
# ==========================================
#
# Fluxo do programa:
#   1. Carrega um arquivo CSV presente no diretório atual.
#   2. Lista as colunas disponíveis para o usuário escolher.
#   3. Valida se a coluna escolhida é numérica.
#   4. Calcula média, máximo, mínimo e soma da coluna.
#   5. Repete a partir do passo 2 até o usuário decidir sair.

CASAS_DECIMAIS = 2  # dígitos após a vírgula na exibição dos resultados


def exibir_cabecalho():
    """Exibe o título visual do sistema."""
    print("\n" + "=" * 50)
    print("      ANALISADOR DE DADOS PROFISSIONAL")
    print("=" * 50)


def carregar_arquivo():
    """Solicita o nome do arquivo e tenta carregá-lo usando Pandas.

    Repete a solicitação enquanto o arquivo informado não existir.
    Retorna o DataFrame carregado, ou None se a leitura falhar
    (ex.: arquivo corrompido ou em formato inválido).
    """
    while True:
        arquivo = input("\nDigite o nome do arquivo CSV (ex: vendas.csv): ").strip()

        if not os.path.exists(arquivo):
            print("Erro: O arquivo '{}' não foi encontrado no diretório.".format(arquivo))
            continue

        try:
            df = pd.read_csv(arquivo)
            print("Sucesso: Arquivo carregado com {} registros.".format(len(df)))
            return df
        except Exception as e:
            print("Erro ao ler o arquivo: {}".format(e))
            return None


def selecionar_coluna(df):
    """Lista as colunas do DataFrame e permite ao usuário escolher uma numérica.

    Retorna o nome da coluna escolhida se ela for numérica, ou None
    caso a seleção seja inválida ou a coluna não seja numérica.
    """
    print("\nColunas disponíveis no arquivo:")
    for i, coluna in enumerate(df.columns):
        print("[{}] - {}".format(i, coluna))

    try:
        indice = int(input("\nDigite o número da coluna que deseja analisar: "))
        coluna_nome = df.columns[indice]

        # Validação: a coluna precisa ser numérica para permitir os cálculos
        if not pd.api.types.is_numeric_dtype(df[coluna_nome]):
            print("Erro: A coluna '{}' não é numérica e não pode ser analisada.".format(coluna_nome))
            return None

        return coluna_nome
    except (ValueError, IndexError):
        print("Erro: Seleção inválida. Escolha um número da lista.")
        return None


def calcular_estatisticas(df, coluna):
    """Calcula média, máximo, mínimo e soma da coluna selecionada.

    O Pandas já possui métodos otimizados (vetorizados sobre NumPy)
    para essas operações, o que evita loops manuais em Python.
    """
    return {
        "media": df[coluna].mean(),
        "maior": df[coluna].max(),
        "menor": df[coluna].min(),
        "soma": df[coluna].sum(),
    }


def exibir_resultados(coluna, stats):
    """Formata e exibe os resultados estatísticos na tela."""
    print("\n" + "-" * 40)
    print("RESUMO ESTATÍSTICO: {}".format(coluna.upper()))
    print("-" * 40)
    print("Média dos valores:     {:.{casas}f}".format(stats["media"], casas=CASAS_DECIMAIS))
    print("Maior valor original:  {:.{casas}f}".format(stats["maior"], casas=CASAS_DECIMAIS))
    print("Menor valor original:  {:.{casas}f}".format(stats["menor"], casas=CASAS_DECIMAIS))
    print("Soma total da coluna:  {:.{casas}f}".format(stats["soma"], casas=CASAS_DECIMAIS))
    print("-" * 40)


def main():
    """Fluxo principal do programa."""
    exibir_cabecalho()

    # 1. Carregar dados
    dados = carregar_arquivo()
    if dados is None:
        return

    # 2. Loop de análise: permite analisar várias colunas na mesma sessão
    while True:
        coluna_escolhida = selecionar_coluna(dados)

        if coluna_escolhida:
            resultados = calcular_estatisticas(dados, coluna_escolhida)
            exibir_resultados(coluna_escolhida, resultados)

        continuar = input("\nDeseja analisar outra coluna? (s/n): ").lower()
        if continuar != "s":
            print("\nFinalizando analisador. Até a próxima!")
            break


if __name__ == "__main__":
    main()
