import random
import string


def generate(letters=0, digits=0, symbols=0, length=0):
    chars = []
    if letters or digits or symbols:
        for i in range(letters):
            chars.append(random.choice(string.ascii_letters))
        for i in range(digits):
            chars.append(random.choice(string.digits))
        for i in range(symbols):
            chars.append(random.choice(string.punctuation))
        random.shuffle(chars)
        return ''.join(chars)

    for i in range(length):
        chars.append((random.choice(string.ascii_letters + string.digits + string.punctuation)))
    random.shuffle(chars)
    return ''.join(chars)

