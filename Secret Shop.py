import os
import time


def secret_shop():
    os.system('cls')
    print("Shh... It's a secret.")
    print('1. Sacred Weapons')
    print('2. Sacred Skills')
    print('3. Stat Boosters')
    print('4. Exit')
    x = input()
    if x == str(1):
        sacred_weapon()
    if x == str(2):
        sacred_skill()
    if x == str(3):
        stat_booster()
    if x == str(4):
        exit_secret_shop()
    else:
        secret_shop()
def sacred_weapon():
    print('ass')
def sacred_skill():
    print('ass')
def stat_booster():
    print('ass')
def exit_secret_shop():
    os.system('cls')
    x = input("Leaving so soon? Yes/No ")
    if x == str('yes'):
        os.system('cls')
        print('Buh-Bye then.')
        time.sleep(2)
        main_menu
    if x == str('no'):
        os.system('cls')
        print('Hm... Then go shopping, silly.')
        time.sleep(2)
        secret_shop()
    else:
        exit_secret_shop()
secret_shop()
