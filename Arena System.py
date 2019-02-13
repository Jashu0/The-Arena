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
    




def player_attack():
    global HP
    global ENEMY_HP
    
    BaseHit = HIT - ENEMY_AVD
    HITRATE = random.randint(1,99)
    CRITRATE = random.randint(1,99)
    SKILLPROCK1 = random.randint(1,99)
    SKILLPROCK2 = random.randint(1,99)
    SKILLPROCK3 = random.randint(1,99)
    SKILLPROCK4 = random.randint(1,99)
    SKILLPROCK5 = random.randint(1,99)
    DAMAGE = ATK - ENEMY_DEF
    CRITDAMAGE = DAMAGE * 3

    if HITRATE < Base_Hit:
        print(Name , 'attacks.')
        time.sleep(1.5)
        if CRITRATE < CRIT:
            print("CRITICAL HIT")
            print(Name , "deals", CRITDAMAGE,'.')
            ENEMY_HP = ENEMY_HP - CRITDAMAGE
            time.sleep(1.5)
            EXP = EXP + 30
        else:
            print(Name, "deals", DAMAGE,'.')
            ENEMY_HP = ENEMY_HP - DAMAGE
            EXP = EXP + 10
            time.sleep(1.5)
    else:
        print(Name, 'missed.')

def player_double():
    BaseHit = HIT - ENEMY_AVD
    HITRATE = random.randint(1,99)
    CRITRATE = random.randint(1,99)
    SKILLPROCK1 = random.randint(1,99)
    SKILLPROCK2 = random.randint(1,99)
    SKILLPROCK3 = random.randint(1,99)
    SKILLPROCK4 = random.randint(1,99)
    SKILLPROCK5 = random.randint(1,99)
    if ATK_SPD > ENEMY_ATK_SPD:
        HITRATE = random.randint(1,99)
        CRITRATE = random.randint(1,99)
        if HITRATE < BaseHit:
            print(Name, 'doubles.')
            time.sleep(1.5)
            if CRITRATE < CRIT:
                print("CRITICAL HIT")
                print(Name , "deals", CRITDAMAGE,'.')
                ENEMY_HP = ENEMY_HP - CRITDAMAGE
                time.sleep(1.5)
                EXP = EXP + 30
            else:
                print(Name, "deals", DAMAGE)
                ENEMY_HP = ENEMY_HP - DAMAGE
                EXP = EXP + 10
                time.sleep(1.5)
        else:
            print(Name, "missed")
            time.sleep(1.5)
            EXP = EXP + 1


def enemy_double():
    BaseHit = ENEMY_HIT - AVD
    HITRATE = random.randint(1,99)
    CRITRATE = random.randint(1,99)
    SKILLPROCK1 = random.randint(1,99)
    SKILLPROCK2 = random.randint(1,99)
    SKILLPROCK3 = random.randint(1,99)
    SKILLPROCK4 = random.randint(1,99)
    SKILLPROCK5 = random.randint(1,99)
    if ENEMY_ATK_SPD > ATK_SPD:
        HITRATE = random.randint(1,99)
        CRITRATE = random.randint(1,99)
        if HITRATE < BaseHit:
            print(ENEMY_Name, 'doubles.')
            time.sleep(1.5)
            if CRITRATE < CRIT:
                print("CRITICAL HIT")
                print(ENEMY_Name , "deals", CRITDAMAGE,'.')
                HP = HP - CRITDAMAGE
                time.sleep(1.5)
                EXP = EXP + 1
            else:
                print(ENEMY_Name, "deals", DAMAGE)
                HP = HP - DAMAGE
                EXP = EXP + 1
                time.sleep(1.5)
        else:
            print(ENEMY_Name, "missed")
            time.sleep(1.5)
            EXP = EXP + 1
