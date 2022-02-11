from python_random_strings import random_strings

def test_lowercase_letters():
    for i in range(1,100):
        assert type(random_strings.random_lowercase(i)) == str
