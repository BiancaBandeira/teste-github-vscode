def inverter_string(texto):
    # Inicializa uma string vazia para armazenar o resultado
    texto_invertido = ""
    
    # Percorre a string de trás para frente usando um loop for
    for i in range(len(texto) - 1, -1, -1):
        # Adiciona o caractere atual à string invertida
        texto_invertido += texto[i]
    
    return texto_invertido

def main():
    # String de exemplo; você pode substituir pela entrada do usuário ou qualquer outra entrada de sua preferência
    texto = input("Digite a string que deseja inverter: ")
    
    # Chama a função para inverter a string
    resultado = inverter_string(texto)
    
    # Exibe o resultado
    print("String invertida:", resultado)

if __name__ == "__main__":
    main()
