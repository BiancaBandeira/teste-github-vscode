def pertence_fibonacci(numero):
    # Função para verificar se o número pertence à sequência de Fibonacci
    if numero < 0:
        return False

    # Inicializa os dois primeiros números da sequência de Fibonacci
    a, b = 0, 1

    # Verifica se o número é um dos primeiros dois números da sequência
    if numero == a or numero == b:
        return True

    # Gera a sequência de Fibonacci até o número informado
    while b <= numero:
        if b == numero:
            return True
        a, b = b, a + b

    return False

# Entrada do usuário
numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

# Verifica se o número pertence à sequência e imprime a mensagem
if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
