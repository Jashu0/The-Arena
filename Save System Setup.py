#Global Variables
#File Information
file = 'DUMMY'
password = 'DUMMY

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

#Eqipped Skill
skill_1 = 0
skill_2 = 0
skill_3 = 0
skill_4 = 0
skill_5 = 0

#Inventory Check (SWORD)
num_slim_swords = 0
num_bronze_swords = 0
num_iron_swords = 0
num_steel_swords = 0
num_silver_sword = 0
num_bronze_blade = 0
num_iron_blade = 0
num_steel_blade = 0
num_silver_blade = 0
num_armorslayer = 0
num_zanbato = 0
num_wing_clipper = 0
num_wyrmslayer = 0
num_rapier = 0










