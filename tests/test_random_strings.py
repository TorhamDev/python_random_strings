from python_random_strings import random_strings
import logging

#Log config
LOG_LEVEL = logging.INFO
my_logger = logging
my_logger.basicConfig(level=LOG_LEVEL)


def test_lowercase_letters():
    for i in range(1,100):

        my_logger.info('On count %i'%i)
        data = random_strings.random_lowercase(i)
        my_logger('Generated data %s'%data)

        assert type(data) == str
        my_logger.info('Passed')

def test_uppercase_letters():
    for i in range(1,100):

        my_logger.info('On count %i'%i)
        data = random_strings.random_uppercase(i)
        my_logger('Generated data %s'%data)

        assert type(data) == str
        my_logger.info('Passed')

def test_letters():
    for i in range(1,100):

        my_logger.info('On count %i'%i)
        data = random_strings.random_letters(i)
        my_logger('Generated data %s'%data)

        assert type(data) == str
        my_logger.info('Passed')

def test_random_digits():
    for i in range(1,100):

        my_logger.info('On count %i'%i)
        data = random_strings.random_digits(i)
        my_logger('Generated data %s'%data)

        assert type(data) == int
        my_logger.info('Passed')

def test_random_hexdigits():
    for i in range(1,100):

        my_logger.info('On count %i'%i)
        data = random_strings.random_hexdigits(i)
        my_logger('Generated data %s'%data)

        assert type(data) == str
        my_logger.info('Passed')

def test_random_octdigits():
    for i in range(1,100):

        my_logger.info('On count %i'%i)
        data = random_strings.random_octdigits(i)
        my_logger('Generated data %s'%data)

        assert type(data) == int
        my_logger.info('Passed')

def test_random_punctuation():
    for i in range(1,100):

        my_logger.info('On count %i'%i)
        data = random_strings.random_punctuation(i)
        my_logger('Generated data %s'%data)

        assert type(data) == str
        my_logger.info('Passed')

def test_random_printable():
    for i in range(1,100):

        my_logger.info('On count %i'%i)
        data = random_strings.random_printable(i)
        my_logger('Generated data %s'%data)

        assert type(data) == str
        my_logger.info('Passed')

def test_random_whitespace():
    for i in range(1,100):

        my_logger.info('On count %i'%i)
        data = random_strings.random_whitespace(i)
        my_logger('Generated data %s'%data)

        assert type(data) == str
        my_logger.info('Passed')







