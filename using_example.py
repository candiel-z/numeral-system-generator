from encryptor_interface import EncryptorInterface
from config import ALPHABET


class Generator(EncryptorInterface):
    def __init__(self, 
        alphabet_len=len(ALPHABET),
    ):
        """
        alphabet_len -- slice length of ALPHABET\n
        """

        super(Generator, self).__init__(alphabet_len)

    def get(self, start: int, stop: int, step: int) -> None:
        """Return the numbers generator in range(start, stop, step) as dict {'encrypted': string, 'decrypted': integer}"""

        for counter in range(start, stop, step):
            yield {'encrypted': self.encrypt(counter), 'decrypted': counter}


class Converter(object):
    def __init__(self):
        """
        
        """


    def convert(self, convert_from: int, convert_to: int, code: str) -> str:
        """
        convert_from -- integer that represent a base of numeral system from which the conversion will take place\n
        convert_to -- integer that represent a base of numeral system to which the conversion will take place\n 
        code -- code string that will be converted\n
        Return converted string.
        """

        converter_from = EncryptorInterface(alphabet_len=convert_from)
        converter_to = EncryptorInterface(alphabet_len=convert_to)
        
        return converter_to.encrypt(converter_from.decrypt(str(code)))
