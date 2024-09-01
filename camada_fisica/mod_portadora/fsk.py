import numpy as np
import matplotlib.pyplot as plt

def transmissor_fsk(entrada):
    """
    Função para gerar o sinal FSK (Frequency Shift Keying) a partir de uma sequência de bits.
    
    Parâmetros:
    entrada: Sequência de bits representada como uma string de '0's e '1's.
    """
    # Definição dos parâmetros
    freq_portadora=1
    amostras_por_bit=100
    num_bits = len(entrada)
    V = 1  # Amplitude máxima do sinal

    # Criação do eixo X
    t = np.linspace(0, num_bits, num_bits * amostras_por_bit, endpoint=False)

    # Sinal de saída
    y = np.zeros(num_bits * amostras_por_bit)

    for i, bit in enumerate(entrada):
        if bit == '1':
            # Calcula a senoide para o bit '1' com frequência freq_1
            y[i * amostras_por_bit:(i + 1) * amostras_por_bit] = V * np.sin(2 * np.pi * 2*freq_portadora * t[i * amostras_por_bit:(i + 1) * amostras_por_bit])
        else:
            # Calcula a senoide para o bit '0' com frequência freq_0
            y[i * amostras_por_bit:(i + 1) * amostras_por_bit] = V * np.sin(2 * np.pi * freq_portadora * t[i * amostras_por_bit:(i + 1) * amostras_por_bit])
    
    
    plt.figure(figsize=(10, 4))
    plt.plot(t, y)
    plt.title('Modulação FSK (Frequency Shift Keying)')
    plt.xlabel('Tempo')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()


