# Definição das posições dos bits de verificação
bits_hamming_posicoes = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

def transmissor_hp(bits):
  """
  Função que implementa o código de Hamming para a transmissão de uma mensagem.

  Parametros:
  - bits: string de bits sem o codigo de hamming
  Retorno:
  - string de bits com o codigo de hamming incorporado
  """
  resultado = []
  i = 0 # index para iterar no resultado
  j = 0 # index para iterar no bits
  while j < len(bits):  # enquanto nao terminou de iterar na entrada bits
    if i + 1 in bits_hamming_posicoes:
      resultado.append("0")  # preenche com o bit 0 as posicoes de hamming na entrada bits
      i += 1  # incrementa i para continuar preenchendo o resultado
    else:
      resultado.append(bits[j])
      bit_posicao_temp = i + 1  # pega a posicao do bit (index + 1) para calcular a sua fatoracao em potencias de 2
      k = len(bits_hamming_posicoes) - 1 # index para iterar no bits_hamming_posicoes
      while bit_posicao_temp > 0: # enquanto ainda nao terminou de fatorar a posicao do bit em potencias de 2
        bit_hamming_posicao = bits_hamming_posicoes[k]
        if bit_posicao_temp >= bit_hamming_posicao:
          bit_posicao_temp -= bit_hamming_posicao
          # faz o xor do bit de posicao de hamming encontrado com o bit da posicao em fatoracao
          resultado[bit_hamming_posicao - 1] = str(int(resultado[bit_hamming_posicao - 1], 2) ^ int(resultado[i], 2))
        k -= 1  # parte para a proxima posicao de hamming
      i += 1
      j += 1
  return "".join(resultado)

def receptor_deteccao_hp(bits):
  """
  Função que implementa o código de Hamming para a recepção de uma mensagem.

  Parametros:
  - bits: string de bits com o codigo de hamming incorporado
  Retorno:
  - uma tupla no formato (booleano, int)
    - o booleano é True caso os bits sejam validos e False caso os bits sejam invalidos
    - o int é o index do bit errado
  """
  msg_bits = list(bits)
  hamming_bits = ""
  for i in range(0, len(msg_bits)):
    bit_posicao_temp = i + 1  # pega a posicao do bit (index + 1) para calcular a sua fatoracao em potencias de 2
    k = len(bits_hamming_posicoes) - 1 # index para iterar no bits_hamming_posicoes
    if bit_posicao_temp not in bits_hamming_posicoes:
      while bit_posicao_temp > 0: # enquanto ainda nao terminou de fatorar a posicao do bit em potencias de 2
        bit_hamming_posicao = bits_hamming_posicoes[k]
        if bit_posicao_temp >= bit_hamming_posicao:
          bit_posicao_temp -= bit_hamming_posicao
          # faz o xor do bit de posicao de hamming encontrado com o bit da posicao em fatoracao
          msg_bits[bit_hamming_posicao - 1] = str(int(msg_bits[bit_hamming_posicao - 1], 2) ^ int(msg_bits[i], 2))
        k -= 1 # parte para a proxima posicao de hamming
  for i in range(len(msg_bits) - 1, -1, -1):
    if i + 1 in bits_hamming_posicoes:
      hamming_bits += msg_bits[i]
  return ("1" not in hamming_bits, int(hamming_bits, 2) - 1)

def receptor_correcao_h(bits, result_deteccao_hamming):
  """
  Função que corrige uma string de bits a partir do resultado de deteccao de erros utilizando Hamming

  Parametros:
  - bits: string de bits
  - result_deteccao_hamming: uma tupla no formato (booleano, int)
    - o booleano é True caso os bits sejam validos e False caso os bits sejam invalidos
    - o int é o index do bit errado
  Retorno:
  - a string de bits com o erro corrigido, utilizando hamming
  """
  eh_valido, bit_errado_index = result_deteccao_hamming
  if not eh_valido:
    bits = bits[:bit_errado_index] + format(not int(bits[bit_errado_index], 2), "1b") + bits[bit_errado_index+1:]
  return bits

def receptor_hp(bits):
  result_deteccao_hamming = receptor_deteccao_hp(bits)
  msg_corrigida = receptor_correcao_h(bits, result_deteccao_hamming)

  dados_sem_hamming = ""
  for i in range(0, len(msg_corrigida)):
    if i + 1 not in bits_hamming_posicoes:
      dados_sem_hamming += msg_corrigida[i]

  return dados_sem_hamming