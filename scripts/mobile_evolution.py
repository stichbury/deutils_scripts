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
# Read DE16 data
de16 = de.read_sparta_survey(7)
de16_meta = de.meta(7)


##################

#Crosstab all devs geographical regions against development area
regions=de.crosstab(de16, de16_meta, 'RegionCode8','CR2a', 'WghtUniversal_Core')
regions.to_clipboard()

#Crosstab professionals only in geographical regions against development area
de16['Prof']  = (de16[['CR2b_2_1']].any(axis=1)).astype(float).replace(0,2)
regions=de.crosstab(de16[de16.Prof==1], de16_meta, 'RegionCode8','CR2a', 'WghtUniversal_Core')
regions.to_clipboard()


mob_devs = (de16.CR2a_2==1)
filtered = de.dist(de16[mob_devs], de16_meta, 'CR_DEV4', 'WghtUniversal_Core')
filtered_pc = de.calc_pct(filtered)
filtered_pc.to_clipboard()

cr_dev4 = de.dist(de16, de16_meta, 'CR_DEV4', 'WghtUniversal_Core')
cr_dev4_pc = de.calc_pct(cr_dev4)
cr_dev4_pc.to_clipboard()

#Look at number of mobile devs
cr2 =  de.dist(de16, de16_meta, 'CR2a', 'WghtUniversal_Core')
cr2.to_clipboard()
cr2_pc = de.calc_pct(cr2)
cr2_pc.to_clipboard()

#Look at areas of development (CR2a)
#Just women devs (filter)
dev_female = de.dist(de16[de16['CR_DEV3']==1],de16_meta,'CR2a','WghtUniversal_Core')
dev_female_pc=de.calc_pct(dev_female)
dev_female_pc.to_clipboard()

#Just male devs (filter)
dev_male = de.dist(de16[de16['CR_DEV3']==3],de16_meta,'CR2a','WghtUniversal_Core')
dev_male_pc=de.calc_pct(dev_male)
dev_male_pc.to_clipboard()


#Look at number of professional devs
cr2 =  de.dist(de16, de16_meta, 'CR2b', 'WghtUniversal_Core')
cr2_pc = de.calc_pct(cr2)
cr2_pc.to_clipboard()

# Look at the other development that mobile devs do
mob_devs = (de16.CR2a_2==1)
filtered = de.dist(de16[mob_devs], de16_meta, 'CR2a', 'WghtUniversal_Core')
filtered_pc = de.calc_pct(filtered)
filtered_pc.to_clipboard()

mob_devs = (de16.CR2a_2==1)
filtered = de.dist(de16[mob_devs], de16_meta, 'CR2b', 'WghtUniversal_Core')
filtered_pc = de.calc_pct(filtered)
filtered_pc.to_clipboard()

# Look at the other development that web devs do
web_devs = (de16.CR2a_1==1)
filtered = de.dist(de16[web_devs], de16_meta, 'CR2a', 'WghtUniversal_Core')
filtered_pc = de.calc_pct(filtered)
filtered_pc.to_clipboard()

# Look at the other development that desktop devs do
desk_devs = (de16.CR2a_3==1)
filtered = de.dist(de16[desk_devs], de16_meta, 'CR2a', 'WghtUniversal_Core')
filtered_pc = de.calc_pct(filtered)
filtered_pc.to_clipboard()

# Look at the other development that backend devs do
backend_devs = (de16.CR2a_4==1)
filtered = de.dist(de16[backend_devs], de16_meta, 'CR2a', 'WghtUniversal_Core')
filtered_pc = de.calc_pct(filtered)
filtered_pc.to_clipboard()

# Look at the other development that datasci devs do
datasci_devs = (de16.CR2a_9==1)
filtered = de.dist(de16[datasci_devs], de16_meta, 'CR2a', 'WghtUniversal_Core')
filtered_pc = de.calc_pct(filtered)
filtered_pc.to_clipboard()

# Look at the other development that IoT devs do
iot_devs = (de16.CR2a_5==1)
filtered = de.dist(de16[iot_devs], de16_meta, 'CR2a', 'WghtUniversal_Core')
filtered_pc = de.calc_pct(filtered)
filtered_pc.to_clipboard()

# Look at the other development that AR devs do
devs = (de16.CR2a_6==1)
filtered = de.dist(de16[devs], de16_meta, 'CR2a', 'WghtUniversal_Core')
filtered_pc = de.calc_pct(filtered)
filtered_pc.to_clipboard()

# Look at the other development that VR devs do
devs = (de16.CR2a_7==1)
filtered = de.dist(de16[devs], de16_meta, 'CR2a', 'WghtUniversal_Core')
filtered_pc = de.calc_pct(filtered)
filtered_pc.to_clipboard()

# Look at the other development that games devs do
devs = (de16.CR2a_8==1)
filtered = de.dist(de16[devs], de16_meta, 'CR2a', 'WghtUniversal_Core')
filtered_pc = de.calc_pct(filtered)
filtered_pc.to_clipboard()


# How many professional mobile devs do other stuff?

de16['Prof']  = (de16[['CR2b_2_1']].any(axis=1)).astype(float).replace(0,2)
cr2pros_only = de.dist(de16[de16.Prof==1], de16_meta, 'CR2b', 'WghtUniversal_Core')
cr2pros_only_pc = de.calc_pct(cr2pros_only)
cr2pros_only_pc.to_clipboard()

# CR6: experience levels over survey
cr6 = de.dist(de16, de16_meta, 'CR6', 'WghtUniversal_Core')
cr6_pc = de.calc_pct(cr6, pct_type='row')
cr6_pc.to_clipboard()

# Filter by mobile 
de16['MOBILE']  = de16[['CR2a_2']].any(axis=1).astype(float).replace(0,np.nan)
mob_dev=(de16.MOBILE==1)

de16['OTHERS']  = de16[['CR2a_1', 'CR2a_3','CR2a_4','CR2a_5','CR2a_6','CR2a_7','CR2a_8','CR2a_9','CR2a_10',]].any(axis=1).astype(float).replace(0,np.nan)
other_dev = (de16.OTHERS==1)

#Look at age levels
# whole dev population except mobile devs
cr_dev2 = de.dist(de16[other_dev], de16_meta, 'CR_DEV2', 'WghtUniversal_Core')
cr_dev2_pc = de.calc_pct(cr_dev2)
cr_dev2_pc.to_clipboard()

cr_dev2_mobile = de.dist(de16[mob_dev],de16_meta,'CR_DEV2','WghtUniversal_Core')
cr_dev2_mobile_pc=de.calc_pct(cr_dev2_mobile)
cr_dev2_mobile_pc.to_clipboard()

#Crosstab geographical regions against development area
regions=de.crosstab(de16, de16_meta, 'RegionCode8','CR2a', 'WghtUniversal_Core')
regions.to_clipboard()

#MOB1: What hardware platforms do you develop  on?
mob1 = de.dist(de16, de16_meta, 'MOB1', 'WghtUniversal_Mob')
mob1pc = de.calc_pct(mob1)
mob1pc.to_clipboard()

# Mobile professionals only
de16['Prof']  = (de16[['CR2b_2_1']].any(axis=1)).astype(float).replace(0,2)
pros_only = de.dist(de16[de16.Prof==1], de16_meta, 'MOB1', 'WghtUniversal_Mob')
pros_onlypc = de.calc_pct(pros_only)
pros_onlypc.to_clipboard()

#Non professionals
de16['nonprof']  = (de16[['CR2b_2_2', 'CR2b_2_3']].any(axis=1)).astype(float).replace(0,2)
npros_only = de.dist(de16[de16.nonprof==1], de16_meta, 'MOB1', 'WghtUniversal_Mob')
npros_onlypc = de.calc_pct(npros_only)
npros_onlypc.to_clipboard()

#MOB3: What programming languages?
mob3 = de.dist(de16, de16_meta, 'MOB3', 'WghtUniversal_Mob')
mob3pc = de.calc_pct(mob3)
mob3pc.to_clipboard()

# Mobile professionals only
pros_only = de.dist(de16[de16.Prof==1], de16_meta, 'MOB3', 'WghtUniversal_Mob')
pros_onlypc = de.calc_pct(pros_only)
pros_onlypc.to_clipboard()

#Non professionals
npros_only = de.dist(de16[de16.nonprof==1], de16_meta, 'MOB3', 'WghtUniversal_Mob')
npros_onlypc = de.calc_pct(npros_only)
npros_onlypc.to_clipboard()


#Filter mobile devs programming language choice by those that use cross platform dev tools
de16['xplat']  = (de16[['MOB_PA_1']].any(axis=1)).astype(float).replace(0,2)
mob3_xplat = de.dist(de16[de16.xplat==1], de16_meta, 'MOB3', 'WghtUniversal_Mob')
mob3_xplatpc = de.calc_pct(mob3_xplat)
mob3_xplatpc.to_clipboard()

#MOB_PA: What tech do you use
mobpa = de.dist(de16, de16_meta, 'MOB_PA', 'WghtUniversal_Mob')
mobpapc = de.calc_pct(mobpa)
mobpapc.to_clipboard()

#What about professional mobile devs?
pros_only = de.dist(de16[de16.Prof==1], de16_meta, 'MOB_PA', 'WghtUniversal_Mob')
pros_onlypc = de.calc_pct(pros_only)
pros_onlypc.to_clipboard()


#Non professionals
npros_only = de.dist(de16[de16.nonprof==1], de16_meta, 'MOB_PA', 'WghtUniversal_Mob')
npros_onlypc = de.calc_pct(npros_only)
npros_onlypc.to_clipboard()




#Look at number of mobile devs with web skills 
cr2 =  de.dist(de16, de16_meta, 'CR2a', 'WghtUniversal_Core')
cr2_pc = de.calc_pct(cr2)
cr2_pc.to_clipboard()


#Look at the professional mobile developers working in various sectors 
de16['Prof']  = (de16[['CR2b_2_1']].any(axis=1)).astype(float).replace(0,2)
pros_only = de.dist(de16[de16.Prof==1], de16_meta, 'CR_PROF1', 'WghtUniversal_Core')
pros_onlypc = de.calc_pct(pros_only)
pros_onlypc.to_clipboard()


## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** 
#MOB2: Application category
## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** 

# Mobile professionals only
de16['Prof']  = (de16[['CR2b_2_1']].any(axis=1)).astype(float).replace(0,2)
#Non professionals
de16['nonprof']  = (de16[['CR2b_2_2', 'CR2b_2_3']].any(axis=1)).astype(float).replace(0,2)

# Pros
pros_only = de.dist(de16[de16.Prof==1], de16_meta, 'MOB2', 'WghtUniversal_Mob')
pros_onlypc = de.calc_pct(pros_only)
pros_onlypc.to_clipboard()

#Non professionals
npros_only = de.dist(de16[de16.nonprof==1], de16_meta, 'MOB2', 'WghtUniversal_Mob')
npros_onlypc = de.calc_pct(npros_only)
npros_onlypc.to_clipboard()

#Filter mobile devs choice of app type by those that use cross platform dev tools
de16['xplat']  = (de16[['MOB_PA_1']].any(axis=1)).astype(float).replace(0,2)
mob2_xplat = de.dist(de16[de16.xplat==1], de16_meta, 'MOB2', 'WghtUniversal_Mob')
mob2_xplatpc = de.calc_pct(mob2_xplat)
mob2_xplatpc.to_clipboard()


#MOB8: Audience sector - pros
mob8pros_only = de.dist(de16[de16.Prof==1], de16_meta, 'MOB8', 'WghtUniversal_Mob')
mob8pros_onlypc = de.calc_pct(mob8pros_only)
mob8pros_onlypc.to_clipboard()

npros_only = de.dist(de16[de16.nonprof==1], de16_meta, 'MOB8', 'WghtUniversal_Mob')
npros_onlypc = de.calc_pct(npros_only)
npros_onlypc.to_clipboard()


## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** 
# MOB_POP questions
# For the professionals only

pros_only = de.dist(de16[de16.Prof==1], de16_meta, 'MOB_POP1', 'WghtUniversal_Core')
pros_onlypc = de.calc_pct(pros_only)
pros_onlypc.to_clipboard()

pros_only = de.dist(de16[de16.Prof==1], de16_meta, 'MOB_POP2', 'WghtUniversal_Core')
pros_onlypc = de.calc_pct(pros_only)
pros_onlypc.to_clipboard()

pros_only = de.dist(de16[de16.Prof==1], de16_meta, 'MOB_POP3', 'WghtUniversal_Core')
pros_onlypc = de.calc_pct(pros_only)
pros_onlypc.to_clipboard()

# Now the same questions for the non-professionals only

npros_only = de.dist(de16[de16.nonprof==1], de16_meta, 'MOB_POP1', 'WghtUniversal_Core')
npros_onlypc = de.calc_pct(npros_only)
npros_onlypc.to_clipboard()


npros_only = de.dist(de16[de16.nonprof==1], de16_meta, 'MOB_POP2', 'WghtUniversal_Core')
npros_onlypc = de.calc_pct(npros_only)
npros_onlypc.to_clipboard()

npros_only = de.dist(de16[de16.nonprof==1], de16_meta, 'MOB_POP3', 'WghtUniversal_Core')
npros_onlypc = de.calc_pct(npros_only)
npros_onlypc.to_clipboard()


## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** 
# Motivation

#Look at the professional mobile developers only

pros_only = de.dist(de16[de16.Prof==1], de16_meta, 'MOB4', 'WghtUniversal_Core')
pros_onlypc = de.calc_pct(pros_only)
pros_onlypc.to_clipboard()

npros_only = de.dist(de16[de16.nonprof==1], de16_meta, 'MOB4', 'WghtUniversal_Core')
npros_onlypc = de.calc_pct(npros_only)
npros_onlypc.to_clipboard()

#Look at ways to make money MOB6 
pros_only = de.dist(de16[de16.Prof==1], de16_meta, 'MOB6', 'WghtUniversal_Core')
pros_onlypc = de.calc_pct(pros_only)
pros_onlypc.to_clipboard()

npros_only = de.dist(de16[de16.nonprof==1], de16_meta, 'MOB6', 'WghtUniversal_Core')
pros_onlypc = de.calc_pct(pros_only)
pros_onlypc.to_clipboard()


#Look at revenue MOB7 

pros_only = de.dist(de16[de16.Prof==1], de16_meta, 'MOB7', 'WghtUniversal_Core')
pros_only.to_clipboard()

npros_only = de.dist(de16[de16.nonprof==1], de16_meta, 'MOB7', 'WghtUniversal_Core')
npros_only.to_clipboard()

## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** 
# Organisation size for pro mobile devs only

pros_only = de.dist(de16[de16.Prof==1], de16_meta, 'MOB8', 'WghtUniversal_Core')
pros_onlypc = de.calc_pct(pros_only)
pros_onlypc.to_clipboard()

npros_only = de.dist(de16[de16.nonprof==1], de16_meta, 'WEB10', 'WghtUniversal_Core')
npros_onlypc = de.calc_pct(npros_only)
npros_onlypc.to_clipboard()

## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** 
# Crosstabs
## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** ## ** 


cross = de.crosstab(de16[de16.Prof==1], de16_meta, 'MOB2', 'MOB8', 'WghtUniversal_Mob')
cross.to_clipboard()

cross = de.crosstab(de16[de16.Prof==1], de16_meta, 'MOB2', 'MOB7', 'WghtUniversal_Mob')
cross.to_clipboard()

cross = de.crosstab(de16[de16.Prof==1], de16_meta, 'MOB_POP3', 'MOB7', 'WghtUniversal_Mob')
cross.to_clipboard()

cross = de.crosstab(de16[de16.Prof==1], de16_meta, 'MOB6', 'MOB7', 'WghtUniversal_Mob')
cross.to_clipboard()


cross = de.crosstab(de16[de16.nonprof==1], de16_meta, 'MOB6', 'MOB7', 'WghtUniversal_Mob')
cross.to_clipboard()










cross = de.crosstab(de16, de16_meta, 'MOB1', 'MOB_PA', 'WghtUniversal_Mob')
cross.to_clipboard()
cross_pc = de.calc_pct(cross)
cross_pc.to_clipboard()

cross = de.crosstab(de16, de16_meta, 'MOB_PA', 'MOB1', 'WghtUniversal_Mob')
cross.to_clipboard()
cross_pc = de.calc_pct(cross)
cross_pc.to_clipboard()

cross = de.crosstab(de16, de16_meta, 'MOB3', 'MOB_PA', 'WghtUniversal_Mob')
cross.to_clipboard()
cross_pc = de.calc_pct(cross)
cross_pc.to_clipboard()






#MS_TECH: Approaches and technologies - only asked to desktop, web & games devs, so only really useful
#for a snapshot
mstech = de.dist(de16, de16_meta, 'MS_TECH', 'WghtUniversal_Core')
mstechpc = de.calc_pct(mstech)
mstechpc.to_clipboard()

