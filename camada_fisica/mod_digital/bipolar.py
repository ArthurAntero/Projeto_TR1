import numpy as np
import matplotlib.pyplot as plt

def transmissor_bi(entrada):
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
    
    plt.figure(figsize=(17,14))
    plt.plot(x, y, drawstyle='steps-pre')
    plt.title('Modulação Bipolar')
    plt.xlabel('Tempo')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()
