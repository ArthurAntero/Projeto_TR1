import numpy as np
import matplotlib.pyplot as plt

def Transmissor_manchester(entrada):
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
    
    return x, y

def Receptor_manchester(sinal_recebido):
    """
    Função para demodular um sinal Manchester em uma sequência de bits.
    
    Parâmetros:
    sinal_recebido: O sinal Manchester recebido como um array NumPy.
    """
    amostras_por_bit=100
    num_amostras = len(sinal_recebido)
    num_bits = num_amostras // amostras_por_bit
    bits_demodulados = []

    # Itera por cada bit no sinal recebido
    for i in range(num_bits):
        # Dividir o sinal pela metade
        segmento_1 = sinal_recebido[i * amostras_por_bit : i * amostras_por_bit + amostras_por_bit // 2]
        segmento_2 = sinal_recebido[i * amostras_por_bit + amostras_por_bit // 2 : (i + 1) * amostras_por_bit]

        # Calcula o valor médio de cada segmento
        media_1 = np.mean(segmento_1)
        media_2 = np.mean(segmento_2)
        
        # Verifica a transição do meio do bit
        if media_1 > media_2:
            bits_demodulados.append('1')  # Transição de alto para baixo -> Bit '1'
        else:
            bits_demodulados.append('0')  # Transição de baixo para alto -> Bit '0'

    # Converter a lista de bits em uma string de bits
    return ''.join(bits_demodulados)

# Exemplo de uso
entrada = "100010000000010"
x, y = Transmissor_manchester(entrada)
bits_demodulados = Receptor_manchester(y)
print("Bits demodulados:", bits_demodulados)

# Plot do sinal Manchester
plt.figure(figsize=(10, 4))
plt.plot(x, y, drawstyle='steps-pre')
plt.title('Modulação Manchester')
plt.xlabel('Tempo')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
