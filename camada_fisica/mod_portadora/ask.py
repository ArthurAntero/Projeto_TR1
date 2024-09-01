import numpy as np
import matplotlib.pyplot as plt

def Transmissor_ask(entrada):
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
    
    plt.figure(figsize=(10, 4))
    plt.plot(t, y, drawstyle='steps-pre')
    plt.title('Modulação ASK (Amplitude Shift Keying)')
    plt.xlabel('Tempo')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

def Receptor_ask(sinal_recebido):
    """
    Função para demodular um sinal ASK em uma sequência de bits.
    
    Parâmetros:
    sinal_recebido: O sinal ASK recebido como um array NumPy.
    """
    amostras_por_bit=100
    limiar=0.5
    num_amostras = len(sinal_recebido)
    num_bits = num_amostras // amostras_por_bit
    bits_demodulados = []

    for i in range(num_bits):
        # Obter o sinal correspondente a um bit
        segmento = sinal_recebido[i * amostras_por_bit : (i + 1) * amostras_por_bit]
        
        # Calcular a amplitude média do sinal no segmento
        amplitude_media = np.mean(np.abs(segmento))
        
        # Decisão do bit baseado na amplitude média
        if amplitude_media > limiar:  # Se a amplitude média é maior que o limiar, é um bit '1'
            bits_demodulados.append('1')
        else:  # Se a amplitude média é menor ou igual ao limiar, é um bit '0'
            bits_demodulados.append('0')

    # Converter a lista de bits em uma string de bits
    return ''.join(bits_demodulados)