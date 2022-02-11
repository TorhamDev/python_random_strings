# python random strings
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) [![Licence](https://img.shields.io/github/license/TorhamDev/python_random_strings?style=for-the-badge)](./LICENSE)

<br>

> a python library to generate random strings and digits and special characters or a combination of them


## installation 🛠

```bash
pip install python-random-strings
```

## options 🖇
1. Random Lower Case
2. Random Upper Case
3. Random Letters
4. Random Digits
5. Random Hex Digits
6. Random Oct Digits
7. Random Punctuation
8. Random Printable
9. Random Whitespace


## Sample Code ✏️
```python

from python_random_strings import random_strings


a = random_strings.random_lowercase(6)
print(a)
output => hueioj

a = random_strings.random_uppercase(6)
print(a)
output => GAVKDF

a = random_strings.random_letters(6)
print(a)
output => rENOtb

a = random_strings.random_digits(6)
print(a)
output => 653665

a = random_strings.random_hexdigits(6)
print(a)
output => c25Ba6

a = random_strings.random_octdigits(6)
print(a)
output => 540322

a = random_strings.random_punctuation(6)
print(a)
output => "=*$^<

a = random_strings.random_printable(6)
print(a)
output => )|~6yZ

a = random_strings.random_whitespace(6)
print(a)
output => \t\n\r\t\n\x0c
```
