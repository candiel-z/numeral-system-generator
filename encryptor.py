ALPHABET = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f',     
            'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',     
            'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',     
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']               
FROM_BASE = len(ALPHABET)
TO_BASE = len(ALPHABET)


def negative_support(func):
    def wrapper(val, base):
        if val[0] == '-':
            return '-' + func(val[1:], base)
        else: 
            return func(val, base)
    return wrapper 

@negative_support
def from_decimal(val: str, base: int = FROM_BASE) -> str:
    """
    :param val: string in the number system with base 10
    :returns: :param val: converted to number system with base :param base:
    """

    res = ''
    val = int(val)
    alphabet = ALPHABET[:base]

    if val == 0: return '0'

    while val != 0:
        res += alphabet[val % base]
        val = int(val / base)
    return res[::-1]

@negative_support
def to_decimal(val: str, base: int = TO_BASE) -> str:
    """
    :param val: string in the number system with base :param base:
    :returns: :param val: converted to number system with base 10
    """

    res = 0
    val = val[::-1]
    alphabet = ALPHABET[:base]

    for i in range(len(val)):   
        res += alphabet.index(val[i]) * base**i
    return str(res)

print(to_decimal(from_decimal('1024', 62), 62))
