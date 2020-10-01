from config import ALPHABET


class Encryptor(object):
    def __init__(self,
            alphabet_len,
        ):
        """
        alphabet_len -- a base of numeral system (slice length of config.ALPHABET)
        """

        self.alphabet_len = alphabet_len
        self.alphabet = ALPHABET[:self.alphabet_len]

    def __encrypt(self, num: int) -> str:
        """Return input decimal integer as code string"""

        res = ''
        while True:
            if num == 0:      
                break
            res += self.alphabet[num % self.alphabet_len]
            num = int(num / self.alphabet_len)
        return res[::-1]

    def __decrypt(self, code: str) -> int:
        """Return input code string as decimal integer."""

        if not any(char in code for char in self.alphabet):
            raise Exception('Unknown char. Character isn`t in the alphabet')

        res = 0
        code = code[::-1]

        for i in range(len(code)):   
            res += self.alphabet.index(code[i]) * self.alphabet_len**i
        return res
