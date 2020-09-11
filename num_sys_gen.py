ALPHABET = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f',     # anything except '-'
            'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',     # anything except '-'
            'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',     # anything except '-'
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']               # anything except '-'


class NumeralSystemGenerator(object):
    def __init__(self, 
        max_output_length=6,
        custom_alphabet_length=len(ALPHABET),
        autoincrement_step=1,
        autoincrement=False,
        disable_negative_numbers=False,
        disable_out_of_range_exception=False,
        remove_unnecessary_chars=False,
    ):
        """
        max_output_length --                maximum output code string length not including '-'\n
        custom_alphabet_length --           slice length from ALPHABET\n
        disable_negative_numbers --         num < 0 will raise 'Input number out of range' exception\n
        disable_out_of_range_exception --   num > range will be counted from the begginning (130/(-127 -- 128) -> -126)\n
        remove_unnecessary_chars --         remove unused characters from the code string (-000F0 -> -F0)
        """

        self.alphabet = ALPHABET[:custom_alphabet_length]
        self.max_output_length = max_output_length

        self.alphabet_length = len(self.alphabet)
        self.unsigned_range = self.alphabet_length**self.max_output_length - 1

        self.disable_negative_numbers = disable_negative_numbers
        self.disable_out_of_range_exception = disable_out_of_range_exception
        self.remove_unnecessary_chars = remove_unnecessary_chars

        self.autoincrement_step = autoincrement_step
        self.autoincrement = autoincrement
        if self.autoincrement:
            self.counter = self.get_range()['min'] - 1

    def next(self):
        """Return dict {'encrypted': string, 'decrypted': integer}"""

        if not self.autoincrement:
            raise Exception('Can`t use next() with autoincrement == False')

        self.counter += self.autoincrement_step
        return {'encrypted': self.encrypt(self.counter), 'decrypted': self.counter}
                                                    # or 'decrypted': self.decrypt(self.encrypt(self.counter))
    def encrypt(self, num: int) -> str:
        """Encrypt input integer to code string"""

        if (((num < -self.unsigned_range or num > self.unsigned_range) or 
            ((num < 0 or num > self.unsigned_range) and self.disable_negative_numbers)) and 
              not self.disable_out_of_range_exception):
            raise Exception('Input number out of range')

        res = ''

        if num < 0:
            res = '-' + self._encrypt_handler(-num) # -(-num) = +num
        else:
            res = self._encrypt_handler(num)

        if self.remove_unnecessary_chars:
            res = self._remove_unnecessary_chars(res)
            if res == '': return self.alphabet[0]
            else: return res
        else:
            return res

    def decrypt(self, code: str) -> int:
        """Decrypt input code string to integer"""

        if len(code.replace('-', '')) > self.max_output_length or len(code.replace('-', '')) == 0:
            raise Exception('Code length out of range')
        if not any(symbol in code for symbol in self.alphabet):
            raise Exception('Unknown symbols. This characters aren`t in the alphabet')
        
        if len(code.replace('-', '')) < self.max_output_length:
            code = self._add_unnecessary_chars(code) # if the string has the wrong length it will break the decryption

        if code[0] == '-':
            return -self._decrypt_handler(code[1:])
        else:
            return self._decrypt_handler(code)

    def get_range(self):
        """Return range as dict {'min': min, 'max': max}"""

        if self.disable_negative_numbers:
            return {'min': 0,
                    'max': self.unsigned_range}
        else:
            return {'min': -self.unsigned_range,
                    'max': self.unsigned_range}

    def _encrypt_handler(self, num: int) -> str:
        """Hadle encrypting input string"""

        res = ''
        while len(res) != self.max_output_length:
            res += self.alphabet[num % self.alphabet_length]
            num = int(num / self.alphabet_length)
        return res[::-1]


    def _decrypt_handler(self, code: str) -> int:
        """Handle decrypting input string"""

        res = 0
        for i in range(self.max_output_length):
            res += self.alphabet.index(code[i]) * self.alphabet_length**((self.max_output_length - 1) - i)
        return res

    def _remove_unnecessary_chars(self, code: str) -> str:
        """Remove unnecessary characters from code string"""

        res = [char for char in code]

        for i in range(len(res)):
            if res[i] == self.alphabet[0]: res[i] = ''
            elif res[i] == '-': continue
            else: break
        return ''.join(res)


    def _add_unnecessary_chars(self, code: str) -> str:
        """Return full length code (include unnecessary chars)"""

        res = ''
        if code[0] == '-': res += '-'
        res += self.alphabet[0]*(self.max_output_length - len(code.replace('-', '')))
        res += code.replace('-', '')
        return res
