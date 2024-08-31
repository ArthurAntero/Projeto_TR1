def Transmissor_crc(quadro, polinomio_gerador):
  """
    Função de deteccao de erros na camada de enlace (subcamada LLC),
    no lado do transmissor
    Recebe um quadro e um polinomio gerador e aplica o calculo de CRC
    para o quadro a ser transmitido

    Parametros:
      - quadro: string de bits sem o CRC
      - polinomia_gerador: string de bits representativos do polinomio gerador
    Retorno:
      - string de bits com o CRC
  """
  tamanho_gerador = len(polinomio_gerador)
  dividendo = quadro + "0" * tamanho_gerador
  dividendo_temp = quadro[0:tamanho_gerador]
  for i in range(0, len(quadro)):
    if (dividendo_temp[0] == "1"):
      resto = format(int(dividendo_temp, 2) ^ int(polinomio_gerador, 2), f"0{tamanho_gerador - 1}b")
    else:
      resto = format(int(dividendo_temp, 2) ^ int("0"*tamanho_gerador, 2), f"0{tamanho_gerador - 1}b")
    dividendo_temp = resto + dividendo[i + tamanho_gerador]

  return quadro + resto

def Receptor_crc(quadro, polinomio_gerador):
  """
    Função de deteccao de erros na camada de enlace (subcamada LLC),
    no lado do receptor
    Recebe um quadro e um polinomio gerador e decodifica o calculo de CRC
    para o quadro recebido

    Parametros:
      - quadro: string de bits com o CRC
      - polinomia_gerador: string de bits representativos do polinomio gerador
    Retorno:
      - um booleano (True se teve erro e False se não teve erro)
  """
  tamanho_gerador = len(polinomio_gerador)
  dividendo = quadro + "0" * tamanho_gerador
  dividendo_temp = quadro[0:tamanho_gerador]
  for i in range(0, len(quadro)):
    if (dividendo_temp[0] == "1"):
      resto = format(int(dividendo_temp, 2) ^ int(polinomio_gerador, 2), f"0{tamanho_gerador - 1}b")
    else:
      resto = format(int(dividendo_temp, 2) ^ int("0"*tamanho_gerador, 2), f"0{tamanho_gerador - 1}b")
    dividendo_temp = resto + dividendo[i + tamanho_gerador]

  return resto != "0" * (tamanho_gerador - 1)

quadro_s_crc = "11111001100"
polinomio_gerador = "100011001"
quadro_c_crc_certo = "1111100110000000111"
quadro_c_crc_errado = "1111100110000000110"

print(Transmissor_crc(quadro_s_crc, polinomio_gerador))
print(Receptor_crc(quadro_c_crc_certo, polinomio_gerador))  # sem erro
print(Receptor_crc(quadro_c_crc_errado, polinomio_gerador))  # com erro
