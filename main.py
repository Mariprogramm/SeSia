def strip_punctuation_ru(s):
    punctuations = '"! () - = + ;: /<>,.'
    new_str = ""
    for char in s:
        if char in punctuations:
            new_str += ''
        else:
            new_str += char
    new_str = new_str.replace(" ", " ")
    return " ".join(new_str.split())

print(strip_punctuation_ru(input()))


