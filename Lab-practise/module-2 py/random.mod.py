import random

"""x=random.random()
print(x)

y=random.randint(1111,9999)
print(y)

z=random.randrange(11111111,99999999,140)
print(z)"""

captcha=['12hr','ytru','gjkenv','iwbgrio','egtrhg']
a=random.choice(captcha)
print(a)

random.shuffle(captcha)
print(captcha)
