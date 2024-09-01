def Transmissor_bit_paridade_par(bits):
    """
    Função do transmissor para realizar a detecção de erros de um 
    array de bytes utilizando bit de paridade PAR

    Parametros:
        - bits: string de bits
    Retorno:
        - string com os bits de dados e o bit de paridade no final
    """
    # Contando o número de bits '1' no byte
    num_bits_1 = bits.count('1')

    # Se o número de bits '1' é par, o bit de paridade é '0', senão é '1'
    bit_paridade = '0' if num_bits_1 % 2 == 0 else '1'
    resultado = bits + bit_paridade

    return resultado

def Receptor_bit_paridade_par(bits):
    """
    Função do receptor para realizar a detecção de erros de um 
    array de bytes utilizando bit de paridade PAR

    Parâmetros:
        - bits: string de bits de dados e bit de paridade no final
    Retorno:
        - booleano (True se os bits sao validos e False se os bits nao sao validos)
    """
    # Contando o número de bits '1' no byte original
    num_bits_1 = bits[:-1].count('1')

    # Se o número de bits '1' é par, o bit de paridade é '0', senão é '1'
    bit_paridade = '0' if num_bits_1 % 2 == 0 else '1'

    return (bits[-1] == bit_paridade, bits[:-1])
