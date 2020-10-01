from encryptor import Encryptor
from config import ALPHABET


class EncryptorInterface(Encryptor):
    def __init__(self, 
        alphabet_len,
    ):
        """
        alphabet_len -- a base of numeral system (slice length of config.ALPHABET)
        """

        super(EncryptorInterface, self).__init__(alphabet_len=alphabet_len)

    def encrypt(self, num: int) -> str:
        """Return input decimal integer (also negative) as code string"""

        res = ''

        if num >= 0: 
            res = self._Encryptor__encrypt(num)
        else: 
            res = '-' + self._Encryptor__encrypt(-num) # num is negative here

        return res

    def decrypt(self, code: str) -> int:
        """Return input code string as decimal integer."""

        if code[0] != '-': 
            return self._Encryptor__decrypt(code)
        else: 
            return -self._Encryptor__decrypt(code[1:])
