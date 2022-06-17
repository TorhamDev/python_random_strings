"""
This module can help you generate random strings of any kind.
"""
import random
import logging
import string

# logger setup
LOG_LEVEL = logging.INFO
my_logger = logging
my_logger.basicConfig(level=LOG_LEVEL)
logger = my_logger.getLogger('python random strings')

# Some strings for ctype-style character classification
ASCII_LOWERCASE = string.ascii_lowercase
ASCII_UPPERCASE = string.ascii_uppercase
ASCII_LETTERS = string.ascii_letters
DIGITS = string.digits
HEXDIGITS = string.hexdigits
OCTDIGITS = string.octdigits
PUNCTUATION = string.punctuation
PRINTABLE = DIGITS + ASCII_LETTERS + PUNCTUATION
WHITESPACE = string.whitespace


class random_strings():
    """
    return random strings with optional length.
    """

    @staticmethod
    def random_lowercase(length: int = 1):
        """
        Returns random lower-case ascii letters.
        Args:
            length(int): desired length to generate random strings.
        Returns:
            str: Randomly generated lower-case ascii letters
        """
        selected = ''
        try:
            if length > len(ASCII_LOWERCASE):
                while length > len(selected):  # To avoid random.sample error
                    selected += ASCII_LOWERCASE

                return ''.join(random.sample(selected, length))
            else:
                return ''.join(random.sample(ASCII_LOWERCASE, length))
        except Exception as e:
            my_logger.error(e)
            return e

    @staticmethod
    def random_uppercase(length: int = 1):
        """
        Returns random upper-case ascii letters.
        Args:
            length(int): desired length to generate random strings.
        Returns:
            str: Randomly generated upper-case ascii letters
        """
        selected = ''
        try:
            if length > len(ASCII_UPPERCASE):
                while length > len(selected):  # To avoid random.sample error
                    selected += ASCII_UPPERCASE

                return ''.join(random.sample(selected, length))
            else:
                return ''.join(random.sample(ASCII_UPPERCASE, length))
        except Exception as e:
            my_logger.error('length should be an int not an %s' % type(length))
            raise TypeError('length should be an int not an %s' % type(length))

    @staticmethod
    def random_letters(length: int = 1):
        """
        Returns random ascii letters.
        Args:
            length(int): desired length to generate random strings.
        Returns:
            str: Randomly generated ascii letters
        """
        selected = ''
        try:
            if length > len(ASCII_LETTERS):  # To avoid random.sample error
                while length > len(selected):
                    selected += ASCII_LETTERS

                return ''.join(random.sample(selected, length))
            else:
                return ''.join(random.sample(ASCII_LETTERS, length))
        except Exception as e:
            my_logger.error('length should be an int not an %s' % type(length))
            raise TypeError('length should be an int not an %s' % type(length))

    @staticmethod
    def random_digits(length: int = 1):
        """
        Returns random digits.
        Args:
            length(int): desired length to generate random digits.
        Returns:
            int: Randomly generated digits.
        """
        selected = ''
        try:
            if length > len(DIGITS):  # To avoid random.sample error
                while length > len(selected):
                    selected += DIGITS

                return int(''.join(random.sample(selected, length)))
            else:
                return int(''.join(random.sample(DIGITS, length)))
        except Exception as e:
            my_logger.error('length should be an int not an %s' % type(length))
            raise TypeError('length should be an int not an %s' % type(length))

    @staticmethod
    def random_hexdigits(length: int = 1):
        """
        Returns random hexdigits.
        Args:
            length(int): desired length to generate random hexdigits.
        Returns:
            str: Randomly generated hexdigits.
        """
        selected = ''
        try:
            if length > len(HEXDIGITS):  # To avoid random.sample error
                while length > len(selected):
                    selected += HEXDIGITS

                return ''.join(random.sample(selected, length))
            else:
                return ''.join(random.sample(HEXDIGITS, length))
        except Exception as e:
            my_logger.error('length should be an int not an %s' % type(length))
            raise TypeError('length should be an int not an %s' % type(length))

    @staticmethod
    def random_octdigits(length: int = 1):
        """
        Returns random octdigits.
        Args:
            length(int): desired length to generate random octdigits.
        Returns:
            int: Randomly generated octdigits.
        """
        selected = ''
        try:
            if length > len(OCTDIGITS):  # To avoid random.sample error
                while length > len(selected):
                    selected += OCTDIGITS

                return int(''.join(random.sample(selected, length)))
            else:
                return int(''.join(random.sample(OCTDIGITS, length)))
        except Exception as e:
            my_logger.error('length should be an int not an %s' % type(length))
            raise TypeError('length should be an int not an %s' % type(length))

    @staticmethod
    def random_punctuation(length: int = 1):
        """
        Returns random punctuation.
        Args:
            length(int): desired length to generate random punctuation.
        Returns:
            str: Randomly generated punctuation.
        """
        selected = ''
        try:
            if length > len(PUNCTUATION):  # To avoid random.sample error
                while length > len(selected):
                    selected += PUNCTUATION

                return ''.join(random.sample(selected, length))
            else:
                return ''.join(random.sample(PUNCTUATION, length))
        except Exception as e:
            my_logger.error('length should be an int not an %s' % type(length))
            raise TypeError('length should be an int not an %s' % type(length))

    @staticmethod
    def random_printable(length: int = 1):
        """
        Returns random printable chars.
        Args:
            length(int): desired length to generate random letters.
        Returns:
            str: Randomly generated printable letters.
        """
        selected = ''
        try:
            if length > len(PRINTABLE):  # To avoid random.sample error
                while length > len(selected):
                    selected += PRINTABLE

                return ''.join(random.sample(selected, length))
            else:
                return ''.join(random.sample(PRINTABLE, length))
        except Exception as e:
            my_logger.error('length should be an int not an %s' % type(length))
            raise TypeError('length should be an int not an %s' % type(length))

    @staticmethod
    def random_whitespace(length: int = 1):
        """
        Returns random whitespace.
        Args:
            length(int): desired length to generate random whitespace.
        Returns:
            str: Randomly generated whitespace.
        """

        selected = ''
        try:
            if length > len(WHITESPACE):  # To avoid random.sample error
                while length > len(selected):
                    selected += WHITESPACE

                return ''.join(random.sample(selected, length))
            else:
                return ''.join(random.sample(WHITESPACE, length))
        except Exception as e:
            my_logger.error(e)
            raise TypeError('length should be an int not an %s' % type(length))
