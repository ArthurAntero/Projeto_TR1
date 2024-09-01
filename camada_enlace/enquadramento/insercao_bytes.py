flag = "00100110" # &
esc = "00011011" # ESC

def transmissor_insercao_bytes(entrada, tamanho_quadro=6):
    """
    Função para realizar o enquadramento de uma string de bits, utilizando insercao de bytes.
    
    Parametros:
        - entrada: string de bits.
    Saida:
        - uma string de bits com a insercao de bytes de flag e esc
    """
    # se a entrada não couber em bytes, retorna -1
    if len(entrada) % 8 != 0:
        return -1

    quadros = ""
    lista_bytes = [entrada[i:i+8] for i in range(0, len(entrada), 8)]

    # Dividindo os bytes em quadros
    while len(lista_bytes) > 0:
        quadro = lista_bytes[:tamanho_quadro]
        lista_bytes = lista_bytes[tamanho_quadro:]

        quadro_inserido = ""
        for byte in quadro:
            # Se o byte for igual a FLAG ou ESC, insere ESC antes
            if byte == flag or byte == esc:
                quadro_inserido += esc
            quadro_inserido += byte

        # Adicionando FLAG ao início e ao fim do quadro
        quadro_completo = flag + quadro_inserido + flag
        quadros += quadro_completo

    return quadros

def receptor_insercao_bytes(bits):
    """
    Função para realizar o desenquadramento de uma string de bits, utilizando insercao de bytes

    Parametros:
        - bits: string de bits com bytes de flag e esc
    Saida:
        - string de bits sem os bytes de flag e esc
    """
    # se a entrada não couber em bytes, retorna -1
    if len(bits) % 8 != 0:
        return -1

    conteudo = ""

    num_bytes = len(bits) // 8
    byte_index = 0
    while byte_index < num_bytes:
        byte = bits[byte_index*8:(byte_index + 1)*8]
        proximo_byte = bits[(byte_index + 1)*8:(byte_index + 2)*8]
        if byte == esc and (proximo_byte == flag or proximo_byte == esc):
            conteudo += proximo_byte
            byte_index += 2
        elif byte == esc:
            return -1
        elif byte == flag:
            byte_index += 1
        else:
            conteudo += byte
            byte_index += 1

    return conteudo

