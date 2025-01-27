import random, string

str = string.digits+string.ascii_letters
r = random.choices(str, k=8)
random.shuffle(r)
r = ''.join(r)
print(str, r)