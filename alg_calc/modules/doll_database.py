# -*- coding: utf-8 -*-
"""
Doll database. DataFrame has been scrapped for now. Scroll down for current implementation via arrays.
"""
import numpy as np
import pandas as pd

#from dolls import *
#%% Initializing the DataFrame with my waifu
EN = pd.DataFrame(
        {
                "Name": ["Magnhilda"],
                "Doll_Class": ["Warrior"],
                
                "Offense": [["Lower Limit", "Limit Value"]],
                "Stability": [["Resolve","Encapsulate"]],
                "Special": [["Stratagem", "Delta V"]],
                
                "Off_main": [["Atk%", "Atk%"]],
                "Sta_main": [["HP%","HP%"]],
                "Spe_main": [["Haste", "Haste"]],
                
                "Off_sub": [[["HP", "DI"], ["Atk%", "DI"]]],
                "Sta_sub": [[["HP%", "DR"], ["HP%", "DR"]]],
                "Spe_sub": [[["HP", "Dodge"], ["HP", "Dodge"]]],        
        }
)
#%% Adding more dolls to the database

def add_raw(database, Name, Doll_Class, Offense, Stability, Special, Off_main, Sta_main, Spe_main, Off_sub, Sta_sub, Spe_sub):
    row = pd.DataFrame(
            {
                # Check input format follows "Magnhilda" and "Warrior" respectively
                "Name": [Name],
                "Doll_Class": [Doll_Class],
                
                # Check input format follows ["Lower Limit%", "Limit Value"]
                "Offense": [Offense],
                "Stability": [Stability],
                "Special": [Special],
                
                # Check input format follows ["Atk%", "Atk%"]
                "Off_main": [Off_main],
                "Sta_main": [Sta_main],
                "Spe_main": [Spe_main],
                # Check input format follows [["HP", "Dodge"], ["HP", "Dodge"]]
                "Off_sub": [Off_sub],
                "Sta_sub": [Sta_sub],
                "Spe_sub": [Spe_sub],        
            } 
    )
    database = database.append(row)
    return database
#%% Attempt 2: Hand-crafted fudge that should to be replaced eventually
twt = np.array([
        ["Magnhilda","Nascita","Hatsu","Helix","Nora",
         "Chanzhi","Sockdolager","Angela","Croque","Nanaka",
         "Sueyoi","Dushevnaya"],
        ["Lower Limit","MLR","MLR","Progression","Feedforward",
         "MLR","MLR","Deduction","Progression","Progression",
         "Lower Limit","Deduction"],
        ["Resolve","PerCap","PerCap","PerCap","PerCap", # PerCap Nascita Hatsu
         "PerCap","PerCap","PerCap","Overflow","PerCap",
         "PerCap","PerCap"],
        ["Stratagem","Paradigm","Delta V","SVM","Exploit",
         "Paradigm","Convolution","Delta V","Stratagem","Loop Gain",
         "Exploit","Paradigm"],
        ["Atk%","Atk%","Atk%","Hash%","Atk%",
         "Atk%","Atk%","Hash%","Hash%","Hash%",
         "Hash%","Hash%"],
        ["HP%","HP%","HP%","HP","HP", # HP% Nascita Hatsu
         "HP","HP","HP","HP","HP",
         "HP","HP"],
        ["Haste","CDmg","Haste","Haste","Haste",
         "CnC","CnC","Haste","Haste","Heal",
         "CnC","Def"],
        [set(["HP","Dmg"]),set(["Dmg","Atk%"]),set(["Dmg","Atk%"]),set(["Hash%","Hash"]),set(["Dmg","Atk%"]),
         set(["Dmg","CRate"]),set(["Dmg","Atk%"]),set(["HP","Resist"]),set(["HP","Hash"]),set(["Hash%","Hash"]),
         set(["Hash","Dmg"]),set(["Hash","Dmg"])],
        [set(["DR","HP"]),set(["DR","Atk"]),set(["DR","Atk"]),set(["DR","Hash"]),set(["Atk","DR"]),
         set(["CDmg","CRate"]),set(["CDmg","Atk"]),set(["DR","HP"]),set(["DR","HP%"]),set(["DR","Hash"]),
         set(["CDmg","CRate"]),set(["DR","Hash"])],
        [set(["Dodge","HP"]),set(["CDmg","Atk"]),set(["Haste","Atk"]),set(["Haste","Hash"]),set(["Haste","Atk"]),
         set(["CDmg","CRate"]),set(["CDmg","CRate"]),set(["Haste","Dodge"]),set(["Haste","Dodge"]),set(["Haste","Hash"]),
         set(["CRate","CDmg"]),set(["Hash","Dodge"])],  
])

inventory = np.transpose(twt)

def add_doll(Doll):
   twt = np.append(twt,np.transpose([Doll[0:7]]),axis=1)
   return twt


#%% DO NOT READ
#while True:
#    try:
#        ans = input("Would you like to add another doll? {} or {}".format('Y', 'N')
#
#while True:
#    try:
#        ans = input("Would you like to add another doll? {} or {}".format('Y', 'N'))
#        if ans == 'Y':
#            valid = "yes"                
#            print("{} set selected.".format(ans))
#        else:
#            valid = 0
#            print("Try again. Don't add a space before typing")
#        int(valid)
#        except ValueError:
#            off_set = ans
#            break
#
#
#
##%%
#while True:
#    try:
#        ans = input("Would you like to add another doll? {} or {}".format('Y', 'N')
#        if ans == 'Y' or ans == 'N':
#            valid = "yes"                
#            print("{} set selected.".format(ans))
#        else:
#            valid = 0
#            print("Try again. Don't add a space before typing")
#        int(valid)
#        except ValueError:
#            off_set = ans
#            break










