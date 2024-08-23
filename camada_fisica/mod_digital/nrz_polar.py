import numpy as np
import matplotlib.pyplot as plt

def nrz_polar(entrada):
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

    return x, y    

# Exemplo de uso
entrada = "1011001111111111111111111"
x, y = nrz_polar(entrada)

# Plot do sinal NRZ Polar
plt.figure(figsize=(10, 4))
plt.plot(x, y, drawstyle='steps-pre')
plt.title('Modulação NRZ Polar')
plt.xlabel('Tempo')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()