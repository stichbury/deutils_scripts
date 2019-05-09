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
# Read de14 data
de14 = de.read_sparta_survey(5)
de14_meta = de.meta(5)
##################


#Look at number of mobile devs
cr2 =  de.dist(de14, de14_meta, 'CR2', 'WghtUniversal_Core')
cr2_pc = de.calc_pct(cr2)
cr2_pc.to_clipboard()


de14['MOBILE']  = de14[['CR2_2_1', 'CR2_2_2', 'CR2_2_3']].any(axis=1).astype(float).replace(0,np.nan)
mob_dev=de14.MOBILE==1
filtered = de.dist(de14[mob_dev],de14_meta,'CR2','WghtUniversal_Core')
filtered_pc = de.calc_pct(filtered)
filtered_pc.to_clipboard()

# CR6: experience levels over survey
cr6 = de.dist(de14, de14_meta, 'CR6', 'WghtUniversal_Core')
cr6_pc = de.calc_pct(cr6, pct_type='row')
cr6_pc.to_clipboard()


#Look at age levels
# whole dev population
cr_dev2 = de.dist(de14, de14_meta, 'CR_DEV2', 'WghtUniversal_Core')
cr_dev2_pc = de.calc_pct(cr_dev2)
cr_dev2_pc.to_clipboard()

cr_dev2_mobile = de.dist(de14[mob_dev],de14_meta,'CR_DEV2','WghtUniversal_Core')
cr_dev2_mobile_pc=de.calc_pct(cr_dev2_mobile)
cr_dev2_mobile_pc.to_clipboard()



#Crosstab geographical regions against development area
regions=de.crosstab(de14, de14_meta, 'RegionCode8','CR2', 'WghtUniversal_Core')
regions.to_clipboard()

#MOB1: What hardware platforms do you develop  on?
mob1 = de.dist(de14, de14_meta, 'MOB1', 'WghtUniversal_Mob')
mob1pc = de.calc_pct(mob1)
mob1pc.to_clipboard()

# Mobile professionals only
de14['Prof']  = (de14[['CR2_2_1']].any(axis=1)).astype(float).replace(0,2)
pros_only = de.dist(de14[de14.Prof==1], de14_meta, 'MOB1', 'WghtUniversal_Core')
pros_onlypc = de.calc_pct(pros_only)
pros_onlypc.to_clipboard()

#MOB3: What programming languages?
mob3 = de.dist(de14, de14_meta, 'MOB3', 'WghtUniversal_Mob')
mob3pc = de.calc_pct(mob3)
mob3pc.to_clipboard()

# Mobile professionals only
de14['Prof']  = (de14[['CR2_2_1']].any(axis=1)).astype(float).replace(0,2)
pros_only = de.dist(de14[de14.Prof==1], de14_meta, 'MOB3', 'WghtUniversal_Core')
pros_onlypc = de.calc_pct(pros_only)
pros_onlypc.to_clipboard()

#Filter mobile devs programming language choice by those that use cross platform dev tools
de14['xplat']  = (de14[['MOB_PA_1']].any(axis=1)).astype(float).replace(0,2)
mob3_xplat = de.dist(de14[de14.xplat==1], de14_meta, 'MOB3', 'WghtUniversal_Mob')
mob3_xplatpc = de.calc_pct(mob3_xplat)
mob3_xplatpc.to_clipboard()

#MOB_PA: What tech do you use
mobpa = de.dist(de14, de14_meta, 'MOB_PA', 'WghtUniversal_Mob')
mobpapc = de.calc_pct(mobpa)
mobpapc.to_clipboard()

#What about professional mobile devs?
de14['Prof']  = (de14[['CR2_2_1']].any(axis=1)).astype(float).replace(0,2)
pros_only = de.dist(de14[de14.Prof==1], de14_meta, 'MOB_PA', 'WghtUniversal_Core')
pros_onlypc = de.calc_pct(pros_only)
pros_onlypc.to_clipboard()

#MOB2: Application category
mob2 = de.dist(de14, de14_meta, 'MOB2', 'WghtUniversal_Mob')
mob2pc = de.calc_pct(mob2)
mob2pc.to_clipboard()

# Mobile professionals only
de14['Prof']  = (de14[['CR2_2_1']].any(axis=1)).astype(float).replace(0,2)
pros_only = de.dist(de14[de14.Prof==1], de14_meta, 'MOB2', 'WghtUniversal_Core')
pros_onlypc = de.calc_pct(pros_only)
pros_onlypc.to_clipboard()

#Filter mobile devs choice of app type by those that use cross platform dev tools
de14['xplat']  = (de14[['MOB_PA_1']].any(axis=1)).astype(float).replace(0,2)
mob2_xplat = de.dist(de14[de14.xplat==1], de14_meta, 'MOB2', 'WghtUniversal_Mob')
mob2_xplatpc = de.calc_pct(mob2_xplat)
mob2_xplatpc.to_clipboard()


#MOB8: Audience sector
mob8 = de.dist(de14, de14_meta, 'MOB8', 'WghtUniversal_Mob')
mob8pc = de.calc_pct(mob8)
mob8pc.to_clipboard()

# Mobile professionals only
de14['Prof']  = (de14[['CR2_2_1']].any(axis=1)).astype(float).replace(0,2)
pros_only = de.dist(de14[de14.Prof==1], de14_meta, 'MOB8', 'WghtUniversal_Core')
pros_onlypc = de.calc_pct(pros_only)
pros_onlypc.to_clipboard()














#MS_TECH: Approaches and technologies - only asked to desktop, web & games devs, so only really useful
#for a snapshot
mstech = de.dist(de14, de14_meta, 'MS_TECH', 'WghtUniversal_Core')
mstechpc = de.calc_pct(mstech)
mstechpc.to_clipboard()


