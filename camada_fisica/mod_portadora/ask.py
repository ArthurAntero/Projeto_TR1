import numpy as np
import matplotlib.pyplot as plt

def ask(entrada):
    """
    Função para gerar o sinal ASK (Amplitude Shift Keying) a partir de uma sequência de bits.
    
    Parâmetros:
    entrada: Sequência de bits representada como uma string de '0's e '1's.
    """
    # Definição dos parâmetros
    freq_portadora=1 # Frequência da portadora em Hz
    amostras_por_bit=100
    num_bits = len(entrada)
    V = 1  # Amplitude máxima do sinal

    # Criação do eixo X
    t = np.linspace(0, num_bits, num_bits * amostras_por_bit, endpoint=False)

    # Sinal de saída
    y = np.zeros(num_bits * amostras_por_bit)

    for i, bit in enumerate(entrada):
        if bit == '1':
            # Calcula a senoide para o bit '1'
            y[i * amostras_por_bit:(i + 1) * amostras_por_bit] = V * np.sin(2 * np.pi * freq_portadora * t[i * amostras_por_bit:(i + 1) * amostras_por_bit])
        # Se for '0', a amplitude é zero, o que já é o padrão no vetor y
    
    return t, y

# Exemplo de uso
entrada = "10110011001111111111111111"
t, y = ask(entrada)

# Plot do sinal ASK
plt.figure(figsize=(10, 4))
plt.plot(t, y, drawstyle='steps-pre')
plt.title('Modulação ASK (Amplitude Shift Keying)')
plt.xlabel('Tempo')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
