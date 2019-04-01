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

# Read DE15 data
#de15 = de.read_sparta_survey(6)
#de15_meta = de.meta(6)

# Read DE14 data
#de14_meta = de.meta(5)
#de14 = de.read_sparta_survey(5)

# Read DE13 data
#de13 = de.read_sparta_survey(4)
#de13_meta = de.meta(4)

##################

cr2 =  de.dist(de16, de16_meta, 'CR2a', 'WghtUniversal_Core')
cr2_pc = de.calc_pct(cr2)
cr2_pc.to_clipboard()


#Crosstab regions against development area
regions=de.crosstab(de16, de16_meta, 'RegionCode8','CR2a', 'WghtUniversal_Core')
regions.to_clipboard()

#MOB1: What platforms do you develop  for?
mob1 = de.dist(de16, de16_meta, 'MOB1', 'WghtUniversal_Mob')
mob1pc = de.calc_pct(mob1)
mob1pc.to_clipboard()

# Mobile professionals only
de16['Prof']  = (de16[['CR2b_2_1']].any(axis=1)).astype(float).replace(0,2)

pros_only = de.dist(de16[de16.Prof==1], de16_meta, 'MOB1', 'WghtUniversal_Core')
pros_onlypc = de.calc_pct(pros_only)
pros_onlypc.to_clipboard()


#MOB3: What programming languages?
mob3 = de.dist(de16, de16_meta, 'MOB3', 'WghtUniversal_Mob')
mob3pc = de.calc_pct(mob3)
mob3pc.to_clipboard()

# Mobile professionals only
de16['Prof']  = (de16[['CR2b_2_1']].any(axis=1)).astype(float).replace(0,2)

pros_only = de.dist(de16[de16.Prof==1], de16_meta, 'MOB3', 'WghtUniversal_Core')
pros_onlypc = de.calc_pct(pros_only)
pros_onlypc.to_clipboard()



#MS_TECH: Approaches and technologies
mstech = de.dist(de16, de16_meta, 'MS_TECH', 'WghtUniversal_Core')
mstechpc = de.calc_pct(mstech)
mstechpc.to_clipboard()

# Mobile devs only
de16['mob']  = (de16[['CR2b_2_1', 'CR2b_2_2', 'CR2b_2_3']].any(axis=1)).astype(float).replace(0,2)

mob_only = de.dist(de16[de16.mob==1], de16_meta, 'MS_TECH', 'WghtUniversal_Core')
mob_onlypc = de.calc_pct(mob_only)
mob_onlypc.to_clipboard()


# Mobile pros only
de16['mobpro']  = (de16[['CR2b_2_1']].any(axis=1)).astype(float).replace(0,2)

mobpro_only = de.dist(de16[de16.mobpro==1], de16_meta, 'MS_TECH', 'WghtUniversal_Core')
mobpro_onlypc = de.calc_pct(mobpro_only)
mobpro_onlypc.to_clipboard()



# Now read DE15 data
de15 = de.read_sparta_survey(6)
de15_meta = de.meta(6)


# CR_DEVCNT2 for DE15
cr_devcnt2_15 =  de.dist(de15, de15_meta, 'CR_DEVCNT2', 'WghtUniversal_Core')
cr_devcnt2_15.to_clipboard()




#Age
#Just women devs (filter)
dev_female = de.dist(de16[de16['CR_DEV3']==1],de16_meta,'CR_DEV2','WghtUniversal_Core')
dev_female_pc=de.calc_pct(dev_female)
dev_female_pc.to_clipboard()


#Mob1: Professional Devs Only
de16['MOB']  = de16[['CR2a_2_1']].any(axis=1).astype(float).replace(0,np.nan)
pro_mob_dev=de16.MOB==1

mob1PRO = de.dist(de16[pro_mob_dev], de16_meta, 'Mob1', 'WghtUniversal_Mob')
mob1PROpc = de.calc_pct(mob1PRO)
mob1PROpc.to_clipboard()


#GAM5: Which programming languages do you use to write code that runs on the client side for your games?
#gam5 = de.dist(de15, de15_meta, 'GAM5', 'WghtUniversal_Game')
#gam5pc = de.calc_pct(gam5)
#gam5pc.to_clipboard()

#GAM_PA "What technologies?"
#gam_pa = de.dist(de15, de15_meta, 'GAM_PA', 'WghtUniversal_Game')
#gam_pa_pc=de.calc_pct(gam_pa)
#gam_pa_pc.to_clipboard()

# Filter by games pros
#de15['GAMES']  = de15[['CR2_8_1', 'CR2_8_2', 'CR2_8_3']].any(axis=1).astype(float).replace(0,np.nan)
#de15['GAMES']  = de15[['CR2_8_1']].any(axis=1).astype(float).replace(0,np.nan)
#Game_dev=de15.GAMES==1

#cr6games = de.dist(de15[Game_dev],de15_meta,'CR6','WghtUniversal_Core')
#cr6g_pc=de.calc_pct(cr6games,pct_type='row')
#cr6g_pc.to_clipboard()
