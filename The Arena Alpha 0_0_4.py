#Imports
import os
import time
import random
import xlrd
#Global Values For Storing
#File Name
file = 'DUMMY'
password = 'DUMMY'
#Base Stats
Name = 'DUMMY'
Boon = 'DUMMY'
Bane = 'DUMMY'
LV = 0
HP = 0
STR = 0
MAG = 0
SKL = 0
SPD = 0
LCK = 0
DEF = 0
RES = 0
GOLD = 0
EXP = 0

#Growth Rates
HP_GROWTH = 0
STR_GROWTH = 0
MAG_GROWTH = 0
SKL_GROWTH = 0
SPD_GROWTH = 0
LCK_GROWTH = 0
DEF_GROWTH = 0
RES_GROWTH = 0

#Weapon Profeciency
sword_rank = 0
lance_rank = 0
axe_rank = 0
bow_rank = 0
dagger_rank = 0
fire_rank = 0
thunder_rank = 0
wind_rank = 0
light_rank = 0
dark_rank = 0

#Equipment Stats
weapon_name = 'Rental Weapon'
weapon_rank = 0
weapon_MT = 1
weapon_WT = 10
weapon_HIT = 50
weapon_CRIT = 0
weapon_price = 0
weapon_exp = 0
weapon_type = 'N/A'
weapon_skill = 0

#Combat Stats
ATK = STR + weapon_MT
ATK_SPD = SPD - (weapon_WT - STR)
if ATK_SPD < 0:
    ATK_SPD = 0
HIT = (SKL * 2) + weapon_HIT + (LCK // 2)
CRIT = (SKL // 2) + (weapon_CRIT)
AVD = LCK + (ATK_SPD * 2)



#Title Screen
def startup():
    os.system('cls')
    print("*********************")
    print("******THE ARENA******")
    print("*********************")
    print("")
    print("1. New Game")
    print("2. Load Game")
    print("3. Exit Game")
    option = input('')
    if option == "1":
        new_game()
    if option == '2':
        load_game()
    if option == '3':
        exit_game()
    else:
        startup()

def exit_game():
    print('Do you wish to exit?')
    x = input(str())
    if x == str('yes'):
        os.system('cls')
        print('See you next time in the arena!')
        time.sleep(2)
        exit
    if x == str('y'):
        os.system('cls')
        print('See you next time in the arena!')
        time.sleep(2)
        exit
    if x == str('no'):
        startup()
    if x == str('n'):
        startup()


#Create New Character
def new_game():
    #Clear the Screen
    os.system('cls')

    #Enter Name Of Character
    global Name
    Name = input('Enter your name: ')
    generate_stats()

#Generate Stats
def generate_stats():
    #Set Global Variables And Random Variables
    global LV
    LV = 1
    global HP
    HP = random.randint(15,25)
    global STR
    STR = random.randint(3,9)
    global MAG
    MAG = random.randint(1,5)
    global SKL
    SKL = random.randint(1,11)
    global SPD
    SPD = random.randint(1,12)
    global LCK
    LCK = random.randint(1,13)
    global DEF
    DEF = random.randint(1,10)
    global RES
    RES = random.randint(1,5)
    global GOLD
    GOLD = 1000
    new_game_stats()

def new_game_stats():
    os.system('cls')
    #Show Player Base Stats
    print('HP:', HP)
    print('Strength:', STR)
    print('Magic:', MAG)
    print('Skill:', SKL)
    print('Speed:', SPD)
    print('Luck:', LCK)
    print('Defence:', DEF)
    print('Resistance:', RES)
    confirm_stats()

def confirm_stats():
    #Ask Player If Stats Are OK
    x = input('Are these ok?: ')
    #Player Says Yes
    if x == 'yes':
        generate_growths()
    if x == 'Yes':
        generate_growths()
    if x == 'y':
        generate_growths()
    if x == 'Y':
        generate_growths()
    #Player Says No
    if x == 'no':
        generate_stats()
    if x == 'No':
        generate_stats()
    if x == 'n':
        generate_stats()
    if x == 'N':
        generate_stats()
    else:
        os.system('cls')
        new_game_stats()
        
def generate_growths():
    #Generate Growths
    global HP_GROWTH
    HP_GROWTH = random.randint(45,90)
    global STR_GROWTH
    STR_GROWTH = random.randint(45,90)
    global MAG_GROWTH
    MAG_GROWTH = random.randint(1,40)
    global SKL_GROWTH
    SKL_GROWTH = random.randint(10,60)
    global SPD_GROWTH
    SPD_GROWTH = random.randint(20,70)
    global LCK_GROWTH
    LCK_GROWTH = random.randint(15,80)
    global DEF_GROWTH
    DEF_GROWTH = random.randint(15,55)
    global RES_GROWTH
    RES_GROWTH = random.randint(15,55)
    boon()

#Choose Boon 
def boon():
    #Set Variables Global
    global HP
    global STR
    global MAG
    global SKL
    global SPD
    global LCK
    global DEF
    global RES
    
    global HP_GROWTH
    global STR_GROWTH
    global MAG_GROWTH
    global SKL_GROWTH
    global SPD_GROWTH
    global LCK_GROWTH
    global DEF_GROWTH
    global RES_GROWTH


    os.system('cls')
    #Choose Boon
    global Boon
    print('Choose Boon: "HP","STR","MAG","SKL","SPD","LCK","DEF","RES": ')
    Boon = input(str())
        #Stat and Growth Boost
    if Boon == str('HP'):
            global HP
            HP = HP + 5
            global HP_GROWTH
            HP_GROWTH = HP_GROWTH + 30
            global DEF_GROWTH
            DEF_GROWTH = DEF_GROWTH + 5
            global RES_GROWTH
            RES_GROWTH = RES_GROWTH + 5
            bane()
    if Boon == str('STR'):
            global STR
            STR = STR + 2
            global STR_GROWTH
            STR_GROWTH = STR_GROWTH + 15
            global SKL_GROWTH
            SKL_GROWTH = SKL_GROWTH + 5
            DEF_GROWTH = DEF_GROWTH + 5
            bane()
    if Boon == str('MAG'):
            global MAG
            MAG = MAG + 2
            global MAG_GROWTH
            MAG_GROWTH = MAG_GROWTH + 15
            global SPD_GROWTH
            SPD_GROWTH = SPD_GROWTH + 5
            RES_GROWTH = RES_GROWTH + 5
            bane()
    if Boon == str('SKL'):
            global SKL
            SKL = SKL + 2
            STR_GROWTH = STR_GROWTH + 5
            SKL_GROWTH = SKL_GROWTH + 15
            DEF_GROWTH = DEF_GROWTH + 5
            bane()
    if Boon == str('SPD'):
            global SPD
            SPD = SPD + 2
            SKL_GROWTH = SKL_GROWTH + 5
            SPD_GROWTH = SPD_GROWTH + 15
            global LCK_GROWTH
            LCK_GROWTH = LCK_GROWTH + 5
            bane()
    if Boon == str('LCK'):
            global LCK
            LCK = LCK + 4
            STR_GROWTH = STR_GROWTH + 5
            MAG_GROWTH = MAG_GROWTH + 5
            LCK_GROWTH = LCK_GROWTH + 15
            bane()
    if Boon == str('DEF'):
            global DEF
            DEF = DEF + 2
            LCK_GROWTH = LCK_GROWTH + 5
            DEF_GROWTH = DEF_GROWTH + 15
            RES_GROWTH = RES_GROWTH + 5
            bane()
    if Boon == str('RES'):
            global RES
            RES = RES + 2
            MAG_GROWTH = MAG_GROWTH + 5
            SPD_GROWTH = SPD_GROWTH + 5
            RES_GROWTH = RES_GROWTH + 15
            bane()
    else:
            boon()


#Choose Bane 
def bane():
    #Set Variables Global
    global HP
    global STR
    global MAG
    global SKL
    global SPD
    global LCK
    global DEF
    global RES
    
    global HP_GROWTH
    global STR_GROWTH
    global MAG_GROWTH
    global SKL_GROWTH
    global SPD_GROWTH
    global LCK_GROWTH
    global DEF_GROWTH
    global RES_GROWTH
    os.system('cls')
    #Choose Bane
    global Bane
    print('Choose Bane: "HP","STR","MAG","SKL","SPD","LCK","DEF","RES"')
    Bane = input(str())
    #Stat and Growth Reduction
    if Bane == Boon:
            print('Bane cannot be the same as Boon')
            time.sleep(1.5)
            bane()
    if Bane == str('HP'):
            global HP
            HP = HP - 3
            HP_GROWTH = HP_GROWTH - 20
            DEF_GROWTH = DEF_GROWTH - 5
            RES_GROWTH = RES_GROWTH - 5
            password_create()
    if Bane == str('STR'):
            STR = STR - 1
            STR_GROWTH = STR_GROWTH - 10
            SKL_GROWTH = SKL_GROWTH - 5
            DEF_GROWTH = DEF_GROWTH - 5
            password_create()
    if Bane == str('MAG'):
            MAG = MAG - 1
            MAG_GROWTH = MAG_GROWTH - 10
            SPD_GROWTH = SPD_GROWTH - 5
            RES_GROWTH = RES_GROWTH - 5
            password_create()
    if Bane == str('SKL'):
            SKL = SKL - 1
            STR_GROWTH = STR_GROWTH - 5
            SKL_GROWTH = SKL_GROWTH - 10
            DEF_GROWTH = DEF_GROWTH - 5
            password_create()
    if Bane == str('SPD'):
            SPD = SPD - 1
            SKL_GROWTH = SKL_GROWTH - 5
            SPD_GROWTH = SPD_GROWTH - 10
            LCK_GROWTH = LCK_GROWTH - 5
            password_create()
    if Bane == str('LCK'):
            LCK = LCK - 2
            STR_GROWTH = STR_GROWTH - 5
            MAG_GROWTH = MAG_GROWTH - 5
            LCK_GROWTH = LCK_GROWTH - 10
            password_create()
    if Bane == str('DEF'):
            DEF = DEF - 1
            LCK_GROWTH = LCK_GROWTH - 5
            DEF_GROWTH = DEF_GROWTH - 10
            RES_GROWTH = RES_GROWTH - 5
            password_create()
    if Bane == str('RES'):
            RES = RES - 1
            MAG_GROWTH = MAG_GROWTH - 5
            SPD_GROWTH = SPD_GROWTH - 5
            RES_GROWTH = RES_GROWTH - 10
            password_create()
    else:
            bane()

def password_create():
    #Create A Password
    os.system('cls')
    global password
    print('Please create a password:')
    password = input(str())
    print('Is this password ok?:')
    print(password)
    z = input()
    if z == 'yes':
        final_confirm()
    if z == 'Yes':
        final_confirm()
    if z == 'y':
        final_confirm()
    if z == 'Y':
        final_confirm()
    #Player Says No
    if z == 'no':
        password_create()
    if z == 'No':
        password_create()
    if z == 'n':
        password_create()
    if z == 'N':
        password_create()

def final_confirm():
    os.system('cls')
    print('Name:', Name)
    print('Password:', password)
    print('Boon:', Boon)
    print('Bane:', Bane)
    print('HP:', HP)
    print('Strength:', STR)
    print('Magic:', MAG)
    print('Skill:', SKL)
    print('Speed:', SPD)
    print('Luck:', LCK)
    print('Defence:', DEF)
    print('Resistance:', RES)
    print('Are these settings ok?')
    x = input()
    #Player Says Yes
    if x == 'yes':
        file_create()
    if x == 'Yes':
        file_create()
    if x == 'y':
        file_create()
    if x == 'Y':
        file_create()
    #Player Says No
    if x == 'no':
        start_over()
    if x == 'No':
        start_over()
    if x == 'n':
        start_over()
    if x == 'N':
        start_over()
    else:
        final_confirm()
    
def start_over():
    print('What would you like to change?')
    print('1. Re-Roll Stats')
    print('2. Change Boon')
    print('3. Change Bane')
    print('4. Change Password')
    print('5. Go Back')
    x = input('')
    if x == 1:
        generate_stats()
    if x == 2:
        boon()
    if x == 3:
        bane()
    if x == 4:
        password_create()
    if x == 5:
        final_confirm()
    else:
        start_over()

def file_create():
    #Create the File
    print('Creating File... Do not close the window')
    global file
    file = open(Name + '.txt','w+')

    file.write(Name + '\n')
    file.write(password + '\n')
    file.write(Boon + '\n')
    file.write(Bane + '\n')
    file.write(str(LV) + '\n')
    file.write(str(HP) + '\n')
    file.write(str(STR) + '\n')
    file.write(str(MAG) + '\n')
    file.write(str(SKL) + '\n')
    file.write(str(SPD) + '\n')
    file.write(str(LCK) + '\n')
    file.write(str(DEF) + '\n')
    file.write(str(RES) + '\n')
    file.write(str(HP_GROWTH) + '\n')
    file.write(str(STR_GROWTH) + '\n')
    file.write(str(MAG_GROWTH) + '\n')
    file.write(str(SKL_GROWTH) + '\n')
    file.write(str(SPD_GROWTH) + '\n')
    file.write(str(LCK_GROWTH) + '\n')
    file.write(str(DEF_GROWTH) + '\n')
    file.write(str(RES_GROWTH) + '\n')
    file.write(str(GOLD) + '\n')
    file.write(str(EXP) + '\n')
    
    file.close

    file = open(Name + '.txt','w+')

    file.write(Name + '\n')
    file.write(password + '\n')
    file.write(Boon + '\n')
    file.write(Bane + '\n')
    file.write(str(LV) + '\n')
    file.write(str(HP) + '\n')
    file.write(str(STR) + '\n')
    file.write(str(MAG) + '\n')
    file.write(str(SKL) + '\n')
    file.write(str(SPD) + '\n')
    file.write(str(LCK) + '\n')
    file.write(str(DEF) + '\n')
    file.write(str(RES) + '\n')
    file.write(str(HP_GROWTH) + '\n')
    file.write(str(STR_GROWTH) + '\n')
    file.write(str(MAG_GROWTH) + '\n')
    file.write(str(SKL_GROWTH) + '\n')
    file.write(str(SPD_GROWTH) + '\n')
    file.write(str(LCK_GROWTH) + '\n')
    file.write(str(DEF_GROWTH) + '\n')
    file.write(str(RES_GROWTH) + '\n')
    file.write(str(GOLD) + '\n')
    file.write(str(EXP) + '\n')
    
    file.close
    time.sleep(1.5)
    os.system('cls')
    print('File Created')
    time.sleep(1.5)
    main_menu()



def load_game():
    global Name
    global password
    os.system('cls')
    print('Enter your name: ')
    Name = input()
    print('Type the password: ')
    password = input()
    file = open(Name + '.txt','r')
    User = file.readline()
    Pass = file.readline()

    User = User.rstrip('\n')
    Pass = Pass.rstrip('\n')
    file.close
    if password == Pass:
        load_file()
    else:
        print('Password Incorrect.')
        time.sleep(0.5)
        print('Try Again?')
        x = input(str())
        if x == 'yes':
            load_game()
        if x == 'Yes':
            load_game()
        if x == 'y':
            load_game()
        if x == 'Y':
            load_game()

        if x == 'no':   
            startup()
        if x == 'No':
            startup()
        if x == 'n':
            startup()
        if x == 'N':
            startup()
        

def load_file():
    os.system('cls')
    print('Loading...')

    global file
    global password
    global Name
    global Boon
    global Bane
    global HP
    global STR
    global MAG
    global SKL
    global SPD
    global LCK
    global DEF
    global RES
    global GOLD
    global EXP
    
    global HP_GROWTH
    global STR_GROWTH
    global MAG_GROWTH
    global SKL_GROWTH
    global SPD_GROWTH
    global LCK_GROWTH
    global DEF_GROWTH
    global RES_GROWTH
    file = open(Name + '.txt','r')

    Name = str(file.readline())
    password = str(file.readline())
    Boon = str(file.readline())
    Bane = str(file.readline())
    LV = int(file.readline())
    HP = int(file.readline())
    STR = int(file.readline())
    MAG = int(file.readline())
    SKL = int(file.readline())
    SPD = int(file.readline())
    LCK = int(file.readline())
    DEF = int(file.readline())
    RES = int(file.readline())

    HP_GROWTH = int(file.readline())
    STR_GROWTH = int(file.readline())
    MAG_GROWTH = int(file.readline())
    SKL_GROWTH = int(file.readline())
    SPD_GROWTH = int(file.readline())
    LCK_GROWTH = int(file.readline())
    DEF_GROWTH = int(file.readline())
    RES_GROWTH = int(file.readline())

    GOLD = int(file.readline())
    EXP = int(file.readline())

    Name = Name.rstrip('\n')
    password = password.rstrip('\n')
    Boon = Boon.rstrip('\n')
    Bane = Bane.rstrip('\n')
    file.close

    time.sleep(1.5)
    os.system('cls')
    print('Loading Complete')
    time.sleep(1.5)

    main_menu()
        
def main_menu():
    os.system('cls')
    print('Select an option.')
    print('1. Enter Arena')
    print('2. Check Status')
    print('3. Change Equipment')
    print('4. Enter Armory')
    print('5. Enter Shop')
    print('6. Save')
    x = input()
    if x == '1':
        arean()
    if x == '2':
        status()
    if x == '3':
        equip()
    if x == '4':
        armory()
    if x == '5':
        shop()
    if x == '6':
        save_prompt()
    if x == '7':
        return_title()
    else:
        main_menu()

def status():
    os.system('cls')
    print('Name:', Name)
    print('Boon:', Boon)
    print('Bane:', Bane)
    print('HP:', HP)
    print('Strength:', STR)
    print('Magic:', MAG)
    print('Skill:', SKL)
    print('Speed:', SPD)
    print('Luck:', LCK)
    print('Defence:', DEF)
    print('Resistance:', RES)
    print('Gold:', GOLD)
    print('EXP:', EXP)
    print('Attack:', ATK)
    print('Hit Rate:', HIT)
    print('Crital Rate:', CRIT)
    print('Aovid:', AVD)

    input('Press Enter to return: ')
    main_menu()

def save_prompt():
    os.system('cls')
    print('Would you like to save?')
    x = input()
    if x == 'n':
        main_menu()
    if x == 'no':
        main_menu()
    if x == 'N':
        main_menu()
    if x == 'No':
        main_menu()

#If player says yes
    if x == "yes":
        save()
    if x == "y":
        save()
    if x == "Yes":
        save()
    if x == 'Y':
        save()

#In case of error
    else:
        save_prompt()



        

startup()
