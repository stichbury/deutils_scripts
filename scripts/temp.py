# -*- coding: utf-8 -*-
"""
Spyder Editor
Granny-Clanger:~ stichbury$ /Users/stichbury/anaconda/envs/py3/bin/spyder ; exit;


This is a temporary script file.
"""

# Imports
import pandas as pd
import deutils as de
import numpy as np

# weights
Sparta_Core = 'WghtUniversal_Core'

# Read DE15 data
de15 = de.read_sparta_survey(6)
de15_meta = de.meta(6)

# Read DE14 data
de14 = de.read_sparta_survey(5)
de14_meta = de.meta(5)

# Read DE13 data
de13 = de.read_sparta_survey(4)
de13_meta = de.meta(4)


#GAM1: What types of platform do you develop games for?
gam1 = de.dist(de15, de15_meta, 'GAM1', 'WghtUniversal_Game')
gam1pc = de.calc_pct(gam1)
gam1pc.to_clipboard()

#GAM1
gam1_14 = de.dist(de14, de14_meta, 'GAM1', 'WghtUniversal_Game')
gam1_14pc = de.calc_pct(gam1_14)
gam1_14pc.to_clipboard()

#GAM1
gam1_13 = de.dist(de13, de13_meta, 'GAM1', 'WghtUniversal_Game')
gam1_13pc = de.calc_pct(gam1_13)
gam1_13pc.to_clipboard()

#GAM2: Which consoles do you target with your games?
gam2 = de.dist(de15, de15_meta, 'GAM2', 'WghtUniversal_Game')
gam2pc = de.calc_pct(gam2)
gam2pc.to_clipboard()

#GAM1: Professional Devs - What types of platform do you develop games for?
de15['GAMES']  = de15[['CR2_8_1']].any(axis=1).astype(float).replace(0,np.nan)
pro_game_dev=de15.GAMES==1

gam1PRO = de.dist(de15[pro_game_dev], de15_meta, 'GAM1', 'WghtUniversal_Game')
gam1PROpc = de.calc_pct(gam1PRO)
gam1PROpc.to_clipboard()

de14['GAMES']  = de14[['CR2_8_1']].any(axis=1).astype(float).replace(0,np.nan)
pro_game_dev=de14.GAMES==1

gam1PRO_14 = de.dist(de14[pro_game_dev], de14_meta, 'GAM1', 'WghtUniversal_Game')
gam1PRO_14pc = de.calc_pct(gam1PRO_14)
gam1PRO_14pc.to_clipboard()

de13['GAMES']  = de13[['CR2_8_1']].any(axis=1).astype(float).replace(0,np.nan)
pro_game_dev=de13.GAMES==1

gam1PRO_13 = de.dist(de13[pro_game_dev], de13_meta, 'GAM1', 'WghtUniversal_Game')
gam1PRO_13pc = de.calc_pct(gam1PRO_13)
gam1PRO_13pc.to_clipboard()

#GAM2: Which consoles do you target with your games?
gam2 = de.dist(de15, de15_meta, 'GAM2', 'WghtUniversal_Game')
gam2pc = de.calc_pct(gam2)
gam2pc.to_clipboard()


#GAM2
gam2_14 = de.dist(de14, de14_meta, 'GAM2', 'WghtUniversal_Game')
gam2_14pc = de.calc_pct(gam2_14)
gam2_14pc.to_clipboard()

#GAM2
gam2_13 = de.dist(de13, de13_meta, 'GAM2', 'WghtUniversal_Game')
gam2_13pc = de.calc_pct(gam2_13)
gam2_13pc.to_clipboard()

#GAM3: Which Smart TVs or set-top boxes do you target with your games?
gam3 = de.dist(de15, de15_meta, 'GAM3', 'WghtUniversal_Game')
gam3pc = de.calc_pct(gam3)
gam3pc.to_clipboard()

#GAM3
gam3_14 = de.dist(de14, de14_meta, 'GAM3', 'WghtUniversal_Game')
gam3_14pc = de.calc_pct(gam3_14)
gam3_14pc.to_clipboard()

#GAM3
gam3_13 = de.dist(de13, de13_meta, 'GAM3', 'WghtUniversal_Game')
gam3_13pc = de.calc_pct(gam3_13)
gam3_13pc.to_clipboard()

#GAM5: Which programming languages do you use to write code that runs on the client side for your games?
gam5 = de.dist(de15, de15_meta, 'GAM5', 'WghtUniversal_Game')
gam5pc = de.calc_pct(gam5)
gam5pc.to_clipboard()

#GAM5
gam5_14 = de.dist(de14, de14_meta, 'GAM5', 'WghtUniversal_Game')
gam5_14pc = de.calc_pct(gam5_14)
gam5_14pc.to_clipboard()

#GAM5
gam5_13 = de.dist(de13, de13_meta, 'GAM5', 'WghtUniversal_Game')
gam5_13pc = de.calc_pct(gam5_13)
gam5_13pc.to_clipboard()


#GAM6 = "Why are you working on games?"
gam6 = de.dist(de15, de15_meta, 'GAM6', 'WghtUniversal_Game')
gam6pc = de.calc_pct(gam6)
gam6pc.to_clipboard()

# Now filter on pros, hobbyists and students
de15['GAMES']  = de15[['CR2_8_3']].any(axis=1).astype(float).replace(0,np.nan)
Game_dev=de15.GAMES==1

gam6f = de.dist(de15[Game_dev],de15_meta,'GAM6','WghtUniversal_Game')
gam6f_pc=de.calc_pct(gam6f)
gam6f_pc.to_clipboard()

#GAM7 = "How do you monetise your games?"
gam7 = de.dist(de15, de15_meta, 'GAM7', 'WghtUniversal_Game')
gam7pc = de.calc_pct(gam7)
gam7pc.to_clipboard()

# Filter out anything that is "Other, don't know, or we don't want to make money"
GAM7_14_excl=de15.GAM7_14.isnull() & de15.GAM7_15.isnull()& de15.GAM7_16.isnull() & de15.GAM7_17.isnull()

#Now I am applying the filter to my DE15 data
gam7f=de.dist(de15[GAM7_14_excl],de15_meta,'GAM7','WghtUniversal_Game')
gam7fpc = de.calc_pct(gam7f)
gam7fpc.to_clipboard()

#GAM8 = "What's your monthly revenue?"
gam8 = de.dist(de15[de15.GAM8<10], de15_meta, 'GAM8', 'WghtUniversal_Game')
gam8pc=de.calc_pct(gam8)
gam8pc.to_clipboard()

#GAM8 = "What's your monthly revenue?"
gam8_14 = de.dist(de15[de15.GAM8<10], de15_meta, 'GAM8', 'WghtUniversal_Game')
gam8_14pc=de.calc_pct(gam8_14)
gam8_14pc.to_clipboard()

#GAM8 = "What's your monthly revenue?"
gam8_13 = de.dist(de15[de15.GAM8<10], de15_meta, 'GAM8', 'WghtUniversal_Game')
gam8_13pc=de.calc_pct(gam8_13)
gam8_13pc.to_clipboard()


#GAM_PA "What technologies?"

gam_pa = de.dist(de15, de15_meta, 'GAM_PA', 'WghtUniversal_Game')
gam_pa_pc=de.calc_pct(gam_pa)
gam_pa_pc.to_clipboard()

#Filter GAM_PA by dev type
de15['GAMES']  = de15[['CR2_8_3']].any(axis=1).astype(float).replace(0,np.nan)
Game_dev=de15.GAMES==1

gam_pa_f = de.dist(de15[Game_dev], de15_meta, 'GAM_PA', 'WghtUniversal_Game')
gam_pa_f_pc=de.calc_pct(gam_pa_f)
gam_pa_f_pc.to_clipboard()



#CR2
cr2 =  de.dist(de15, de15_meta, 'CR2', 'WghtUniversal_Core')
cr2_pc = de.calc_pct(cr2)
cr2_pc.to_clipboard()

# CR6: experience levels
cr6 = de.dist(de15, de15_meta, 'CR6', 'WghtUniversal_Core')
cr6_pc = de.calc_pct(cr6, pct_type='row')
cr6_pc.to_clipboard()

# Filter by games pros
#de15['GAMES']  = de15[['CR2_8_1', 'CR2_8_2', 'CR2_8_3']].any(axis=1).astype(float).replace(0,np.nan)
de15['GAMES']  = de15[['CR2_8_1']].any(axis=1).astype(float).replace(0,np.nan)
Game_dev=de15.GAMES==1

cr6games = de.dist(de15[Game_dev],de15_meta,'CR6','WghtUniversal_Core')
cr6g_pc=de.calc_pct(cr6games,pct_type='row')
cr6g_pc.to_clipboard()



#Look at age levels
# whole dev population
cr_dev2 = de.dist(de15, de15_meta, 'CR_DEV2', 'WghtUniversal_Core')
cr_dev2_pc = de.calc_pct(cr_dev2)
cr_dev2_pc.to_clipboard()

#Just game devs (filter)

de15['GAMES']  = de15[['CR2_8_1', 'CR2_8_2', 'CR2_8_3']].any(axis=1).astype(float).replace(0,np.nan)
Game_dev=de15.GAMES==1

cr_dev2_games = de.dist(de15[Game_dev],de15_meta,'CR_DEV2','WghtUniversal_Core')
cr_dev2_games_pc=de.calc_pct(cr_dev2_games)
cr_dev2_games_pc.to_clipboard()

#CR3: organisation sizes
cr3 = de.dist(de15, de15_meta, 'CR3', 'WghtUniversal_Core')
cr3_pc = de.calc_pct(cr3)
cr3_pc.to_clipboard()

#Just game devs (filter)

de15['GAMES']  = de15[['CR2_8_1', 'CR2_8_2', 'CR2_8_3']].any(axis=1).astype(float).replace(0,np.nan)
Game_dev=de15.GAMES==1

cr3g = de.dist(de15[Game_dev],de15_meta,'CR3','WghtUniversal_Core')
cr3g_pc=de.calc_pct(cr3g)
cr3g_pc.to_clipboard()

#Just pro game devs (filter)

de15['GAMES']  = de15[['CR2_8_1']].any(axis=1).astype(float).replace(0,np.nan)
Game_dev=de15.GAMES==1

cr3gp = de.dist(de15[Game_dev],de15_meta,'CR3','WghtUniversal_Core')
cr3gp_pc=de.calc_pct(cr3gp)
cr3gp_pc.to_clipboard()


