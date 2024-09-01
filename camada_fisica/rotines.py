from camada_fisica.mod_digital import nrz_polar, bipolar, manchester
from camada_fisica.mod_portadora import ask, fsk, qam

def modulacao_digital(msg_pos_correcao_err_trans, cmd_mod_digital):
    """
    Função para execução da rotina de modulacao digital
    Eh operada de acordo com um cmd que define qual tipo de rotina sera executada

    Parametros:
      - msg_pos_correcao_err_trans: string de bits
      - cmd_mod_digital: comando que diz qual modulacao digital será realizada
        - final 1: NRZ Polar
        - final 2: Manchester
        - final 2: Bipolar
    """
    if cmd_mod_digital[-1] == "1": #NRZ Polar
        nrz_polar.transmissor_nrz_p(msg_pos_correcao_err_trans)
    elif cmd_mod_digital == "2": #Manchester
        manchester.transmissor_m(msg_pos_correcao_err_trans)
    elif cmd_mod_digital[-1] == "3": #Bipolar
        bipolar.transmissor_bi(msg_pos_correcao_err_trans)


def modulacao_portadora(msg_pos_correcao_err_trans, cmd_mod_portadora):
    """
    Função para execução da rotina de modulacao por portadora
    Eh operada de acordo com um cmd que define qual tipo de rotina sera executada

    Parametros:
      - msg_pos_correcao_err_trans: string de bits
      - cmd_mod_digital: comando que diz qual modulacao por portadora será realizada
        - final 1: ASK
        - final 2: FSK
        - final 2: 8QAM
    """
    if cmd_mod_portadora[-1] == "1": #ASK
        ask.transmissor_ask(msg_pos_correcao_err_trans)
    elif cmd_mod_portadora[-1] == "2": #FSK
        fsk.transmissor_fsk(msg_pos_correcao_err_trans)
    elif cmd_mod_portadora[-1] == "3": #8-QAM
        qam.transmissor_8QAM(msg_pos_correcao_err_trans)