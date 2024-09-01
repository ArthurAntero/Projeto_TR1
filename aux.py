def transformar_para_bits(msg):
    """
    Função que trasnforma uma string de chars em uma string de bits

    Parametros:
    - msg: string de chars
    Retorno:
    - uma string de bits
    """
    bits = ""
    for char in msg:
        # converte o char para seu valor decimal na tabela ascii e depois formata em binario com 8 casas
        bits += format(ord(char), "08b")
    return bits

def transformar_para_ascii(bits):
    """
    Função que trasnforma uma string de bits em uma string de chars

    Parametros:
    - msg: string de bits
    Retorno:
    - uma string de bits
    """
    msg = ""
    for byte_index in range(0, len(bits), 8):  # itera a cada byte da string bits
        # converte o byte para um inteiro binario e depois para um char ascii
        msg += chr(int(bits[byte_index:byte_index + 8], 2))
    return msg
