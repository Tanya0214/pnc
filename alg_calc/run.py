# -*- coding: utf-8 -*-
"""
Executable
"""
import pandas as pd
import numpy as np
#%% Import library of dolls... Not actually used right now
from modules import dolls
#print([item for item in dir(dolls) if not item.startswith("__")])
#%% Pick the dolls you have... Does NOT Work!
EN = doll_database.EN
def my_dolls():
    global EN
    for item in dir(dolls):
        if item.startswith("__") != True:
            ans = input("Would you like to add {}? or {}".format(item, 'Y/N'))
            if ans == "Y":
                EN = EN.append(dolls.item) # Halp pls
            else:
                continue
    return EN
my_dolls()
#%% Select algorithms for dolls with multiple viable algorithms... Giga broken actually
from modules import select_set
Hatsu = select_set.alg_selection(dolls.Hatsu)
np.transpose([Hatsu[0:7]]) # the format later used in dumbfukjuice
# CTRL + C to terminate if you're stuck in a loop
#%% Anyways... here's the gist of my idea. Go look inside dumbfukjuice to understand
from modules import doll_database # Hand typed database like a pleb
from modules import teams # Teeeeeaam! Edit teams.py file to add/remove teams
my_teams = teams.teams
from modules import dumbfukjuice as dfj # The only part that works as intended

#%% How many Perception/enCapsulation do you need?
dfj.alg_min("PerCap",doll_database.inventory,my_teams)
#%%
'''
Output: {'HP%': 2, 'HP': 4}
'''
#%% What about unique substats?
dfj.alg_min2("PerCap",dfj.inventory,my_teams)
#%%
'''
{"HP%:{'DR', 'Atk'}": 2,
 "HP:{'DR', 'Hash'}": 2,
 "HP:{'DR', 'Atk'}": 1,
 "HP:{'CRate', 'CDmg'}": 1,
 "HP:{'Atk', 'CDmg'}": 1,
 "HP:{'DR', 'HP'}": 1}
'''
