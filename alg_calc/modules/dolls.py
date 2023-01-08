# -*- coding: utf-8 -*-
"""
Database for all dolls and viable algorithms. Please don't ask why I added __ ;-;
"""
import numpy as __np
import pandas as __pd
#%%
Mag = __pd.DataFrame(
        {
                "Name": ["Magnhilda"],
                "Doll_Class": ["Warrior"],
                
                "Offense": [["Lower Limit", "Limit Value"]],
                "Stability": [["Resolve","Encapsulate"]],
                "Special": [["Stratagem", "Delta V"]],
                
                "Off_main": [["Atk%", "Atk%"]],
                "Sta_main": [["HP%","HP%"]],
                "Spe_main": [["Haste", "Haste"]],
                
                "Off_sub": [[["HP", "Dmg"], ["Atk%", "Dmg"]]],
                "Sta_sub": [[["HP%", "DR"], ["HP%", "DR"]]],
                "Spe_sub": [[["HP", "Dodge"], ["HP", "Dodge"]]],
        }                
)    

Hatsu = __pd.DataFrame(
        {
                "Name": ["Hatsuchiri"],
                "Doll_Class": ["Warrior"],
                
                "Offense": [["MLR Matrix", "Limit Value"]],
                "Stability": [["Perception","Encapsulate"]],
                "Special": [["Paradigm", "Delta V"]],
                
                "Off_main": [["Atk%", "Atk%"]],
                "Sta_main": [["HP%","HP%"]],
                "Spe_main": [["Haste", "Haste"]],
                
                "Off_sub": [[["Atk%", "Dmg"], ["Atk%", "Dmg"]]],
                "Sta_sub": [[["Atk", "DR"], ["Atk", "DR"]]],
                "Spe_sub": [[["Atk", "Haste"], ["Atk", "Haste"]]],
        }                
)


Nascita = __pd.DataFrame(
        {
                "Name": ["Nascita"],
                "Doll_Class": ["Warrior"],
                
                "Offense": [["MLR Matrix", "Limit Value"]],
                "Stability": [["Perception","Encapsulate"]],
                "Special": [["Paradigm", "Paradigm"]],
                
                "Off_main": [["Atk%", "Atk%"]],
                "Sta_main": [["HP%","HP%"]],
                "Spe_main": [["CDmg", "CRate"]],
                
                "Off_sub": [[["Atk%", "Dmg"], ["Atk%", "Dmg"]]],
                "Sta_sub": [[["Atk", "DR"], ["Crit", "DR"]]],
                "Spe_sub": [[["Atk", "CDmg"], ["Atk", "Haste"]]],
        }                
)

Clukay = __pd.DataFrame(
        {
                "Name": ["Clukay"],
                "Doll_Class": ["Sniper"],
                
                "Offense": [["Limit Value"]],
                "Stability": [["Perception","Encapsulate"]],
                "Special": [["Cluster", "Convolution"]],
                
                "Off_main": [["Hash%"]],
                "Sta_main": [["HP","HP"]],
                "Spe_main": [["CDmgCRate"]],
                
                "Off_sub": [["Hash%", "Dmg"]],
                "Sta_sub": [[["CDmg", "CRate"], ["CDmg", "CRate"]]],
                "Spe_sub": [[["CDmg", "CRate"], ["CDmg", "CRate"]]],
        }                
)