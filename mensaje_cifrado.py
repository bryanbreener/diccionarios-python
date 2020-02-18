import random

def cypher(message):
    words = message.split(' ')
    cypher_message = []

    for word in words:
        cypher_word = ''
        for letter in word:
            cypher_word += new_dictionary[letter]

        cypher_message.append(cypher_word)

    return ' '.join(cypher_message)


def decipher(message):
    words = message.split(' ')
    decipher_message = []

    for word in words:
        decipher_word = ''

        for letter in word:

            for key, value in new_dictionary.items():
                if value == letter:
                    decipher_word += key

        decipher_message.append(decipher_word)

    return ' '.join(decipher_message)


def run():

    while True:

        command = str(input('''--- * --- * --- * --- * --- * --- * --- * ---

            Bienvenido a criptografia. ¿Que deseas hacer?

            [c]ifrar mensaje
            [d]ecifrar mensaje
            [s]alir
        '''))

        if command == 'c':
            message = str(input('Escribe tu mensaje: '))
            cypher_message = cypher(message)
            print(cypher_message)

        elif command == 'd':
            message = str(input('Escribe tu mensaje cifrado: '))
            decypher_message = decipher(message)
            print(decypher_message)
        elif command == 's':
            print('salir')
            return False
        else:
            print('Comando no encontrado!')


if __name__ == '__main__':

    KEYS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '?', '!']
    VALUES = ['w', 'E', 'x', '1', 'a', 't', '0', 'C', 'b', '!', 'z', '8', 'M', 'I', 'd', '.', 'U', 'Y', 'i', '3', ',', 'J', 'N', 'f', 'm', 'W', 'G', 'S', 'j', 'n', 's', 'Q', 'o', 'e', 'u', 'g', '2', '9', 'A', '5', '4', '?', 'c', 'r', 'O', 'P', 'h', '6', 'q', 'H', 'R', 'l', 'k', '7', 'X', 'L', 'p', 'v', 'T', 'V', 'y', 'K', 'Z', 'D', 'F', 'B']

    new_dictionary = {}
    new_values = []

    for key in KEYS:

        valor_repetido = False

        while valor_repetido is False:
        
            indice_random = random.randint(0, len(VALUES) - 1)
            value_random = VALUES[indice_random]

            if value_random in new_dictionary.values():
                pass
            else:
                new_values.append(value_random)
                new_dictionary[key] = value_random
                valor_repetido = True

    print('M E N S A J E S  C I F R A D O S')
    run()