from random import randint
import logging

## logger setup
log_level = logging.INFO
my_logger = logging
my_logger.basicConfig(level=log_level)
logger = my_logger.getLogger('python random strings')

# Some strings for ctype-style character classification
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
digits = '0123456789'
hexdigits = digits + 'abcdef' + 'ABCDEF'
octdigits = '01234567'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
printable = digits + ascii_letters + punctuation



class random_strings():
    """
    return random strings with length optional.
    """

    def random_lowercase(length):
        """
        return random lower ascii case
        """

        # text for return
        text_string = ''
        # for save numbers, for select chars
        selected = []
        try:
            for i in range(0,length):
                select = randint(0,len(ascii_lowercase)-1)
                selected.append(select)
        except Exception as ex:
            # return Error when length value not ivailable
            logger.error(str(ex)+f'\n your enter value is "{length}" is a {type(length)}')
        
        for char in selected:
            text_string += ascii_lowercase[char]
        
        return text_string



    def random_uppercase(length):
        """
        return random upper ascii case
        """
        # text for return
        text_string = ''
        # for save numbers, for select chars
        selected = []
        try:
            for i in range(0,length):
                select = randint(0,len(ascii_uppercase)-1)
                selected.append(select)
        except Exception as ex:
            # return Error when length value not ivailable
            logger.error(str(ex)+f'\n your enter value is "{length}" is a {type(length)}')
        
        for char in selected:
            text_string += ascii_uppercase[char]
        
        return text_string



    def random_letters(length):
        """
        return random latters ascii case
        """

        # text for return
        text_string = ''
        # for save numbers, for select chars
        selected = []
        try:
            for i in range(0,length):
                select = randint(0,len(ascii_letters)-1)
                selected.append(select)
        except Exception as ex:
            # return Error when length value not ivailable
            logger.error(str(ex)+f'\n your enter value is "{length}" is a {type(length)}')
        
        for char in selected:
            text_string += ascii_letters[char]
        
        return text_string


    def random_digits(length):
        """
        return random digits
        """

        # text for return
        text_string = ''
        # for save numbers, for select chars
        selected = []
        try:
            for i in range(0,length):
                select = randint(0,len(digits)-1)
                selected.append(select)
        except Exception as ex:
            # return Error when length value not ivailable
            logger.error(str(ex)+f'\n your enter value is "{length}" is a {type(length)}')
        
        for char in selected:
            text_string += digits[char]
        
        return text_string

    def random_hexdigits(length):
        """
        return random hex digits
        """

        # text for return
        text_string = ''
        # for save numbers, for select chars
        selected = []
        try:
            for i in range(0,length):
                select = randint(0,len(hexdigits)-1)
                selected.append(select)

        except Exception as ex:
            # return Error when length value not ivailable
            logger.error(str(ex)+f'\n your enter value is "{length}" is a {type(length)}')
        
        for char in selected:

            text_string += hexdigits[char]
        
        return text_string

    def random_octdigits(length):
        """
        return random octal digits
        """
        # text for return
        text_string = ''
        # for save numbers, for select chars
        selected = []
        try:
            for i in range(0,length):
                select = randint(0,len(octdigits)-1)
                selected.append(select)

        except Exception as ex:
            # return Error when length value not ivailable
            logger.error(str(ex)+f'\n your enter value is "{length}" is a {type(length)}')
        
        for char in selected:

            text_string += octdigits[char]
        
        return text_string
    

    def random_punctuation(length):
        """
        return random punctuation string
        """

        # text for return
        text_string = ''
        # for save numbers, for select chars
        selected = []
        try:
            for i in range(0,length):
                select = randint(0,len(punctuation)-1)
                selected.append(select)

        except Exception as ex:
            # return Error when length value not ivailable
            logger.error(str(ex)+f'\n your enter value is "{length}" is a {type(length)}')
        
        for char in selected:

            text_string += punctuation[char]
        
        return text_string


    def random_printable(length):
        """
        return random printable string
        """
        # text for return
        text_string = ''
        # for save numbers, for select chars
        selected = []
        try:
            for i in range(0,length):
                select = randint(0,len(printable)-1)
                selected.append(select)

        except Exception as ex:
            # return Error when length value not ivailable
            logger.error(str(ex)+f'\n your enter value is "{length}" is a {type(length)}')
        
        for char in selected:

            text_string += printable[char]
        
        return text_string