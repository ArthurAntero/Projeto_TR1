def transformar_para_bits(msg):
    bits = ""
    for char in msg:
        bits += format(ord(char), "08b")
    return bits

def transformar_para_ascii(bits):
    msg = ""
    for byte_index in range(0, len(bits), 8):
        msg += chr(int(bits[byte_index:byte_index + 8], 2))
    return msg
