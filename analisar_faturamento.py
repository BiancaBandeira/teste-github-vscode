import json

def calcular_faturamento(dados):
    # Carregar os dados do faturamento
    faturamento = dados.get('faturamento', [])

    # Filtrar os valores não nulos
    faturamento = [valor for valor in faturamento if valor is not None]

    if not faturamento:
        return None, None, 0

    menor_faturamento = min(faturamento)
    maior_faturamento = max(faturamento)
    media_mensal = sum(faturamento) / len(faturamento)
    dias_acima_da_media = sum(1 for valor in faturamento if valor > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_da_media

def main():
    # Carregar os dados do JSON
    with open('faturamento.json', 'r') as file:
        dados = json.load(file)

    menor, maior, dias_acima = calcular_faturamento(dados)

    print(f"Menor valor de faturamento: {menor}")
    print(f"Maior valor de faturamento: {maior}")
    print(f"Número de dias com faturamento acima da média: {dias_acima}")

if __name__ == "__main__":
    main()
