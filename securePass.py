import random
import string
import os


def clear():
    os.system('cls')


blue = '\033[1;34;48m'
green = '\033[1;32;48m'
red = '\033[1;31;48m'

l_chars = string.ascii_lowercase
u_chars = string.ascii_uppercase
n_chars = string.digits
p_chars = string.punctuation
hesap = l_chars + u_chars + n_chars + p_chars

banner = f'''
{green}| {blue}Python SecurePass {green}\----------------------------\n
'''
while True:
    clear()
    print(banner)
    lenght = input(f'{blue}> {green}Password uzunluğu : {red}')
    data = random.sample(hesap, int(lenght))
    password = ''.join(data)
    clear()
    print(banner)
    print(f"{blue}>{green} Password : {red}" + password)
    soru = input(f'{blue}> {green}Yeni şifre (y/n) : {red}')
    if soru in 'y' or soru in 'Y':
        continue
    else:
        exit()
