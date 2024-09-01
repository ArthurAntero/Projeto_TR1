import numpy as np
import matplotlib.pyplot as plt

def Transmissor_bipolar(entrada):
    """
    Função para gerar o sinal Bipolar a partir de uma sequência de bits.
    
    Parâmetros:
    entrada: Sequência de bits representada como uma string de '0's e '1's.
    """
    # Definição dos parâmetros
    num_bits = len(entrada)
    amostras_por_bit = 100
    V = 1  # Amplitude do sinal (V)

    # Variável de controle para alternar a polaridade dos bits '1'
    pulso = True

    # Sinal de saída
    y = np.zeros(num_bits * amostras_por_bit)

    for i, bit in enumerate(entrada):
        start_idx = i * amostras_por_bit
        end_idx = (i + 1) * amostras_por_bit
        
        if bit == '1':
            # Alterna a polaridade para cada bit '1'
            y[start_idx:end_idx] = V if pulso else -V
            pulso = not pulso  # Inverte o pulso para o próximo bit '1'
        else:
            # Bit '0' é representado por zero
            y[start_idx:end_idx] = 0

    # Criação do eixo X
    x = np.linspace(0, num_bits, num_bits * amostras_por_bit)
    
    plt.figure(figsize=(10, 4))
    plt.plot(x, y, drawstyle='steps-pre')
    plt.title('Modulação Bipolar')
    plt.xlabel('Tempo')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

def Receptor_bipolar(sinal_recebido):
    """
    Função para demodular um sinal Bipolar em uma sequência de bits.
    
    Parâmetros:
    sinal_recebido: O sinal Bipolar recebido como um array NumPy.
    """
    amostras_por_bit=100
    num_amostras = len(sinal_recebido)
    num_bits = num_amostras // amostras_por_bit
    bits_demodulados = []

    for i in range(num_bits):
        # Obter o sinal correspondente a um bit
        segmento = sinal_recebido[i * amostras_por_bit : (i + 1) * amostras_por_bit]

        # Calcular o nível médio do sinal no segmento
        nivel_medio = np.mean(segmento)

        # Decisão do bit baseado no nível médio
        if nivel_medio == 0:
            bits_demodulados.append('0')
        else:
            bits_demodulados.append('1')

    # Converter a lista de bits em uma string de bits
    return ''.join(bits_demodulados)
