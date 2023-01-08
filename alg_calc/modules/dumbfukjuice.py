# -*- coding: utf-8 -*-
"""
Calculates minimum algos if your dolls are willing to share algos :416lewd:
"""
import numpy as np
#%% Substats yet to be implemented
def alg_min(set_name,inventory,teams):
    
    set_dict = {}    
    for i in inventory:
        if i[2] == str(set_name):
            set_dict.update({"{}".format(i[0]) : str(i[5])})
    
    total = {}    
    for team in teams:      # iterates over teams
        htab = {}           # contains algos needed within the team
        
        for doll in team:   # iterates over dolls
            if doll in set_dict:
#                print("{} uses this set".format(doll))
                if set_dict[doll] in htab:
                    current_val = htab[set_dict[doll]]
                    htab.update({"{}".format(set_dict[doll]) : current_val+1})
                else:
                    htab.update({"{}".format(set_dict[doll]) : 1})
            else:
#                print("{} does not use this set".format(doll))
                continue
#        print(htab)
        for main in htab:
            if main in total:
                total.update({"{}".format(main) : max(htab[main],total[main])})
            else:
                total.update({"{}".format(main) : htab[main]})                
    return total

#%% Adding dolls (?)
#np.append(twt,np.transpose([Hatsu[0:7]]),axis=1)

#%%

def alg_min2(set_name,inventory,teams):
    
    set_dict = {}    
    for i in inventory:
        if i[1] == str(set_name):
            set_dict.update({"{}".format(i[0]) : str(i[4])})
        if i[2] == str(set_name):
            set_dict.update({"{}".format(i[0]) : str(i[5])})
        if i[3] == str(set_name):
            set_dict.update({"{}".format(i[0]) : str(i[6])})
             
    sub_dict = {}    
    for i in inventory:
        if i[1] == str(set_name):
            sub_dict.update({"{}".format(i[0]) : str(i[7])}) 
        if i[2] == str(set_name):
            sub_dict.update({"{}".format(i[0]) : str(i[8])})    
        if i[3] == str(set_name):
            sub_dict.update({"{}".format(i[0]) : str(i[9])})
            
    total = {}    
    for team in teams:      # iterates over teams
        htab = {}           # contains algos needed within the team
        
        for doll in team:   # iterates over dolls
            if doll in set_dict:
                if "{}:{}".format(set_dict[doll],sub_dict[doll]) in htab: # does main+sub combination already exist?
                    current_val = htab["{}:{}".format(set_dict[doll], sub_dict[doll])]
                    htab.update({"{}:{}".format(set_dict[doll], sub_dict[doll]) : current_val+1 }) # if yes, add one
                else:
                    htab.update({"{}:{}".format(set_dict[doll], sub_dict[doll]) : 1 }) # if not, add algo combination
                    continue                    
            else:
                continue
            
        for main in htab: # keep track of everything
            if main in total:
                total.update({"{}".format(main) : max(htab[main],total[main])})
            else:
                total.update({"{}".format(main) : htab[main]})
    return total

#%% 
'''
MY TESTING AREA. POINT OF NO RETURN.
'''
#%%
#fml1 = {"HP%": {"{}".format(set(["Dmg","Atk%"])) : 2},
#        "HP": {"{}".format(set(["Dmg","Atk%"])) : 1},
#        "HP": {"{}".format(set(["Dmg","Hash%"])) : 1}
#}
#%%
#fml1["HP%"].keys()

#%%
#fml1["HP%"]["{}".format(set(["Dmg","Atk%"]))]


#%%
#set_name="PerCap"
#sub_dict = {}    
#for i in inventory:
#    if i[2] == str(set_name):
#        sub_dict.update({"{}".format(i[0]) : str(i[8])})
    
#%%
#alg_min2("PerCap",inventory,my_teams)

#%% Hand-crafted fudge that needs to be replaced asap
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

#%%

def alg_min_test(set_name,inventory,teams):
    
    set_dict = {}    
    for i in inventory:
        if i[1] == str(set_name):
            set_dict.update({"{}".format(i[0]) : str(i[4])})
        if i[2] == str(set_name):
            set_dict.update({"{}".format(i[0]) : str(i[5])})
        if i[3] == str(set_name):
            set_dict.update({"{}".format(i[0]) : str(i[6])})
#    print(set_dict)
             
    sub_dict = {}    
    for i in inventory:
        if i[1] == str(set_name):
            sub_dict.update({"{}".format(i[0]) : str(i[7])}) 
        if i[2] == str(set_name):
            sub_dict.update({"{}".format(i[0]) : str(i[8])})    
        if i[3] == str(set_name):
            sub_dict.update({"{}".format(i[0]) : str(i[9])})
#    print(sub_dict)
            
    total = {}    
    for team in teams:      # iterates over teams
        htab = {}           # contains algos needed within the team
        
        for doll in team:   # iterates over dolls
            if doll in set_dict:
#                print("{} uses this set".format(doll))
#                if set_dict[doll] in htab:
#                    current_val = htab[set_dict[doll]]
#                    htab.update({"{}".format(set_dict[doll]) : current_val+1})
#                else:
#                    htab.update({"{}".format(set_dict[doll]) : 1})
#                print(set_dict[doll])
#                if set_dict[doll] in htab:
                if "{}:{}".format(set_dict[doll],sub_dict[doll]) in htab:
                    current_val = htab["{}:{}".format(set_dict[doll], sub_dict[doll])]
#                    print(current_val)
                    htab.update({"{}:{}".format(set_dict[doll], sub_dict[doll]) : current_val+1 })  
                    print(htab)
                else:
                    htab.update({"{}:{}".format(set_dict[doll], sub_dict[doll]) : 1 })
                    print(htab)
                    continue                    
                    
#                    temp_main = set_dict[doll]
#                    print(temp_main)
#                    if sub_dict[doll] in htab[temp_main]:
##                        print(htab)
#                        
#                        current_val = htab["{}:{}".format(set_dict[doll], sub_dict[doll])]
##                        print(current_val)
#                        htab.update({"{}:{}".format(set_dict[doll], sub_dict[doll]) : current_val+1 })
##                        print(htab)
#                    else:
#                        htab.update({"{}:{}".format(set_dict[doll], sub_dict[doll]) : 1 })
#                        continue
#                else:
#                    htab.update({"{}:{}".format(set_dict[doll], sub_dict[doll]) : 1 })
#                    print(htab)
#                    continue
                
            else:
#                print("{} does not use this set".format(doll))
#                print(htab)
                continue
#        print(htab)
        for main in htab:
#            print(main)
            if main in total:
#                print("Comp {}".format(htab[main]))
#                print("Total {}".format(total[main]))
                total.update({"{}".format(main) : max(htab[main],total[main])})
                if htab[main] < total[main]:
#                    print("{} algos saved".format(total[main]-htab[main]))
                    continue
            else:
                total.update({"{}".format(main) : htab[main]})                
    return total

#%%
#alg_min2("PerCap",inventory,my_teams)
