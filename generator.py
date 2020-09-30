from encryptor_interface import EncryptorInterface
from config import ALPHABET


class Generator(EncryptorInterface):
    def __init__(self, 
        alphabet_len=len(ALPHABET),
        autoincrement_step=1,
        remove_unnecessary_chars=False,
    ):
        """
        
        """

        super(Generator, self).__init__(alphabet_len, remove_unnecessary_chars)

        self.autoincrement_step = autoincrement_step

    def get(self):
        """"""

        for counter in range(self.io_int_range['min'], self.io_int_range['max'], self.autoincrement_step):
            yield {'encrypted': self.encrypt(counter), 'decrypted': counter}

    def get_range(self) -> dict:
        """"""

        return self._EncryptorInterface__get_range()

    def set_range(self, min: int, max: int):
        """"""

        self._EncryptorInterface__set_range(min, max)
