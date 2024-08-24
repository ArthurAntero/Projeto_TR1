def Transmissor_contagem_caractere_bytes(entrada, tamanho_quadro=6):
    """
    Função para realizar o enquadramento de um array de bytes utilizando contagem de bytes.
    
    Parâmetros:
    - entrada: String de bytes.
    """
    tamanho_quadro=6
    lista_bytes = [format(ord(char), '08b') for char in entrada]
    comprimento_total = len(lista_bytes)

    lista_enquadrada = []

    if comprimento_total <= tamanho_quadro:
        # Se o comprimento total for menor ou igual ao tamanho do quadro, adicionar o comprimento no início
        quadro = format(comprimento_total, '08b')  # Formatar o comprimento como 8 bits
        quadro += ''.join(lista_bytes)
        lista_enquadrada.append(quadro)
    else:
        # Quebra a entrada em múltiplos quadros
        aux1 = comprimento_total % tamanho_quadro  # Bytes restantes após os quadros completos
        num_quadros_completos = comprimento_total // tamanho_quadro  # Número de quadros completos

        # Inserir comprimento dos quadros completos
        for i in range(num_quadros_completos):
            quadro = format(tamanho_quadro, '08b')  # Formatar o comprimento como 8 bits
            quadro += ''.join(lista_bytes[i * tamanho_quadro:(i + 1) * tamanho_quadro])
            lista_enquadrada.append(quadro)
        
        # Inserir comprimento do último quadro (caso haja um quadro incompleto)
        if aux1 != 0:
            quadro = format(aux1, '08b')  # Formatar o comprimento como 8 bits
            quadro += ''.join(lista_bytes[num_quadros_completos * tamanho_quadro:])
            lista_enquadrada.append(quadro)

    string_enquadrada = ''.join(lista_enquadrada)
    return lista_enquadrada, string_enquadrada

# Exemplo de uso
entrada = "Aaaaaaa"  # Cada caractere é convertido em um byte
resultado = Transmissor_contagem_caractere_bytes(entrada, tamanho_quadro=6)  # Define o tamanho do quadro em bytes
print(resultado)  # Exemplo de saída: ['00000010', '0100000101000010', '01000011']

