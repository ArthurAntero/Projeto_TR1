import numpy as np
import matplotlib.pyplot as plt

def transmissor_nrz_polar(entrada):
    """
    Função para gerar o sinal NRZ Polar a partir de uma sequência de bits.
    
    Parâmetros:
    entrada: Sequência de bits representada como uma string de '0's e '1's.
    """
    # Definição dos parâmetros
    num_bits = len(entrada)
    amostras_por_bit = 100
    V = 1  # Amplitude do sinal (V)
    
    # Sinal de saída
    y = np.array([V if bit == '1' else -V for bit in entrada for _ in range(amostras_por_bit)])
    
    # Criação do eixo X
    x = np.linspace(0, num_bits, num_bits * amostras_por_bit)

    plt.figure(figsize=(10, 4))
    plt.plot(x, y, drawstyle='steps-pre')
    plt.title('Modulação NRZ Polar')
    plt.xlabel('Tempo')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()  

def receptor_nrz_polar(sinal_recebido):
    """
    Função para demodular um sinal NRZ-Polar em uma sequência de bits.
    
    Parâmetros:
    sinal_recebido: O sinal NRZ-Polar recebido como um array NumPy.
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
        if nivel_medio > 0:
            bits_demodulados.append('1')
        else:
            bits_demodulados.append('0')

    # Converter a lista de bits em uma string de bits
    return ''.join(bits_demodulados)