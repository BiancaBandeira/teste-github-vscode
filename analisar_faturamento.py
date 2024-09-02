import json

# Função para carregar dados do arquivo JSON
def carregar_dados(caminho_arquivo):
    with open(caminho_arquivo, 'r') as file:
        return json.load(file)

# Função principal para analisar o faturamento
def analisar_faturamento(dados):
    # Filtra apenas os dias com faturamento
    faturamentos = [item['faturamento'] for item in dados if item['faturamento'] > 0]

    if not faturamentos:
        print("Não há dados de faturamento.")
        return

    # Calcular o menor e o maior valor de faturamento
    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)

    # Calcular a média de faturamento
    media_faturamento = sum(faturamentos) / len(faturamentos)
    # Contar os dias com faturamento acima da média
    dias_acima_media = sum(1 for f in faturamentos if f > media_faturamento)

    # Exibir os resultados
    print(f"Menor valor de faturamento: {menor_faturamento}")
    print(f"Maior valor de faturamento: {maior_faturamento}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_media}")

# Caminho do arquivo JSON
caminho_arquivo = 'faturamento.json'

# Carregar dados e analisar
dados_faturamento = carregar_dados(caminho_arquivo)
analisar_faturamento(dados_faturamento)