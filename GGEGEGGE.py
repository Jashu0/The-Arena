def arena_entrance():
    os.system('cls')
    print("Want to enter the arena?")
    x = input('')
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
        arena_generate()
    if x == "y":
        arena_generate()
    if x == "Yes":
        arena_generate()
    if x == 'Y':
        arena_generate()

#In case of error
    else:
        arena_enterance()

def arena_enterance():
    #Generate a random class
    x = random.randint(1,40)
    file = open( x + '.txt', 'r')
    




def rng():
    Base_Hit = HIT - ENEMY_AVD
    HITRATE = random.randint(1,99)
    CRITRATE = random.randint(1,99)
    SKILLPROCK1 = random.randint(1,99)
    SKILLPROCK2 = random.randint(1,99)
    SKILLPROCK3 = random.randint(1,99)
    SKILLPROCK4 = random.randint(1,99)
    SKILLPROCK5 = random.randint(1,99)


def player_attack():
    DAMAGE = ATK - ENEMY_DEF
    CRITDAMAGE = DAMAGE * 3
    if HITRATE < Base_Hit:
        print(Name , 'attacks.')
        time.sleep(1.5)
        if CRITRATE < CRIT:
            print("CRITICAL HIT")
            print(Name , "deals", CRITDAMAGE)
            EXP = EXP + 30
        else:
            print(Name, "deals", DAMAGE)
            EXP = EXP + 10
    else:
        print(Name, "missed")
            
        
    
    
