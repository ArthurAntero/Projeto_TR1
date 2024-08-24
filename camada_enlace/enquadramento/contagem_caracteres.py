def Transmissor_contagem_caractere(entrada):
    """
    Função para realizar o enquadramento de uma string de entrada utilizando contagem de caracteres.
    
    Parâmetros:
    - entrada: String de entrada que será enquadrada.
    """
    tamanho_quadro=6
    
    # Converter a string de entrada em uma lista de caracteres
    lista = list(entrada)
    comprimento_total = len(lista)

    # Se o comprimento total for menor ou igual ao tamanho do quadro, apenas adicionar o comprimento no início
    if comprimento_total <= tamanho_quadro:
        lista.insert(0, str(comprimento_total))
    else:
        # Quebra a entrada em múltiplos quadros
        aux1 = comprimento_total % tamanho_quadro  # Caracteres restantes após os quadros completos
        num_quadros_completos = comprimento_total // tamanho_quadro  # Número de quadros completos
        
        # Inserir o comprimento do primeiro quadro completo
        lista.insert(0, str(tamanho_quadro))
        
        # Inserir comprimento dos quadros intermediários (todos são completos com o tamanho máximo)
        for i in range(1, num_quadros_completos):
            lista.insert(i * (tamanho_quadro + 1), str(tamanho_quadro))
        
        # Inserir comprimento do último quadro (caso haja um quadro incompleto)
        if aux1 != 0:
            lista.insert(num_quadros_completos * (tamanho_quadro + 1), str(aux1))

    return lista

def Receptor_contagem_caractere(entrada):
    """
    Função para decodificar uma string de entrada usando o método de enquadramento por contagem de caracteres.
    
    Parâmetros:
    - entrada: Lista de caracteres recebida do transmissor, que inclui a contagem de caracteres no início de cada quadro.
    """
    
    resultado = []  # Lista para armazenar os caracteres decodificados
    i = 0  # Índice para percorrer a lista de entrada

    while i < len(entrada):
        # O primeiro caractere de cada quadro é o número de caracteres desse quadro
        num_caracteres = int(entrada[i])  # Converte a contagem de caracteres para um número inteiro
        i += 1  # Move para o primeiro caractere real do quadro

        # Extrai os caracteres do quadro atual baseado na contagem
        quadro = entrada[i:i + num_caracteres]
        resultado.extend(quadro)  # Adiciona os caracteres decodificados ao resultado final

        # Move o índice para o próximo quadro
        i += num_caracteres

    return ''.join(resultado)  # Converte a lista de caracteres de volta para uma string

# Exemplo de uso
entrada = "ABcd46111111"
resultado_transmissor = Transmissor_contagem_caractere(entrada)
print(resultado_transmissor) 
resultado_receptor = Receptor_contagem_caractere(resultado_transmissor)
print(resultado_receptor) 
