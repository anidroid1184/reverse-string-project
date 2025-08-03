"""
Autor: Juan Sebastian Valencia Londoño
Your task for today is to write some code that reverses any string.
There are two fundamentally different ways to accomplish this,
one using a for-loop and another using string slicing.
If you can, write both solutions.
"""


def reversed_string_1(string):
    """
    Se usa el manejo de strings para retornar el string
    :param string: str
    :return: str
    """
    reversed_string = string[::-1]
    return f'The reversed string is: {reversed_string} - with algorithm 1'

def reversed_string_2(string):
    reversed_string = []
    for i in range(len(string)-1, -1, -1):
        reversed_string.append(string[i])
    reversed_string = ''.join(reversed_string)
    return f'The reversed string is: {reversed_string} - with algorithm 1'

print(reversed_string_1('Hola retorname en reversa'))
print(reversed_string_2('Hola retorname en reversa'))
