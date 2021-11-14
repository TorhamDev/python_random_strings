# python random strings
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) [![Licence](https://img.shields.io/github/license/TorhamDev/python_random_strings?style=for-the-badge)](./LICENSE)

<br>

> a python lib for generate random string and digits and special characters or A combination of them


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


## Sample Code ✏️
```python

from python_random_strings import random_strings


a = random_strings.random_lowercase(6)
print(a)

a = random_strings.random_uppercase(6)
print(a)

a = random_strings.random_letters(6)
print(a)

a = random_strings.random_digits(6)
print(a)

a = random_strings.random_hexdigits(6)
print(a)

a = random_strings.random_octdigits(6)
print(a)

a = random_strings.random_punctuation(6)
print(a)

a = random_strings.random_printable(6)
print(a)

```
## sample output 📜
```bash
hueioj
GAVKDF
rENOtb
653665
c25Ba6
540322
"=*$^<
)|~6yZ

```