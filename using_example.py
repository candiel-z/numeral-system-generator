from encryptor import Encryptor


def get(start: int, stop: int, step: int) -> None:
    """Return the numbers generator in range(start, stop, step) as dict {'encrypted': string, 'decrypted': integer}"""

    encryptor = Encryptor(62)

    for counter in range(start, stop, step):
        yield {'encrypted': encryptor.encrypt(counter), 'decrypted': counter}


def convert(convert_from: int, convert_to: int, code: str) -> str:
    """
    convert_from -- integer that represent a base of numeral system from which the conversion will take place\n
    convert_to -- integer that represent a base of numeral system to which the conversion will take place\n 
    code -- code string that will be converted\n
    Return converted string.
    """

    converter_from = Encryptor(alphabet_len=convert_from)
    converter_to = Encryptor(alphabet_len=convert_to)
    
    return converter_to.encrypt(converter_from.decrypt(str(code)))
