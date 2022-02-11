from python_random_strings import random_strings
import logging

#Log config
LOG_LEVEL = logging.INFO
my_logger = logging
my_logger.basicConfig(level=LOG_LEVEL)


def test_lowercase_letters():
    for i in range(1,100):
        my_logger.info('On count %i'%i)
        assert type(random_strings.random_lowercase(i)) == str
        my_logger.info('Passed')

def test_uppercase_letters():
    for i in range(1,100):
        my_logger.info('On count %i'%i)
        assert type(random_strings.random_lowercase(i)) == str
        my_logger.info('Passed')

def test_letters():
    for i in range(1,100):
        my_logger.info('On count %i'%i)
        assert type(random_strings.random_letters(i)) == str
        my_logger.info('Passed')

def test_random_digits():
    for i in range(1,100):
        my_logger.info('On count %i'%i)
        assert type(random_strings.random_digits(i)) == int
        my_logger.info('Passed')

def test_random_hexdigits():
    for i in range(1,100):
        my_logger.info('On count %i'%i)
        assert type(random_strings.random_hexdigits(i)) == str
        my_logger.info('Passed')

def test_random_octdigits():
    for i in range(1,100):
        my_logger.info('On count %i'%i)
        assert type(random_strings.random_hexdigits(i)) == int
        my_logger.info('Passed')

def test_random_punctuation():
    for i in range(1,100):
        my_logger.info('On count %i'%i)
        assert type(random_strings.random_punctuation(i)) == str
        my_logger.info('Passed')

def test_random_printable():
    for i in range(1,100):
        my_logger.info('On count %i'%i)
        assert type(random_strings.random_printable(i)) == str
        my_logger.info('Passed')

def test_random_whitespace():
    for i in range(1,100):
        my_logger.info('On count %i'%i)
        assert type(random_strings.random_whitespace(i)) == str
        my_logger.info('Passed')







