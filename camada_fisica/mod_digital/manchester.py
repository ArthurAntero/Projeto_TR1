import numpy as np
import matplotlib.pyplot as plt

def transmissor_m(entrada):
    """
    Função para gerar o sinal Manchester a partir de uma sequência de bits.
    
    Parâmetros:
    entrada: Sequência de bits representada como uma string de '0's e '1's.
    """
    # Definição dos parâmetros
    num_bits = len(entrada)
    amostras_por_bit = 100
    V = 1  # Amplitude do sinal (V)

    # Sinal de saída
    y = np.zeros(num_bits * amostras_por_bit)

    for i, bit in enumerate(entrada): # Variável auxiliar "i" para calcular o início, meio e final do bit
        start_idx = i * amostras_por_bit
        mid_idx = start_idx + amostras_por_bit // 2
        end_idx = (i + 1) * amostras_por_bit

        if bit == '1':
            # Para bit '1': alta (V) para metade e baixa (-V) para a outra metade
            y[start_idx:mid_idx] = V
            y[mid_idx:end_idx] = -V
        else:
            # Para bit '0': baixa (-V) para metade e alta (V) para a outra metade
            y[start_idx:mid_idx] = -V
            y[mid_idx:end_idx] = V

    # Criação do eixo X
    x = np.linspace(0, num_bits, num_bits * amostras_por_bit)
    
    plt.figure(figsize=(17,14))
    plt.plot(x, y, drawstyle='steps-pre')
    plt.title('Modulação Manchester')
    plt.xlabel('Tempo')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show(block=True)