# Definição das posições dos bits de verificação
bits_hamming_posicoes = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

def Transmissor_hamming_par(msg):
  """
  Função que implementa o código de Hamming para a transmissão de uma mensagem.

  Parametros:
    - msg: string de bits sem o codigo de hamming
  Retorno:
    - string de bits com o codigo de hamming incorporado
  """
  resultado = []
  i = 0 # index para iterar no resultado
  j = 0 # index para iterar no msg
  while j < len(msg):
    if i + 1 in bits_hamming_posicoes:
      resultado.append("0")
      i += 1
    else:
      resultado.append(msg[j])
      bit_posicao_temp = i + 1
      k = len(bits_hamming_posicoes) - 1 # index para iterar no bits_hamming_posicoes
      while bit_posicao_temp > 0:
        bit_hamming_posicao = bits_hamming_posicoes[k]
        if bit_posicao_temp >= bit_hamming_posicao:
          resultado[bit_hamming_posicao - 1] = str(int(resultado[bit_hamming_posicao - 1], 2) ^ int(resultado[i], 2))
          bit_posicao_temp -= bit_hamming_posicao
        k -= 1
      i += 1
      j += 1
  return "".join(resultado)

def Receptor_deteccao_hamming_par(msg):
  """
  Função que implementa o código de Hamming para a recepção de uma mensagem.

  Parametros:
    - msg: string de bits com o codigo de hamming incorporado
  Retorno:
    - uma tupla no formato (booleano, int)
      - o booleano é True caso a msg seja valida e False caso a msg nao seja valida
      - o int é o index do bit errado
  """
  msg_bits = list(msg)
  hamming_bits = ""
  for i in range(0, len(msg_bits)):
    bit_posicao_temp = i + 1
    k = len(bits_hamming_posicoes) - 1 # index para iterar no bits_hamming_posicoes
    if bit_posicao_temp not in bits_hamming_posicoes:
      while bit_posicao_temp > 0:
        bit_hamming_posicao = bits_hamming_posicoes[k]
        if bit_posicao_temp >= bit_hamming_posicao:
          msg_bits[bit_hamming_posicao - 1] = str(int(msg_bits[bit_hamming_posicao - 1], 2) ^ int(msg_bits[i], 2))
          bit_posicao_temp -= bit_hamming_posicao
        k -= 1
  for i in range(len(msg_bits) - 1, -1, -1):
    if i + 1 in bits_hamming_posicoes:
      hamming_bits += msg_bits[i]
  return ("1" not in hamming_bits, int(hamming_bits, 2) - 1)

def Receptor_correcao_hamming(msg, result_deteccao_hamming):
  """
  Função que corrige uma string de bits a partir do resultado de deteccao de erros utilizando Hamming

  Parametros:
    - msg: string de bits
    - result_deteccao_hamming: uma tupla no formato (booleano, int)
      - o booleano é True caso a msg seja valida e False caso a msg nao seja valida
      - o int é o index do bit errado
  Retorno:
    - a string de bits com o erro corrigido, utilizando hamming
  """
  eh_valido, bit_errado_index = result_deteccao_hamming
  if not eh_valido:
    msg = msg[:bit_errado_index] + format(not int(msg[bit_errado_index], 2), "1b") + msg[bit_errado_index+1:]
  return msg

def Receptor_hamming_par(msg):
  result_deteccao_hamming = Receptor_deteccao_hamming_par(msg)
  msg_corrigida = Receptor_correcao_hamming(msg, result_deteccao_hamming)
  return msg_corrigida
