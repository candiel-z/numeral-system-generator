alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f',     # anything except '-'
            'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',     # anything except '-'
            'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',     # anything except '-'
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']               # anything except '-'
output_length = 3 # desired code string length

alphabet_length = len(alphabet)
unsigned_range = alphabet_length**output_length - 1


def encrypt(num: int, remove_unnecessary_chars=False, disable_out_of_range_exception=False) -> str:
    """Encrypts input integer to the string"""

    if (num < -unsigned_range or num > unsigned_range) and not disable_out_of_range_exception:
        raise Exception('Input number out of range')
    
    res = ''

    if num < 0:
        res = '-' + _encrypt_handler(-num)
    else:
        res = _encrypt_handler(num)

    if remove_unnecessary_chars:
        res = _remove_unnecessary_chars(res)
        if res == '': return alphabet[0]
        else: return res
    else:
        return res


def decrypt(code: str) -> int:
    """Decrypts input string to an integer"""

    if len(code.replace('-', '')) > output_length or len(code.replace('-', '')) == 0:
        raise Exception('Code length out of range')
    if not any(symbol in code for symbol in alphabet):
        raise Exception('Unknown symbol. This character isn`t in the alphabet')
    
    if len(code.replace('-', '')) < output_length:
        code = _add_unnecessary_chars(code) # if the string has the wrong length it will break the decryption

    if code[0] == '-':
        return -_decrypt_handler(code[1:])
    else:
        return _decrypt_handler(code)


def get_range():
    """Return dictionary {'min': min, 'max': max}"""

    return {'min': -unsigned_range,
            'max': unsigned_range}


def _encrypt_handler(num: int) -> str:
    """Hadle encrypting input string"""

    res = ''
    while len(res) != output_length:
        res += alphabet[num % alphabet_length]
        num = int(num / alphabet_length)
    return res[::-1]


def _decrypt_handler(code: str) -> int:
    """Handle decrypting input string"""
    res = 0
    for i in range(output_length):
        res += alphabet.index(code[i]) * alphabet_length**((output_length - 1) - i)
    return res


def _remove_unnecessary_chars(code: str) -> str:
    """Remove unnecessary characters from input string"""
    res = [char for char in code]

    for i in range(len(res)):
        if res[i] == alphabet[0]: 
            res[i] = ''
        elif res[i] == '-': continue
        else: 
            break
    return ''.join(res)


def _add_unnecessary_chars(code: str) -> str:
    """Add unnecessary characters to input string"""

    res = ''
    if code[0] == '-':
        res += '-'
    res += alphabet[0]*(output_length - len(code.replace('-', '')))
    res += code.replace('-', '')
    return res
