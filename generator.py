from encryptor_interface import EncryptorInterface
from config import ALPHABET


class Generator(EncryptorInterface):
    def __init__(self, 
        alphabet_len=len(ALPHABET),
        autoincrement_step=1,
        remove_unnecessary_chars=False,
    ):
        """
        alphabet_len -- slice length of ALPHABET\n
        autoincrement_step -- step for generator\n
        remove_unnecessary_chars -- if True remove unused chars from code string (e.g. -00Fg0 -> -Fg0)
        """

        super(Generator, self).__init__(alphabet_len, remove_unnecessary_chars)

        self.autoincrement_step = autoincrement_step

    def get(self) -> None:
        """return generator as dict {'encrypted': string, 'decrypted': integer}
        in EncryptorInterface.io_int_range with autoincrement_step"""

        for counter in range(self.io_int_range['min'], self.io_int_range['max'], self.autoincrement_step):
            yield {'encrypted': self.encrypt(counter), 'decrypted': counter}

    def get_range(self) -> dict:
        """Return a range as dict {'min': integer, 'max': integer}"""

        return self._EncryptorInterface__get_range()

    def set_range(self, min: int, max: int) -> None:
        """
        min -- minimal value of range\n
        max -- maximal value of range\n
        max cannot be less than min
        """

        self._EncryptorInterface__set_range(min, max)


class Converter(object):
    def __init__(self):
        """
        
        """


    def convert(self, convert_from: int, convert_to: int, code: str) -> str:
        """
        convert_from -- integer that represent a base of numeral system from which the conversion will take place\n
        convert_to -- integer that represent a base of numeral system to which the conversion will take place\n 
        Return converted string
        """

        converter_from = EncryptorInterface(alphabet_len=convert_from, max_output_len=len(code), remove_unnecessary_chars=True)
        converter_to = EncryptorInterface(alphabet_len=convert_to, max_output_len=10*len(code), remove_unnecessary_chars=True)
        
        return converter_to.encrypt(converter_from.decrypt(code))
