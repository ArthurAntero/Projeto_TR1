def Transmissor_insercao_bytes(entrada):
    """
    Função para realizar o enquadramento de um array de bytes utilizando insercao de bytes.
    
    Parâmetros:
    - entrada: String de bytes.
    """
    tamanho_quadro=6 # 6 bytes por quadro
    flag = "00100110" # &
    esc = "00011011" # ESC
    quadros = []
    
    lista_bytes = [format(ord(char), '08b') for char in entrada]
    print(lista_bytes)

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
        quadros.append(quadro_completo)

    return quadros 

# Exemplo de uso
entrada = "&a"  # Cada caractere é convertido em um byte
resultado = Transmissor_insercao_bytes(entrada)  # Define o tamanho do quadro em bytes
print(resultado)  