import numpy as np
import matplotlib.pyplot as plt

def transmissor_nrz_p(entrada):
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

    plt.figure(figsize=(17,14))
    plt.plot(x, y, drawstyle='steps-pre')
    plt.title('Modulação NRZ Polar')
    plt.xlabel('Tempo')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()  