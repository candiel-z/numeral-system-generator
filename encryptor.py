from config import ALPHABET


class Encryptor(object):
    def __init__(self,
            alphabet_len,
        ):
        """
        alphabet_len -- a base of numeral system (> 1)
        """

        self._alphabet_len = alphabet_len
        self._alphabet = ALPHABET[:self._alphabet_len]

        if self._alphabet_len < 2:
            raise Exception('alphabet length cannot be less than 2')

    def encrypt(self, num: int) -> str:
        """Return input decimal integer (also negative) as code string"""

        if num >= 0: 
            return self._encrypt(num)
        else: 
            return '-' + self._encrypt(-num)

    def decrypt(self, code: str) -> int:
        """Return input code string as decimal integer."""

        if code[0] != '-': 
            return self._decrypt(code)
        else: 
            return -self._decrypt(code[1:])

    def _encrypt(self, num: int) -> str:
        """Return input decimal integer as code string"""

        res = ''
        while num > 0:
            res += self._alphabet[num % self._alphabet_len]
            num = int(num / self._alphabet_len)
        return res[::-1]

    def _decrypt(self, code: str) -> int:
        """Return input code string as decimal integer."""

        if not any(char in code for char in self._alphabet):
            raise Exception('Unknown char. Character isn`t in the alphabet')

        res = 0
        code = code[::-1]

        for i in range(len(code)):   
            res += self._alphabet.index(code[i]) * self._alphabet_len**i
        return res
