'''
random_strings tests.
'''
import logging
from python_random_strings import random_strings

#Log config
LOG_LEVEL = logging.INFO
my_logger = logging
my_logger.basicConfig(level=LOG_LEVEL)


def test_lowercase_letters():
    '''
    Test random_strings lowercase function
    '''
    for i in range(1,100):

        my_logger.info('On count %i'%i)
        data = random_strings.random_lowercase(i)
        my_logger.info('Generated data %s'%data)

        assert isinstance(data,str)
        my_logger.info('Passed')

def test_uppercase_letters():
    '''
    Test random_strings upper function
    '''
    for i in range(1,100):

        my_logger.info('On count %i'%i)
        data = random_strings.random_uppercase(i)
        my_logger.info('Generated data %s'%data)

        assert isinstance(data,str)
        my_logger.info('Passed')

def test_letters():
    '''
    Test random_strings letters function
    '''
    for i in range(1,100):

        my_logger.info('On count %i'%i)
        data = random_strings.random_letters(i)
        my_logger.info('Generated data %s'%data)

        assert isinstance(data,str)
        my_logger.info('Passed')

def test_random_digits():
    '''
    Test random_strings digits function
    '''
    for i in range(1,100):

        my_logger.info('On count %i'%i)
        data = random_strings.random_digits(i)
        my_logger.info('Generated data %s'%data)

        assert isinstance(data,int)
        my_logger.info('Passed')

def test_random_hexdigits():
    '''
    Test random_strings hexdigits function
    '''
    for i in range(1,100):

        my_logger.info('On count %i'%i)
        data = random_strings.random_hexdigits(i)
        my_logger.info('Generated data %s'%data)

        assert isinstance(data,str)
        my_logger.info('Passed')

def test_random_octdigits():
    '''
    Test random_strings octdigits function
    '''
    for i in range(1,100):

        my_logger.info('On count %i'%i)
        data = random_strings.random_octdigits(i)
        my_logger.info('Generated data %s'%data)

        assert isinstance(data,int)
        my_logger.info('Passed')

def test_random_punctuation():
    '''
    Test random_strings punctuation function
    '''
    for i in range(1,100):

        my_logger.info('On count %i'%i)
        data = random_strings.random_punctuation(i)
        my_logger.info('Generated data %s'%data)

        assert isinstance(data,str)
        my_logger.info('Passed')

def test_random_printable():
    '''
    Test random_strings printable function
    '''
    for i in range(1,100):

        my_logger.info('On count %i'%i)
        data = random_strings.random_printable(i)
        my_logger.info('Generated data %s'%data)

        assert isinstance(data,str)
        my_logger.info('Passed')

def test_random_whitespace():
    '''
    Test random_strings whitespace function
    '''
    for i in range(1,100):

        my_logger.info('On count %i'%i)
        data = random_strings.random_whitespace(i)
        my_logger.info('Generated data %s'%data)

        assert isinstance(data,str)
        my_logger.info('Passed')