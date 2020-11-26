ALPHABET = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f',     
            'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',     
            'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',     
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']               


alphabet_len = 62 # len(ALPHABET)
alphabet = ALPHABET[:alphabet_len]

def encrypt(num: int) -> str:
    """
    Return input decimal integer as code string
    """

    res = ''
    while num != 0:
        res += alphabet[num % alphabet_len]
        num = int(num / alphabet_len)
    return res[::-1]

def decrypt(code: str) -> int:
    """
    Return input code string as decimal integer.
    """

    res = 0
    code = code[::-1]

    for i in range(len(code)):   
        res += alphabet.index(code[i]) * alphabet_len**i
    return res
