#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:07:50 2019

@author: stichbury
"""



# Imports
import pandas as pd
import deutils as de
import numpy as np

# weights
Sparta_Core = 'WghtUniversal_Core'

##################
# Read de13 data
de13 = de.read_sparta_survey(4)
de13_meta = de.meta(4)
##################


#MOB3: What programming languages?
mob3 = de.dist(de13, de13_meta, 'MOB3', 'WghtUniversal_Mob')
mob3pc = de.calc_pct(mob3)
mob3pc.to_clipboard()

# Mobile professionals only
de13['Prof']  = (de13[['CR2_2_1']].any(axis=1)).astype(float).replace(0,2)
pros_only = de.dist(de13[de13.Prof==1], de13_meta, 'MOB3', 'WghtUniversal_Core')
pros_onlypc = de.calc_pct(pros_only)
pros_onlypc.to_clipboard()

#Filter mobile devs programming language choice by those that use cross platform dev tools
de13['xplat']  = (de13[['MOB_PA_1']].any(axis=1)).astype(float).replace(0,2)
mob3_xplat = de.dist(de13[de13.xplat==1], de13_meta, 'MOB3', 'WghtUniversal_Mob')
mob3_xplatpc = de.calc_pct(mob3_xplat)
mob3_xplatpc.to_clipboard()


#Crosstab all devs geographical regions against development area
regions=de.crosstab(de13, de13_meta, 'RegionCode8','CR2', 'WghtUniversal_Core')
regions.to_clipboard()


de13['MOBILE']  = de13[['CR2_2_1', 'CR2_2_2', 'CR2_2_3']].any(axis=1).astype(float).replace(0,np.nan)
mob_dev=(de13.MOBILE==1)

de13['OTHERS']  = de13[['CR2_1_1', 'CR2_1_1', 'CR2_1_1',
    'CR2_3_1','CR2_3_2','CR2_3_3',
    'CR2_4_1','CR2_4_2','CR2_4_3',
    'CR2_5_1','CR2_5_2','CR2_5_3',
    'CR2_6_1','CR2_6_2','CR2_6_3',
    'CR2_7_1','CR2_7_2','CR2_7_3',
    'CR2_8_1','CR2_8_2','CR2_8_3',
    'CR2_9_1','CR2_9_2','CR2_9_3']].any(axis=1).astype(float).replace(0,np.nan)

other_dev = (de13.OTHERS==1)

#Look at age levels
# whole dev population except mobile devs
cr_dev2 = de.dist(de13[other_dev], de13_meta, 'CR_DEV2', 'WghtUniversal_Core')
cr_dev2_pc = de.calc_pct(cr_dev2)
cr_dev2_pc.to_clipboard()

cr_dev2_mobile = de.dist(de13[mob_dev],de13_meta,'CR_DEV2','WghtUniversal_Core')
cr_dev2_mobile_pc=de.calc_pct(cr_dev2_mobile)
cr_dev2_mobile_pc.to_clipboard()