def transmissor_crc(bits, polinomio_gerador="1000111"):
  """
    Função de deteccao de erros na camada de enlace (subcamada LLC),
    no lado do transmissor

    Parametros:
    - bits: string de bits sem o CRC
    - polinomia_gerador: string de bits representativos do polinomio gerador
    Retorno:
    - string de bits com o CRC
  """
  tamanho_gerador = len(polinomio_gerador)
  dividendo = bits + "0" * tamanho_gerador
  dividendo_temp = bits[0:tamanho_gerador]
  for i in range(0, len(bits)):
    if (dividendo_temp[0] == "1"):
      resto = format(int(dividendo_temp, 2) ^ int(polinomio_gerador, 2), f"0{tamanho_gerador - 1}b")
    else:
      resto = format(int(dividendo_temp, 2) ^ int("0"*tamanho_gerador, 2), f"0{tamanho_gerador - 1}b")
    dividendo_temp = resto + dividendo[i + tamanho_gerador]

  return bits + resto

def receptor_crc(bits, polinomio_gerador="1000111"):
  """
    Função de deteccao de erros na camada de enlace (subcamada LLC),
    no lado do receptor

    Parametros:
    - bits: string de bits com o CRC
    - polinomia_gerador: string de bits representativos do polinomio gerador
    Retorno:
    - uma tupla no formato (booleano, string)
      - booleano (True se os bits sao validos e False se os bits nao sao validos)
      - string de bits representando os dados sem os bits de validacao
  """
  tamanho_gerador = len(polinomio_gerador)
  dividendo = bits + "0" * tamanho_gerador
  dividendo_temp = bits[0:tamanho_gerador]
  for i in range(0, len(bits)):
    if (dividendo_temp[0] == "1"):
      resto = format(int(dividendo_temp, 2) ^ int(polinomio_gerador, 2), f"0{tamanho_gerador - 1}b")
    else:
      resto = format(int(dividendo_temp, 2) ^ int("0"*tamanho_gerador, 2), f"0{tamanho_gerador - 1}b")
    dividendo_temp = resto + dividendo[i + tamanho_gerador]

  return (resto == "0" * (tamanho_gerador - 1), bits[:-(tamanho_gerador - 1)])