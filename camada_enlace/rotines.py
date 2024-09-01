from camada_enlace.enquadramento import contagem_bytes, insercao_bytes
from camada_enlace.deteccao_erros import bit_paridade_par, crc
from camada_enlace.correcao_erros import hamming

def enquadramento_transmissor(bits, cmd_enquadramento):
    """
    Função para execução da rotina de enquadramento do lado transmissor
    Eh operada de acordo com um cmd que define qual tipo de rotina sera executada

    Parametros:
    - bits: string de bits
    - cmd_enquadramento: comando que diz qual enquadramento será realizado
        - final 1: contagem de bytes
        - final 2: insercao de bytes
    Retorno:
    - string de bits representando a mensagem enquadrada
    """
    if cmd_enquadramento[-1] == "1": #Contagem de caracteres
        msg_enquadrada = contagem_bytes.transmissor_cb(bits)
    elif cmd_enquadramento[-1] == "2": #Insercao de bytes ou caracteres
        msg_enquadrada = insercao_bytes.transmissor_ib(bits)
    return msg_enquadrada


def enquadramento_receptor(msg_pos_deteccao_err_rec, cmd_enquadramento):
    """
    Função para execução da rotina de enquadramento do lado receptor
    Eh operada de acordo com um cmd que define qual tipo de rotina sera executada

    Parametros:
    - msg_pos_deteccao_err_rec: string de bits
    - cmd_enquadramento: comando que diz qual enquadramento será realizado
        - final 1: contagem de bytes
        - final 2: insercao de bytes
    Retorno:
    - string de bits representando a mensagem desenquadrada
    """
    if cmd_enquadramento[-1] == "1": #Contagem de caracteres
        msg_desenquadrada = contagem_bytes.receptor_cb(msg_pos_deteccao_err_rec)
    elif cmd_enquadramento[-1] == "2": #Insercao de bytes ou caracteres
        msg_desenquadrada = insercao_bytes.receptor_ib(msg_pos_deteccao_err_rec)
    return msg_desenquadrada

def deteccao_err_transmissor(msg_enquadrada, cmd_deteccao_err):
    """
    Função para execução da rotina de deteccao de erros do lado transmissor
    Eh operada de acordo com um cmd que define qual tipo de rotina sera executada
    
    Parametros:
    - msg_enquadrada: string de bits
    - cmd_deteccao_err: comando que diz qual deteccao de erros será realizada
        - final 1: bit de paridade par
        - final 2: CRC
    Retorno:
    - string de bits representando a mensagem apos bits de validacao da deteccao de erros
    no lado transmissor
    """
    if cmd_deteccao_err[-1] == "1": #Bit de paridade par
        det_err_trans = bit_paridade_par.transmissor_bpp(msg_enquadrada)
    elif cmd_deteccao_err[-1] == "2": #CRC
        det_err_trans = crc.transmissor_crc(msg_enquadrada)
    return det_err_trans

def deteccao_err_receptor(msg_pos_correcao_err_rec, cmd_deteccao_err):
    """
    Função para execução da rotina de deteccao de erros do lado receptor
    Eh operada de acordo com um cmd que define qual tipo de rotina sera executada

    Parametros:
    - msg_pos_correcao_err_rec: string de bits
    - cmd_deteccao_err: comando que diz qual deteccao de erros será realizada
        - final 1: bit de paridade par
        - final 2: CRC
    Retorno;
    - uma tupla no formato (booleano, string):
        - booleano falando resultado da validacao (True se a mensagem eh valida e False se não)
        - string de bits representando a mensagem apos validacao na deteccao de erros
        no lado receptor
    """
    if cmd_deteccao_err[-1] == "1": #Bit de paridade par
        eh_valido, det_err_rec = bit_paridade_par.receptor_bpp(msg_pos_correcao_err_rec)
    elif cmd_deteccao_err[-1] == "2": #CRC
        eh_valido, det_err_rec = crc.receptor_crc(msg_pos_correcao_err_rec)
    return eh_valido, det_err_rec
