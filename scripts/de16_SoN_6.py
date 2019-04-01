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

# Read DE16 data
de16 = de.read_sparta_survey(7)
de16_meta = de.meta(7)

##################

#Look at age levels (CR_DEV2)
# whole dev population
cr_dev2 = de.dist(de16, de16_meta, 'CR_DEV2', 'WghtUniversal_Core')
cr_dev2_pc = de.calc_pct(cr_dev2)
cr_dev2_pc.to_clipboard()

#Experience (CR6)
#Just women devs (filter)
dev_female = de.dist(de16[de16['CR_DEV3']==1],de16_meta,'CR6','WghtUniversal_Core')
dev_female.to_clipboard()

#Just male devs (filter)
dev_male = de.dist(de16[de16['CR_DEV3']==3],de16_meta,'CR6','WghtUniversal_Core')
dev_male.to_clipboard()


#crosstab CR_DEV2 (age) with CR5 (job description/role) -- women
crosstab=de.crosstab(de16[de16['CR_DEV3']==1], de16_meta, 'CR5', 'CR_DEV2', 'WghtUniversal_Core')
crosstab.to_clipboard()

crosstab=de.crosstab(de16[de16['CR_DEV3']==3], de16_meta, 'CR5', 'CR_DEV2', 'WghtUniversal_Core')
crosstab.to_clipboard()

#Age
#Just women devs (filter)
dev_female = de.dist(de16[de16['CR_DEV3']==1],de16_meta,'CR_DEV2','WghtUniversal_Core')
dev_female_pc=de.calc_pct(dev_female)
dev_female_pc.to_clipboard()

#Just male devs (filter)
dev_male = de.dist(de16[de16['CR_DEV3']==3],de16_meta,'CR_DEV2','WghtUniversal_Core')
dev_male_pc=de.calc_pct(dev_male)
dev_male_pc.to_clipboard()

#Region
#Just women devs (filter)
dev_female = de.dist(de16[de16['CR_DEV3']==1],de16_meta,'CR1','WghtUniversal_Core')
dev_female_pc=de.calc_pct(dev_female)
dev_female_pc.to_clipboard()

#Just male devs (filter)
dev_male = de.dist(de16[de16['CR_DEV3']==3],de16_meta,'CR1','WghtUniversal_Core')
dev_male_pc=de.calc_pct(dev_male)
dev_male_pc.to_clipboard()

#excluding the "I prefer not to specify" option -> [de16.CR_DEV3<4]
regions=de.crosstab(de16[de16.CR_DEV3<4], de16_meta, 'RegionCode8','CR_DEV3', 'WghtUniversal_Core')
regions_pc=de.calc_pct(regions)
regions_pc.to_clipboard()

#Crosstab regions against development area
regions=de.crosstab(de16, de16_meta, 'RegionCode8','CR2a', 'WghtUniversal_Core')
regions.to_clipboard()

#Look at areas of development (CR2a)
#Just women devs (filter)
dev_female = de.dist(de16[de16['CR_DEV3']==1],de16_meta,'CR2a','WghtUniversal_Core')
dev_female_pc=de.calc_pct(dev_female)
dev_female_pc.to_clipboard()

#Just male devs (filter)
dev_male = de.dist(de16[de16['CR_DEV3']==3],de16_meta,'CR2a','WghtUniversal_Core')
dev_male_pc=de.calc_pct(dev_male)
dev_male_pc.to_clipboard()

#ML1: How are you involved in data science / machine learning (ML) / AI?
#Just women devs (filter)
dev_female = de.dist(de16[de16['CR_DEV3']==1],de16_meta,'ML1','WghtUniversal_ML')
dev_female_pc=de.calc_pct(dev_female)
dev_female_pc.to_clipboard()

#Just male devs (filter)
dev_male = de.dist(de16[de16['CR_DEV3']==3],de16_meta,'ML1','WghtUniversal_ML')
dev_male_pc=de.calc_pct(dev_male)
dev_male_pc.to_clipboard()

#Look at professional status (CR2b)
#Just women devs (filter)
dev_female = de.dist(de16[de16['CR_DEV3']==1],de16_meta,'CR2b','WghtUniversal_Core')
dev_female_pc=de.calc_pct(dev_female)
dev_female_pc.to_clipboard()

#Just male devs (filter)
dev_male = de.dist(de16[de16['CR_DEV3']==3],de16_meta,'CR2b','WghtUniversal_Core')
dev_male_pc=de.calc_pct(dev_male)
dev_male_pc.to_clipboard()

#Look at how people learn to code (CR_DEV4)
#Just women devs (filter)
dev_female = de.dist(de16[de16['CR_DEV3']==1],de16_meta,'CR_DEV4','WghtUniversal_Core')
dev_female_pc=de.calc_pct(dev_female)
dev_female_pc.to_clipboard()

#Just male devs (filter)
dev_male = de.dist(de16[de16['CR_DEV3']==3],de16_meta,'CR_DEV4','WghtUniversal_Core')
dev_male_pc=de.calc_pct(dev_male)
dev_male_pc.to_clipboard()

#Size of the organisation (CR3)
#Just women devs (filter)
dev_female = de.dist(de16[de16['CR_DEV3']==1],de16_meta,'CR3','WghtUniversal_Core')
dev_female_pc=de.calc_pct(dev_female)
dev_female_pc.to_clipboard()

#Just male devs (filter)
dev_male = de.dist(de16[de16['CR_DEV3']==3],de16_meta,'CR3','WghtUniversal_Core')
dev_male_pc=de.calc_pct(dev_male)
dev_male_pc.to_clipboard()

#Role in the team 
#Just women devs (filter)
dev_female = de.dist(de16[de16['CR_DEV3']==1],de16_meta,'CR5','WghtUniversal_Core')
dev_female_pc=de.calc_pct(dev_female)
dev_female_pc.to_clipboard()

#Just male devs (filter)
dev_male = de.dist(de16[de16['CR_DEV3']==3],de16_meta,'CR5','WghtUniversal_Core')
dev_male_pc=de.calc_pct(dev_male)
dev_male_pc.to_clipboard()

#Sectors 
#Just women devs (filter)
dev_female = de.dist(de16[de16['CR_DEV3']==1],de16_meta,'CR_PROF1','WghtUniversal_Core')
dev_female_pc=de.calc_pct(dev_female)
dev_female_pc.to_clipboard()

#Just male devs (filter)
dev_male = de.dist(de16[de16['CR_DEV3']==3],de16_meta,'CR_PROF1','WghtUniversal_Core')
dev_male_pc=de.calc_pct(dev_male)
dev_male_pc.to_clipboard()

#Github usage
#Just women devs (filter)
dev_female = de.dist(de16[de16['CR_DEV3']==1],de16_meta,'CR_POP1','WghtUniversal_Core')
dev_female_pc=de.calc_pct(dev_female)
dev_female_pc.to_clipboard()

#Just male devs (filter)
dev_male = de.dist(de16[de16['CR_DEV3']==3],de16_meta,'CR_POP1','WghtUniversal_Core')
dev_male_pc=de.calc_pct(dev_male)
dev_male_pc.to_clipboard()

#Stack Overflow usage
#Just women devs (filter)
dev_female = de.dist(de16[de16['CR_DEV3']==1],de16_meta,'CR_POP2','WghtUniversal_Core')
dev_female_pc=de.calc_pct(dev_female)
dev_female_pc.to_clipboard()

#Just male devs (filter)
dev_male = de.dist(de16[de16['CR_DEV3']==3],de16_meta,'CR_POP2','WghtUniversal_Core')
dev_male_pc=de.calc_pct(dev_male)
dev_male_pc.to_clipboard()

#Emerging technology
#Just women devs (filter)
dev_female = de.dist(de16[de16['CR_DEV3']==1], de16_meta, 'CR_DEVCNT2', 'WghtUniversal_Core')
dev_female.to_clipboard()

#Just male devs (filter)
dev_male = de.dist(de16[de16['CR_DEV3']==3], de16_meta, 'CR_DEVCNT2', 'WghtUniversal_Core')
dev_male.to_clipboard()



