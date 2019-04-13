# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Imports
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 15:54:14 2019
Granny-Clanger:~ stichbury$ /Users/stichbury/anaconda/envs/py3/bin/spyder ; exit;

@author: stichbury
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Imports
import pandas as pd
import deutils as de
import numpy as np

# weights
Sparta_Core = 'WghtUniversal_Core'

##################
# Read de15 data
de15 = de.read_sparta_survey(6)
de15_meta = de.meta(6)

##################

#Look at number of mobile devs
cr2 =  de.dist(de15, de15_meta, 'CR2', 'WghtUniversal_Core')
cr2_pc = de.calc_pct(cr2)
cr2_pc.to_clipboard()

#Crosstab geographical regions against development area
regions=de.crosstab(de15, de15_meta, 'RegionCode8','CR2', 'WghtUniversal_Core')
regions.to_clipboard()

#MOB1: What hardware platforms do you develop  on?
mob1 = de.dist(de15, de15_meta, 'MOB1', 'WghtUniversal_Mob')
mob1pc = de.calc_pct(mob1)
mob1pc.to_clipboard()

# Mobile professionals only
de15['Prof']  = (de15[['CR2_2_1']].any(axis=1)).astype(float).replace(0,2)
pros_only = de.dist(de15[de15.Prof==1], de15_meta, 'MOB1', 'WghtUniversal_Core')
pros_onlypc = de.calc_pct(pros_only)
pros_onlypc.to_clipboard()

#MOB3: What programming languages?
mob3 = de.dist(de15, de15_meta, 'MOB3', 'WghtUniversal_Mob')
mob3pc = de.calc_pct(mob3)
mob3pc.to_clipboard()

# Mobile professionals only
de15['Prof']  = (de15[['CR2_2_1']].any(axis=1)).astype(float).replace(0,2)
pros_only = de.dist(de15[de15.Prof==1], de15_meta, 'MOB3', 'WghtUniversal_Core')
pros_onlypc = de.calc_pct(pros_only)
pros_onlypc.to_clipboard()

#Filter mobile devs programming language choice by those that use cross platform dev tools
de15['xplat']  = (de15[['MOB_PA_1']].any(axis=1)).astype(float).replace(0,2)
mob3_xplat = de.dist(de15[de15.xplat==1], de15_meta, 'MOB3', 'WghtUniversal_Mob')
mob3_xplatpc = de.calc_pct(mob3_xplat)
mob3_xplatpc.to_clipboard()

#MOB_PA: What tech do you use
mobpa = de.dist(de15, de15_meta, 'MOB_PA', 'WghtUniversal_Mob')
mobpapc = de.calc_pct(mobpa)
mobpapc.to_clipboard()

#What about professional mobile devs?
de15['Prof']  = (de15[['CR2_2_1']].any(axis=1)).astype(float).replace(0,2)
pros_only = de.dist(de15[de15.Prof==1], de15_meta, 'MOB_PA', 'WghtUniversal_Core')
pros_onlypc = de.calc_pct(pros_only)
pros_onlypc.to_clipboard()

#MOB2: Application category
mob2 = de.dist(de15, de15_meta, 'MOB2', 'WghtUniversal_Mob')
mob2pc = de.calc_pct(mob2)
mob2pc.to_clipboard()

# Mobile professionals only
de15['Prof']  = (de15[['CR2_2_1']].any(axis=1)).astype(float).replace(0,2)
pros_only = de.dist(de15[de15.Prof==1], de15_meta, 'MOB2', 'WghtUniversal_Core')
pros_onlypc = de.calc_pct(pros_only)
pros_onlypc.to_clipboard()

#Filter mobile devs choice of app type by those that use cross platform dev tools
de15['xplat']  = (de15[['MOB_PA_1']].any(axis=1)).astype(float).replace(0,2)
mob2_xplat = de.dist(de15[de15.xplat==1], de15_meta, 'MOB2', 'WghtUniversal_Mob')
mob2_xplatpc = de.calc_pct(mob2_xplat)
mob2_xplatpc.to_clipboard()


#MOB8: Audience sector
mob8 = de.dist(de15, de15_meta, 'MOB8', 'WghtUniversal_Mob')
mob8pc = de.calc_pct(mob8)
mob8pc.to_clipboard()

# Mobile professionals only
de15['Prof']  = (de15[['CR2_2_1']].any(axis=1)).astype(float).replace(0,2)
pros_only = de.dist(de15[de15.Prof==1], de15_meta, 'MOB8', 'WghtUniversal_Core')
pros_onlypc = de.calc_pct(pros_only)
pros_onlypc.to_clipboard()














#MS_TECH: Approaches and technologies - only asked to desktop, web & games devs, so only really useful
#for a snapshot
mstech = de.dist(de15, de15_meta, 'MS_TECH', 'WghtUniversal_Core')
mstechpc = de.calc_pct(mstech)
mstechpc.to_clipboard()


