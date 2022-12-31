# -*- coding: utf-8 -*-
"""
A tool that was intended to help schedule fragment searching. Feel free to write a class for what I called channels or any other improvements like UI.
"""
import numpy as np
import pandas as pd
from datetime import datetime, date, timedelta
#%% Function to calculate number of fragments till target rarity is reached
bta = np.array([[1,1.5,2.,2.5,3.,3.5,4.,4.5,5],[0,5,10,25,40,60,70,90,100]]) # BreakthroughArray

def cum_frags(Fragments,Current_Rarity,Target_Rarity):
    ind = 0
    for i in bta[0,:]:
        if i == Current_Rarity:
            break
        else:
            ind += 1

    frags = 0
    for j in bta[0,ind:]:
        #print(j)
        if j == Target_Rarity:
            return frags - Fragments
        else:
            ind += 1
            frags += bta[1,ind]
#%% Run this and scroll down for user manual
class PNC_acc:
    
    def __init__(self, names, fragments, current_rarities):
        self.df = pd.DataFrame(
            {
                    "Name": names,
                    "Fragments": fragments,
                    "Current_Rarity": current_rarities
            }
        )
        
        self.Ch4 = pd.DataFrame({"name": ["Today"], "days": [0]}) # queue for 4 searches per day
        self.Ch6 = pd.DataFrame({"name": ["Today"], "days": [0]}) # queue for 6 searches per day
#        self.backlog = pd.DataFrame({"name": ["n/a"]})
    
    # add dolls to your collection 
    def add_doll(self, name, fragments, current_rarity):
        if self.df['Name'].str.contains(name).any() or self.Ch6['name'].str.contains(name).any():
            raise ValueError("Baka! Only the mainframe has their own neural cloud.")
            
        new_doll = {"Name": str(name), 
                    "Fragments": int(fragments), 
                    "Current_Rarity": float(current_rarity), 
        }    
        self.df = self.df.append(new_doll, ignore_index = True)
        return self.df    

    # queues up dolls for fragment search
    def search(self,name,target_rarity,channel):
        
        if channel != 4 and channel != 6:
            raise ValueError("Pick 4 or 6")
        
        doll_info = self.df.loc[self.df['Name'] == name]    
        if target_rarity < float(doll_info['Current_Rarity']):
            raise ValueError("Error: Target rarity below current rarity")
        
        if self.Ch4['name'].str.contains(name).any() or self.Ch6['name'].str.contains(name).any():
            raise ValueError("Error: Doll is already scheduled for cuddles, please use .move() to if you wish to reschedule.")
            
        tot_frags = cum_frags(
                float(doll_info["Fragments"]),
                float(doll_info["Current_Rarity"]),
                float(target_rarity)
        )

        if int(channel) == 4:
            self.Ch4 = self.Ch4.append({"name": str(name), "days": tot_frags/(channel*1.2)}, ignore_index = True)
        if int(channel) == 6:
            self.Ch6 = self.Ch6.append({"name": str(name), "days": tot_frags/(channel*1.2)}, ignore_index = True)
        
    # remove dolls in queue
    def remove(self,name,channel):
        if channel == 4:
            row_id = self.Ch4[self.Ch4['name'] == name].index
            self.Ch4 = self.Ch4.drop(row_id)
            self.Ch4 = self.Ch4.reset_index(drop=True)
            return self.Ch4
        if channel == 6:
            row_id = self.Ch6[self.Ch6['name'] == name].index
            self.Ch6 = self.Ch6.drop(row_id)
            self.Ch6 = self.Ch6.reset_index(drop=True)
            return self.Ch6  
        else:
            raise ValueError("Error: Channel does not exist")
                
    # returns backlog as a list of dates
    def timeline(self,channel):
        if channel == 4:
            cum_day = np.array([date.today()])
            for i in self.Ch4.iloc[1:,1:].values:
                cum_day = np.append(cum_day, cum_day[-1] + timedelta(days=float(i)))                
            return pd.DataFrame({"name": self.Ch4.iloc[:,0].values, "date": cum_day})            
        if channel == 6:
            cum_day = np.array([date.today()])
            for i in self.Ch6.iloc[1:,1:].values:
                cum_day = np.append(cum_day, cum_day[-1] + timedelta(days=float(i)))                
            return pd.DataFrame({"name": self.Ch6.iloc[:,0].values, "date": cum_day}) 
        else:
            raise ValueError("Error: Channel does not exist")        
                      
    def move(self,name, from_channel,to_channel,position):
        if position < 0:
            raise ValueError("Time travel forbidden!")
        if from_channel != 4 and from_channel != 6:
            raise ValueError("Pick 4 or 6")
        if to_channel != 4 and to_channel != 6:
            raise ValueError("Pick 4 or 6")

        if from_channel == 4:
            line = self.Ch4.loc[self.Ch4['name'] == name]
            line2= line.rename(index={line.index[0]:str(position)})
            
            self.Ch4 = self.Ch4.drop(self.Ch4[self.Ch4['name'] == "Dushy"].index)
            if to_channel == 4:
                self.Ch4 = self.Ch4.append(line2, ignore_index=False)
                self.Ch4.index = self.Ch4.index.map(str)
                self.Ch4 = self.Ch4.sort_index().reset_index(drop=True)
            if to_channel == 6:
                self.Ch6 = self.Ch6.append(line2, ignore_index=False)
                self.Ch6.index = self.Ch6.index.map(str)
                self.Ch6 = self.Ch6.sort_index().reset_index(drop=True)

        if from_channel == 6:
            line = self.Ch6.loc[self.Ch6['name'] == name]
            line2= line.rename(index={line.index[0]:str(position)})
            
            self.Ch4 = self.Ch4.drop(self.Ch4[self.Ch4['name'] == "Dushy"].index)
            if to_channel == 4:
                self.Ch4 = self.Ch4.append(line2, ignore_index=False)
                self.Ch4.index = self.Ch4.index.map(str)
                self.Ch4 = self.Ch4.sort_index().reset_index(drop=True)
            if to_channel == 6:
                self.Ch6 = self.Ch6.append(line2, ignore_index=False)
                self.Ch6.index = self.Ch6.index.map(str)
                self.Ch6 = self.Ch6.sort_index().reset_index(drop=True)
                
#%% USER GUIDE
# Add dolls
EN = PNC_acc(["Chanzhi", "Dushy", "Hatsu"],[36,24,58],[4.5,2.5,3])
EN.df
''' Output
      Name  Fragments  Current_Rarity
0  Chanzhi         36             4.5
1    Dushy         24             2.5
2    Hatsu         58             3.0
'''
#%%
# Add more dolls
EN.add_doll("Nanaka",2,3)
EN.add_doll("Sueyoi",0,3)
EN.add_doll("Imhotep",13,2)
EN.add_doll("Lam",20,4)
EN.df
'''
      Name  Fragments  Current_Rarity
0  Chanzhi         36             4.5
1    Dushy         24             2.5
2    Hatsu         58             3.0
3   Nanaka          2             3.0
4   Sueyoi          0             3.0
5  Imhotep         13             2.0
6      Lam         20             4.0
'''
#%%
# Queue up dolls
EN.search("Dushy",3.5,4)
EN.search("Hatsu",5,6)
EN.search("Lam",4.5,4)
EN.search("Imhotep",5,4)
EN.search("Nanaka",4.5,6)
#%%
# View days required to reach goal
EN.Ch4 # The 4-per-day queue
'''
      name       days
0    Today   0.000000
1    Dushy  15.833333
2      Lam  14.583333
3  Imhotep  77.500000
'''
EN.Ch6 # The 6-per-day queue
'''
     name       days
0   Today   0.000000
1   Hatsu  36.388889
2  Nanaka  30.277778
'''
#%%
# Translate days to dates
EN.timeline(4)

'''
      name        date
0    Today  2022-12-31
1    Dushy  2023-01-15
2      Lam  2023-01-29
3  Imhotep  2023-04-16
'''
#%%
# Moving dolls around
EN.move("Dushy",4,4,2.5)
EN.timeline(4)
'''
      name        date
0    Today  2022-12-31
1      Lam  2023-01-14
2    Dushy  2023-01-29
3  Imhotep  2023-04-16
'''
#%%
# More frags per day
EN.move("Dushy",4,6,0.5)
EN.timeline(6)
'''
     name        date
0   Today  2022-12-31
1   Dushy  2023-01-15
2   Hatsu  2023-02-20
3  Nanaka  2023-03-22
'''
#%%
# Remove dolls from the queue
EN.remove("Dushy",6)
EN.timeline(6)
'''
     name        date
0   Today  2022-12-31
1   Hatsu  2023-02-05
2  Nanaka  2023-03-07
'''