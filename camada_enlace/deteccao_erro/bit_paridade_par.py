def Transmissor_bit_paridade_par(quadro):
    """
    Função do transmissor para realizar a detecção de erros de um 
    array de bytes utilizando bit de paridade PAR

    Parâmetros:
    - quadro: String de bytes
    """
    # Contando o número de bits '1' no byte
    num_bits_1 = quadro.count('1')
    
    # Se o número de bits '1' é par, o bit de paridade é '0', senão é '1'
    bit_paridade = '0' if num_bits_1 % 2 == 0 else '1'
    resultado = quadro + bit_paridade
    
    return resultado

def Receptor_bit_paridade_par(quadro):
    """
    Função do receptor para realizar a detecção de erros de um 
    array de bytes utilizando bit de paridade PAR

    Parâmetros:
    - quadro: String de bytes
    """
    # Contando o número de bits '1' no byte original
    num_bits_1 = quadro[:-1].count('1')
    
    # Se o número de bits '1' é par, o bit de paridade é '0', senão é '1'
    bit_paridade = '0' if num_bits_1 % 2 == 0 else '1'
    
    if quadro[-1] == bit_paridade:
        return "Nenhum erro detectado!"
    else:
        return "Erro detectado!"

# Exemplo de uso
quadro = "00100110001000000010011000100110"
print(Transmissor_bit_paridade_par(quadro))
print(Receptor_bit_paridade_par(quadro)) # Resposta sem erro
print(Receptor_bit_paridade_par("10100110001000000010011000100110")) # Resposta com erro