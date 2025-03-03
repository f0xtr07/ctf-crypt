import base64
import binascii as ascii
import codecs

def hex2b64(hex_input) -> str:
    to_hex = bytes.fromhex(str(hex_input))
    to_b64 = base64.b64encode(to_hex)
    return to_b64.decode('utf-8')

def b64tohex(b64encoded_input) -> bytes:
    b64_string = b64encoded_input
    b64_dec = base64.b64decode(b64_string)
    dec2hex = b64_dec.hex()
    return dec2hex

def hex2ascii(hex_raw) -> str:
    if TypeError in print(hex(hex_raw)): //debugging this currently
        print(hex_raw)
    else:
        print(hex(hex_raw))

def ascii2hex(ascii_raw) -> bytes:
    ascii_parse = str(ascii_raw).encode()
    ascii2hex = ascii.hexlify(ascii_parse)
    return ascii2hex.decode()

def any2hex(any_valu) -> bytes:
    input_any = bytes.fromhex(any_valu)
    return input_any.decode()
