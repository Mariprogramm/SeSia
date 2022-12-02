
line = 'сегодня пасмурно ==--==.'
import string
string.punctuation


for n in string.punctuation:
    if n in line:

        line = line.replace(n, '')


line.strip()

