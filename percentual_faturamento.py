def calcular_percentual(faturamento):
    # Calcula o valor total de faturamento
    total = sum(faturamento.values())
    
    # Calcula o percentual de cada estado
    percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento.items()}
    
    return percentuais, total

def main():
    # Faturamento mensal por estado
    faturamento = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }
    
    percentuais, total = calcular_percentual(faturamento)
    
    # Exibir resultados
    print(f"Valor total de faturamento: R${total:.2f}")
    for estado, percentual in percentuais.items():
        print(f"Percentual de {estado}: {percentual:.2f}%")

if __name__ == "__main__":
    main()
