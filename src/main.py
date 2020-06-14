# Resolve the problem!!
import string
import random 

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')


def generate_password():

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
    return str_pass


def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
