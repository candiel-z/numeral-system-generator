alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
output_length = 6 # desired code string length
alphabet_length = len(alphabet)


def encrypt(num: int) -> str:
    """Encrypts input integer to the string"""

    if num < 0 or num > alphabet_length**output_length - 1:
        raise Exception('Input number out of range')
    
    res = ''

    while len(res) != output_length:
        res += alphabet[num % alphabet_length]
        num = int(num / alphabet_length)
    
    return res[::-1]


def decrypt(code: str) -> int:
    """Decrypts input string to an integer"""

    res = 0
    for i in range(output_length):
        res += alphabet.index(code[i]) * alphabet_length**((output_length - 1) - i)
    
    return res 
