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



#IN_TAM12
#For which of the following types of development / projects are you using the resources of Intel?


#CR_DPB1
#In the past 12 months, which of the following companies' official developer websites, documentation, events or support have you used?

#CR_DPB2
#In the past 12 months, how often have you visited or used the official developer websites, documentation, events or support of the following companies?


de16['GAMES']  = de16[['CR2b_8_1', 'CR2b_8_2', 'CR2b_8_3']].any(axis=1).astype(float).replace(0,np.nan)
game_dev=de16.GAMES==1

dpb1games = de.dist(de16[game_dev],de16_meta,'CR_DPB1','WghtUniversal_Core')
dpb1games_pc=de.calc_pct(dpb1games)
dpb1games_pc.to_clipboard()

dpb3games = de.dist(de16[game_dev],de16_meta,'CR_DPB3','WghtUniversal_Core')
dpb3games_pc=de.calc_pct(dpb3games)
dpb3games_pc.to_clipboard()

intam12 = de.dist(de16[game_dev],de16_meta,'IN_TAM12','WghtUniversal_Core')
intam12_pc=de.calc_pct(intam12)
intam12_pc.to_clipboard()

# Regions
regions=de.crosstab(de16, de16_meta, 'RegionCode8','CR2a', 'WghtUniversal_Core')
regions.to_clipboard()

# GAM1 - target device
gam1 = de.dist(de16, de16_meta, 'GAM1', 'WghtUniversal_Game')
gam1pc = de.calc_pct(gam1)
gam1pc.to_clipboard()


#GAM5 programming language
gam5 = de.dist(de16, de16_meta, 'GAM5', 'WghtUniversal_Game')
gam5pc = de.calc_pct(gam5)
gam5pc.to_clipboard()



##################

# Get CR_DPB1 option labels
cr_dpb1_olabels = de16_meta.get_option_labels('CR_DPB1', by='value')


# Construct metadata for CR_DPB1_TAM_COMPANY
CR_DPB1_TAM_COMPANY_meta = {'name': 'CR_DPB1_TAM_COMPANY',
                            'type': 'RADIO_LIST',
                            'title': '(Derived variable) List of TAM companies',
                            'options': [{'name': 'CR_DPB1_TAM_COMPANY' + key, 'value': key, 
                                  'text': cr_dpb1_olabels[key]} for key in cr_dpb1_olabels]}

# Add CR_DPB1_TAM_COMPANY to the metadata
if 'CR_DPB1_TAM_COMPANY' not in de16_meta.question_list:
    de16_meta.add_question_by_dict(CR_DPB1_TAM_COMPANY_meta)

intam13 = de.crosstab(de16[game_dev], de16_meta, 'CR_DPB1_TAM_COMPANY', 'IN_TAM13', 'WghtUniversal_Core')
#intam13_pc=de.calc_pct(intam13)
intam13.to_clipboard()

##################

# Read DE15 data
de15 = de.read_sparta_survey(6)
de15_meta = de.meta(6)

de15['GAMES']  = de15[['CR2_8_1', 'CR2_8_2', 'CR2_8_3']].any(axis=1).astype(float).replace(0,np.nan)
game_dev=de15.GAMES==1

dpb1games = de.dist(de15[game_dev],de15_meta,'CR_DPB1','WghtUniversal_Core')
dpb1games_pc=de.calc_pct(dpb1games)
dpb1games_pc.to_clipboard()

dpb3games = de.dist(de15[game_dev],de15_meta,'CR_DPB3','WghtUniversal_Core')
dpb3games_pc=de.calc_pct(dpb3games)
dpb3games_pc.to_clipboard()

##################

intam12 = de.dist(de15[game_dev],de15_meta,'IN_TAM12','WghtUniversal_Core')
intam12_pc=de.calc_pct(intam12)
intam12_pc.to_clipboard()

##################

# Get CR_DPB1 option labels
cr_dpb1_olabels = de15_meta.get_option_labels('CR_DPB1', by='value')


# Construct metadata for CR_DPB1_TAM_COMPANY
CR_DPB1_TAM_COMPANY_meta = {'name': 'CR_DPB1_TAM_COMPANY',
                            'type': 'RADIO_LIST',
                            'title': '(Derived variable) List of TAM companies',
                            'options': [{'name': 'CR_DPB1_TAM_COMPANY' + key, 'value': key, 
                                  'text': cr_dpb1_olabels[key]} for key in cr_dpb1_olabels]}

# Add CR_DPB1_TAM_COMPANY to the metadata
if 'CR_DPB1_TAM_COMPANY' not in de15_meta.question_list:
    de15_meta.add_question_by_dict(CR_DPB1_TAM_COMPANY_meta)

intam13 = de.crosstab(de15[game_dev], de15_meta, 'CR_DPB1_TAM_COMPANY', 'IN_TAM13', 'WghtUniversal_Core')
#intam13_pc=de.calc_pct(intam13)
intam13.to_clipboard()



##################


