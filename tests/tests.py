from python_random_strings import random_strings

def test_lowercase_letters():
    for i in range(1,100):
        assert type(random_strings.random_lowercase(i)) == str

def test_uppercase_letters():
    for i in range(1,100):
        assert type(random_strings.random_lowercase(i)) == str

def test_letters():
    for i in range(1,100):
        assert type(random_strings.random_letters(i)) == str

def test_random_digits():
    for i in range(1,100):
        assert type(random_strings.random_digits(i)) == int

def test_random_hexdigits():
    for i in range(1,100):
        assert type(random_strings.random_hexdigits(i)) == str

def test_random_octdigits():
    for i in range(1,100):
        assert type(random_strings.random_hexdigits(i)) == int

def test_random_punctuation():
    for i in range(1,100):
        assert type(random_strings.random_punctuation(i)) == str

def test_random_printable():
    for i in range(1,100):
        assert type(random_strings.random_printable(i)) == str

def test_random_whitespace():
    for i in range(1,100):
        assert type(random_strings.random_whitespace(i)) == str








