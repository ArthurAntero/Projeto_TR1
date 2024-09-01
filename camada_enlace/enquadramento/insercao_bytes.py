def Transmissor_insercao_bytes(entrada, tamanho_quadro=6):
    """
    Função para realizar o enquadramento de uma string de bits, utilizando insercao de bytes.
    
    Parâmetros:
    - entrada: string de bits.
    """
    flag = "00100110" # &
    esc = "00011011" # ESC
    quadros = ""
    
    lista_bytes = [format(ord(char), '08b') for char in entrada]

    # Dividindo os bytes em quadros
    while len(lista_bytes) > 0:
        quadro = lista_bytes[:tamanho_quadro]
        lista_bytes = lista_bytes[tamanho_quadro:]

        quadro_inserido = ""
        for byte in quadro:
            # Se o byte for igual a FLAG ou ESC, insere ESC antes
            if byte == flag or byte == esc:
                quadro_inserido += esc
            quadro_inserido += flag

        # Adicionando FLAG ao início e ao fim do quadro
        quadro_completo = flag + quadro_inserido + flag
        quadros += quadro_completo

    return quadros

def Receptor_insercao_bytes(bits):
    """
    Função para realizar o desenquadramento de uma string de bits, utilizando insercao de bytes
    """
    return ""

# Exemplo de uso
entrada = "&a"  # Cada caractere é convertido em um byte
resultado = Transmissor_insercao_bytes(entrada)  # Define o tamanho do quadro em bytes
print(resultado)  