"""
Selecting algorithms for dolls with multiple viable sets
"""
import numpy as np
import pandas as pd
#%%
def alg_selection(Doll_Object):
    
    Doll = Doll_Object
    
    name = Doll["Name"][0]
    
    if len(Doll["Offense"][0]) != 1:
        while True:
            try:
                ans = input("Pick {} or {}".format(Doll["Offense"][0][0], Doll["Offense"][0][1]))
                if ans == Doll["Offense"][0][0] or ans == Doll["Offense"][0][1]:
                    valid = "yes"                
                    print("{} set selected.".format(ans))
                else:
                    valid = 0
                    print("Try again. Don't add a space before typing")
                int(valid)
            except ValueError:
                off_set = ans             
                break
    else: off_set = Doll["Offense"][0][0]
    
    
    if len(Doll["Stability"][0]) != 1:
        while True:
            try:
                ans = input("Pick {} or {}".format(Doll["Stability"][0][0], Doll["Stability"][0][1]))
                if ans == Doll["Stability"][0][0] or ans == Doll["Stability"][0][1]:
                    valid = "yes"
                    print("{} set selected.".format(ans))
                else:
                    valid = 0
                    print("Try again. Don't add a space before typing")
                int(valid)
            except ValueError:
                sta_set = ans
                break
    else: sta_set = Doll["Stability"][0][0]    

    if len(Doll["Special"][0]) != 1:
        while True:
            try:
                ans = input("Pick {} or {}".format(Doll["Special"][0][0], Doll["Special"][0][1]))
                if ans == Doll["Special"][0][0] or ans == Doll["Special"][0][1]:
                    valid = "yes"
                    print("{} set selected.".format(ans))
                else:
                    valid = 0
                    print("Try again. Don't add a space before typing")
                int(valid)
            except ValueError:
                spe_set = ans
                break
    else: spe_set = Doll["Special"][0][0]    
    
    off_m, sta_m, spe_m = Doll["Off_main"][0][1], Doll["Sta_main"][0][1], Doll["Spe_main"][0][1]
    off_s, sta_s, spe_s = set(Doll["Off_sub"][0][1]), set(Doll["Sta_sub"][0][1]), set(Doll["Spe_sub"][0][1])
    
    your_doll = [name,off_set,sta_set,spe_set,off_m,sta_m,spe_m,off_s,sta_s,spe_s]        
    return your_doll    
    
#your_Mag = alg_selection("Magnhilda")  
#%%
def alg_selection1(Doll_Object):
    
    Doll = Doll_Object
    
    name = Doll["Name"][0]
    
    if len(Doll["Offense"][0]) != 1:
        while True:
            try:
                ans = input("Pick {} or {}".format(Doll["Offense"][0][0], Doll["Offense"][0][1]))
                if ans == Doll["Offense"][0][0]:
                    nb = 0
                    valid = "yes"                
                    print("{} set selected.".format(ans))
                if ans == Doll["Offense"][0][1]:
                    nb = 1
                    valid = "yes"                
                    print("{} set selected.".format(ans))                
                else:
                    valid = 0
                    print("Try again. Don't add a space before typing")
                int(valid)
            except ValueError:
                off_set = Doll["Offense"][0][nb] 
                off_m = Doll["Off_main"][0][ans]
                off_s = set(Doll["Off_sub"][0][ans])   
                break
    else:
        off_set = Doll["Offense"][0][0]
        off_m = Doll["Off_main"][0][0]
        off_s = set(Doll["Off_sub"][0][0]) 
    
    if len(Doll["Stability"][0]) != 1:
        while True:
            try:
                ans = input("Pick {} or {}".format(Doll["Stability"][0][0], Doll["Stability"][0][1]))
                if ans == Doll["Stability"][0][0]:
                    nb = 0
                    valid = "yes"
                    print("{} set selected.".format(ans))
                if ans == Doll["Stability"][0][1]:                
                    nb = 1
                    valid = "yes"
                    print("{} set selected.".format(ans))                    
                else:
                    valid = 0
                    print("Try again. Don't add a space before typing")
                int(valid)
            except ValueError:
                sta_set = Doll["Stability"][0][ans]
                sta_m = Doll["Sta_main"][0][ans]
                sta_s = set(Doll["Sta_sub"][0][ans])
                break
    else: 
        sta_set = Doll["Stability"][0][0]
        sta_m = Doll["Sta_main"][0][0]
        sta_s = set(Doll["Stability"][0][0])    

    if len(Doll["Special"][0]) != 1:
        while True:
            try:
                ans = input("Pick {} or {}".format(Doll["Special"][0][0], Doll["Special"][0][1]))
                if ans == Doll["Special"][0][0]:
                    nb = 0
                    valid = "yes"
                    print("{} set selected.".format(ans))
                if ans == Doll["Special"][0][1]:
                    nb = 0
                    valid = "yes"
                    print("{} set selected.".format(ans))
                else:
                    valid = 0
                    print("Try again. Don't add a space before typing")
                int(valid)
            except ValueError:
                spe_set = Doll["Special"][0][ans]
                spe_m = Doll["Spe_main"][0][ans]
                spe_s = set(Doll["Spe_sub"][0][ans])
                break
    else: 
        spe_set = Doll["Special"][0][0]
        spe_m = Doll["Spe_main"][0][0]
        spe_s = set(Doll["Special"][0][0])     
        
    your_doll = [name,off_set,sta_set,spe_set,off_m,sta_m,spe_m,off_s,sta_s,spe_s]        
    return your_doll    

#%%
def alg_selection2(Doll_Object):
    
    Doll = Doll_Object
    
    name = Doll["Name"][0]
    
    if len(Doll["Offense"][0]) != 1:
        while True:
            try:
                ans = input("Pick {} or {}".format(Doll["Offense"][0][0], Doll["Offense"][0][1]))
                if ans == 1 or ans == 1:
                    valid = "yes"                
                    print("{} set selected.".format(ans))
                else:
                    valid = 0
                    print("Try again. Don't add a space before typing")
                int(valid)
            except ValueError:
                off_set = Doll["Offense"][0][ans]
                off_m = Doll["Off_main"][0][ans]
                off_s = set(Doll["Off_sub"][0][ans])                
                break
    else: 
        off_set = Doll["Offense"][0][0]
        off_m = Doll["Off_main"][0][0]
        off_s = set(Doll["Off_sub"][0][0])    
    
    if len(Doll["Stability"][0]) != 1:
#       
#        while True:
#            try:
#                ans = input("Pick {} or {}".format(Doll["Stability"][0][0], Doll["Stability"][0][1]))
#                if ans == Doll["Stability"][0][0] or ans == Doll["Stability"][0][1]:
#                    valid = "yes"
#                    print("{} set selected.".format(ans))
#                else:
#                    valid = 0
#                    print("Try again. Don't add a space before typing")
#                int(valid)
#            except ValueError:
#
        while True:
            try:
                ans = input("Pick (1) {} or (2) {}".format(Doll["Stability"][0][0], Doll["Stability"][0][1]))
                if ans == Doll["Stability"][0][0]:
                    ans = 0
                    valid = "yes"                
                    print("{} set selected.".format(Doll["Stability"][0][ans]))
                if ans == Doll["Stability"][0][1]:     
                    ans = 1
                    valid = "yes"                
                    print("{} set selected.".format(Doll["Stability"][0][ans]))
                else:
                    valid = 0
                    print("Try again. Don't add a space before typing")
                int(valid)
            except ValueError:
                sta_set = Doll["Stability"][0][ans]
                sta_m = Doll["Sta_main"][0][ans]
                sta_s = set(Doll["Sta_sub"][0][ans])
                break
    else: 
        sta_set = Doll["Stability"][0][0]
        sta_m = Doll["Sta_main"][0][0]
        sta_s = set(Doll["Stability"][0][0])    
        
    if len(Doll["Special"][0]) != 1:
        while True:
            try:
                ans = input("Pick {} or {}".format(Doll["Special"][0][0], Doll["Special"][0][1]))
                print(ans)
                if ans == 1 or ans == 2:
                    valid = "yes"                
                    print("{} set selected.".format(ans))
                else:
                    valid = 0
                    print("Try again. Don't add a space before typing")
                int(valid)
            except ValueError:
                spe_set = Doll["Special"][0][ans]
                spe_m = Doll["Spe_main"][0][ans]
                spe_s = set(Doll["Spe_sub"][0][ans])
                break
    else: 
        spe_set = Doll["Special"][0][0]
        spe_m = Doll["Spe_main"][0][0]
        spe_s = set(Doll["Special"][0][0])   
    
#    off_m, sta_m, spe_m = Doll["Off_main"][0][1], Doll["Sta_main"][0][1], Doll["Spe_main"][0][1]
#    off_s, sta_s, spe_s = set(Doll["Off_sub"][0][1]), set(Doll["Sta_sub"][0][1]), set(Doll["Spe_sub"][0][1])
    
    your_doll = [name,off_set,sta_set,spe_set,off_m,sta_m,spe_m,off_s,sta_s,spe_s]        
    return your_doll    
    
#your_Mag = alg_selection("Magnhilda")  