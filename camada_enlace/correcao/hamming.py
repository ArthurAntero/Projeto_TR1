# Definição das posições dos bits de verificação
check_bits_positions = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

def Transmissor_hamming_par(msg):
  """
  Função que implementa o código de Hamming para a transmissão de uma mensagem.

  Parametros:
    - msg: string de bits sem o codigo de hamming
  Retorno:
    - string de bits com o codigo de hamming incorporado
  """
  result = []
  i = 0 # index para iterar no result
  j = 0 # index para iterar no msg
  while j < len(msg):
    if i + 1 in check_bits_positions:
      result.append("0")
      i += 1
    else:
      result.append(msg[j])
      bit_position_temp = i + 1
      k = len(check_bits_positions) - 1 # index para iterar no check_bits_positions
      while bit_position_temp > 0:
        check_bit_position = check_bits_positions[k]
        if bit_position_temp >= check_bit_position:
          result[check_bit_position - 1] = str(int(result[check_bit_position - 1], 2) ^ int(result[i], 2))
          bit_position_temp -= check_bit_position
        k -= 1
      i += 1
      j += 1
  return "".join(result)

def Receptor_hamming_par(msg):
  """
  Função que implementa o código de Hamming para a recepção de uma mensagem.

  Parametros:
    - msg: string de bits com o codigo de hamming incorporado
  Retorno:
    - uma tupla no formato (booleano, int)
      - o booleano é True caso tenha ocorrido erro e False caso não tenha ocorrido erro
      - o int é o index do bit errado
  """
  msg_bits = list(msg)
  hamming_bits = ""
  for i in range(0, len(msg_bits)):
    bit_position_temp = i + 1
    k = len(check_bits_positions) - 1 # index para iterar no check_bits_positions
    if bit_position_temp not in check_bits_positions:
      while bit_position_temp > 0:
        check_bit_position = check_bits_positions[k]
        if bit_position_temp >= check_bit_position:
          msg_bits[check_bit_position - 1] = str(int(msg_bits[check_bit_position - 1], 2) ^ int(msg_bits[i], 2))
          bit_position_temp -= check_bit_position
        k -= 1
  for i in range(len(msg_bits) - 1, -1, -1):
    if i + 1 in check_bits_positions:
      hamming_bits += msg_bits[i]
  return ("1" in hamming_bits, int(hamming_bits, 2) - 1)

# Exemplo de uso
msg = "010111"
msg_hamming_correct = "1000101011"
msg_hamming_incorrect = "1000001011"  # erro no 5º bit (index 4)
print(Transmissor_hamming_par(msg))  # esperado: 1000101011
print(Receptor_hamming_par(msg_hamming_correct))  # esperado: (False, -1)
print(Receptor_hamming_par(msg_hamming_incorrect))  # esperado: (True, 4)