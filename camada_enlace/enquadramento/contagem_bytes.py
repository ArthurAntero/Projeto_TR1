def transmissor_cb(entrada, tamanho_quadro=6):
    """
    Função para realizar o enquadramento de uma string de bits utilizando contagem de bytes.
    
    Parâmetros:
    - entrada: string de bits.
    Retorno:
    - string de bits enquadrados.
    """
    # se a entrada não couber em bytes, retorna -1
    if len(entrada) % 8 != 0:
        return -1

    lista_bytes = [entrada[i:i+8] for i in range(0, len(entrada), 8)]
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
    return string_enquadrada

def receptor_cb(bits):
    """
    Função para realizar o desenquadramento de uma string de bits, utilizando contagem de bytes.

    Parametros:
    - bits: string de bits com os cabecalhos de enquadramento.
    Retorno:
    - string de bits sem os cabecalhos do enquadramento OU -1 caso tenha erro no desenquadramento.
    """
    # se há uma contagem de bits que não cabem em bytes retorna -1
    if (len(bits)) % 8 != 0:
        return -1

    conteudo = ""
    num_bytes = len(bits) // 8
    byte_index = 0
    while byte_index < num_bytes:
        byte = bits[byte_index*8:(byte_index + 1)*8]
        num_bytes_quadro = int(byte, 2)
        byte_index += 1
        for i in range(num_bytes_quadro):
            # se já passou do numero de bytes, ou seja, se o cabecalho tem mais bytes do que o esperado
            if byte_index > num_bytes:
                return -1
            else:
                conteudo += bits[byte_index*8:(byte_index + 1)*8]
                byte_index += 1
    return conteudo
