import numpy as np
import matplotlib.pyplot as plt

def transmissor_8QAM(entrada):
    """
    Função para gerar o sinal 8QAM a partir de uma sequência de bits.
    
    Parâmetros:
    entrada: Sequência de bits representada como uma string de '0's e '1's.
    """
    simbolos = bits_to_qam8(entrada)
    x, y = gerar_sinal_8qam(simbolos)
    plotar_sinal_8qam(x, y)

def bits_to_qam8(bits):
    """Mapeia bits para símbolos da constelação 8-QAM."""
    constelacao_8qam = {
        '000': (-1, -1),
        '001': (-1, 1),
        '010': (1, -1),
        '011': (1, 1),
        '100': (-3, -3),
        '101': (-3, 3),
        '110': (3, -3),
        '111': (3, 3),
    }
    
    simbolos = []
    for i in range(0, len(bits), 3):
        tripla = bits[i:i+3]
        if len(tripla) == 3:
            simbolos.append(constelacao_8qam[tripla])
    
    return np.array(simbolos)

def gerar_sinal_8qam(simbolos, taxa_de_amostragem=100, freq_portadora=5):
    """Gera o sinal 8-QAM modulado no tempo."""

    # Eixo x -> Tempo
    x = np.arange(0, len(simbolos), 1/taxa_de_amostragem)

    # Eixo y -> Energia do sinal
    y = np.zeros_like(x)
    
    for i, (I, Q) in enumerate(simbolos):
        y[i*taxa_de_amostragem:(i+1)*taxa_de_amostragem] = (
            I * np.cos(2 * np.pi * freq_portadora * x[i*taxa_de_amostragem:(i+1)*taxa_de_amostragem]) +
            Q * np.sin(2 * np.pi * freq_portadora * x[i*taxa_de_amostragem:(i+1)*taxa_de_amostragem])
        )
    
    return x, y

def plotar_sinal_8qam(t, sinal):
    """Plota o sinal 8-QAM gerado no tempo."""
    plt.figure(figsize=(17, 14))
    plt.plot(t, sinal, color='blue')
    plt.title("Modulação 8-QAM")
    plt.xlabel("Tempo")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
