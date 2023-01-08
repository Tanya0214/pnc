# -*- coding: utf-8 -*-
"""
Creating teams
"""
import numpy as np
#%%
def add(teams,team):
    teams = np.append(teams,[team],axis=0)
    return teams
#%%
teams = np.array([
    ["Magnhilda","Nascita","Hatsu","Helix","Nora"],
])
teams = add(teams,["Chanzhi","Sockdolager","Angela","Croque","Nanaka"])
teams = add(teams,["Angela","Croque","Nanaka","Sueyoi","Dushevnaya"])