import random
import string

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')

lengh_pass = random.randint(8,16)
array_pass=[None]*lengh_pass

for idx in range(len(array_pass)):

    if idx == 0 :
        array_pass[0] = random.choice(string.ascii_uppercase)
    elif idx == 1 :
        array_pass[1] = str(random.randint(0,9))
    elif idx % 2 == 0 and idx != 0 and idx % 3 != 0: #par, menos el 0
        array_pass[idx] = random.choice(SYMBOLS)
    elif idx % 2 == 1 and idx != 1 and idx % 3 != 0: #impar, menos el 1
        array_pass[idx] = random.choice(string.ascii_lowercase)
    elif idx % 3 == 0:
        array_pass[idx] = str(random.randint(0,9))

random.shuffle(array_pass)

str_pass =''.join(array_pass)

