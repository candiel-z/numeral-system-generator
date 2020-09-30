from config import ALPHABET, MAX_OUTPUT_LEN


class Encryptor(object):
    def __init__(self,
            alphabet_len=len(ALPHABET),
        ):
        """

        """

        self.max_output_len = MAX_OUTPUT_LEN
        self.alphabet_len = alphabet_len

        self.alphabet = ALPHABET[:self.alphabet_len]

    def __encrypt(self, num: int) -> None:
        """"""

        res = ''
        while len(res) != self.max_output_len:
            # performance when num << unsigned_range
            if num == 0: 
                res += self.alphabet[0]*(self.max_output_len - len(res))      
                break
            res += self.alphabet[num % self.alphabet_len]
            num = int(num / self.alphabet_len)
        return res[::-1]

    def __decrypt(self, code: str) -> int:
        """"""

        if not any(char in code for char in self.alphabet):
            raise Exception(f'Unknown char. Character isn`t in the alphabet')
        if len(code) > self.max_output_len:
            raise Exception('Code length out of range')
        elif len(code) < self.max_output_len:
            code = code.rjust(self.max_output_len, self.alphabet[0])

        res = 0
        for i in range(self.max_output_len):
            # performance when len(code) << max_output_len
            if code[i] == self.alphabet[0]: continue     
            res += self.alphabet.index(code[i]) * self.alphabet_len**((self.max_output_len - 1) - i)
        return res

