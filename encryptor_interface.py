from encryptor import Encryptor
from config import ALPHABET, MAX_OUTPUT_LEN


class EncryptorInterface(Encryptor):
    def __init__(self, 
        alphabet_len=len(ALPHABET),
        remove_unnecessary_chars=False,
    ):
        """
        
        """

        self.alphabet_len = alphabet_len
        self.remove_unnecessary_chars = remove_unnecessary_chars

        self.unsigned_range = self.alphabet_len**MAX_OUTPUT_LEN - 1
        self.io_int_range = {'min': -self.unsigned_range, 'max': self.unsigned_range}

        super(EncryptorInterface, self).__init__(alphabet_len)

    def encrypt(self, num: int) -> str:
        """"""
    
        if num < self.io_int_range['min'] or num > self.io_int_range['max']:
            raise Exception('Input integer out of range')

        code = ''

        if num >= 0: 
            code = self._Encryptor__encrypt(num)
        else: 
            code = '-' + self._Encryptor__encrypt(-num) # num is negative here

        if self.remove_unnecessary_chars: 
            code = self._remove_unnecessary_chars(code)
        return code

    def decrypt(self, code: str) -> int:
        """"""

        if code[0] == '-': 
            return -self._Encryptor__decrypt(code[1:])
        else: 
            return self._Encryptor__decrypt(code)

    def _remove_unnecessary_chars(self, code: str) -> str:
        """"""

        res = [char for char in code]

        for i in range(len(res)):
            if res[-2] == '': break
            if res[i] == self.alphabet[0]: res[i] = ''
            elif res[i] == '-': continue
            else: break
        return ''.join(res)

    def __get_range(self) -> dict:
        """"""

        return self.io_int_range

    def __set_range(self, min: int, max: int):
        """"""

        if min > max:
            raise Exception("'max' arg cannot be less than 'min'")
        if min < -self.unsigned_range or max > self.unsigned_range:
            raise Exception('"min" or "max" out of range')

        self.io_int_range['min'] = min
        self.io_int_range['max'] = max
