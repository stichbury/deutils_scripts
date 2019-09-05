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
import numpy as np
import warnings
import deutils as de
import numpy as np

import dill
import pathlib
path = pathlib.Path.home().joinpath('Documents/Github/slashdata/deutils/scripts/scripts/')
dill.load_session(path/'de_env.db')






# Exploring NVIDIA have more C# and Shading Languages but fewer C/C++ and much fewer Java/JavaScript. 

# Game devs and their programming languages GAM5
# CR_DPB1_12_Intel
# CR_DPB1_3_AMD
# CR_DPB1_15_NVIDIA

#Intel
de16['IntelDevs'] = de16[['CR_DPB1_12']].any(axis=1).astype(float).replace(0,np.nan)
inteldevs=de16.IntelDevs==1

# Everyone but Intel
de16['NotIntelDevs'] = de16[['CR_DPB1_1', 'CR_DPB1_2', 'CR_DPB1_3', 'CR_DPB1_4', 'CR_DPB1_5', 'CR_DPB1_6', 'CR_DPB1_7', 'CR_DPB1_8', 'CR_DPB1_9', 'CR_DPB1_10', 'CR_DPB1_11', 'CR_DPB1_13', 'CR_DPB1_14', 'CR_DPB1_15', 'CR_DPB1_16', 'CR_DPB1_17', 'CR_DPB1_18', 'CR_DPB1_19', 'CR_DPB1_20', 'CR_DPB1_21', 'CR_DPB1_22', 'CR_DPB1_23', 'CR_DPB1_24']].any(axis=1).astype(float).replace(0,np.nan)
ninteldevs=de16.NotIntelDevs==1

# NO Intel, AMD or NVIDIA
de16['NDevs'] = de16[['CR_DPB1_1', 'CR_DPB1_2', 'CR_DPB1_4', 'CR_DPB1_5', 'CR_DPB1_6', 'CR_DPB1_7', 'CR_DPB1_8', 'CR_DPB1_9', 'CR_DPB1_10', 'CR_DPB1_11', 'CR_DPB1_13', 'CR_DPB1_14', 'CR_DPB1_16', 'CR_DPB1_17', 'CR_DPB1_18', 'CR_DPB1_19', 'CR_DPB1_20', 'CR_DPB1_21', 'CR_DPB1_22', 'CR_DPB1_23', 'CR_DPB1_24']].any(axis=1).astype(float).replace(0,np.nan)
ndevs=de16.NDevs==1

# AMD
de16['AMDDevs'] = de16[['CR_DPB1_3']].any(axis=1).astype(float).replace(0,np.nan)
amddevs=de16.AMDDevs==1

# NVIDIA
de16['NVIDIADevs'] = de16[['CR_DPB1_15']].any(axis=1).astype(float).replace(0,np.nan)
nvdevs=de16.NVIDIADevs==1

# game devs
de16['GAMES']  = de16[['CR2b_8_1', 'CR2b_8_2', 'CR2b_8_3']].any(axis=1).astype(float).replace(0,np.nan)
game_dev=de16.GAMES==1

# GAM5 - Language
gam5 = de.dist(de16[inteldevs],de16_meta,'GAM5','WghtUniversal_Game')
gam5_pc=de.calc_pct(gam5)
gam5_pc.to_clipboard()

gam5 = de.dist(de16[ninteldevs],de16_meta,'GAM5','WghtUniversal_Game')
gam5_pc=de.calc_pct(gam5)
gam5_pc.to_clipboard()

gam5 = de.dist(de16[amddevs],de16_meta,'GAM5','WghtUniversal_Game')
gam5_pc=de.calc_pct(gam5)
gam5_pc.to_clipboard()

gam5 = de.dist(de16[nvdevs],de16_meta,'GAM5','WghtUniversal_Game')
gam5_pc=de.calc_pct(gam5)
gam5_pc.to_clipboard()

gam5 = de.dist(de16[ndevs],de16_meta,'GAM5','WghtUniversal_Game')
gam5_pc=de.calc_pct(gam5)
gam5_pc.to_clipboard()


# Regions
regions=de.crosstab(de16[inteldevs], de16_meta, 'RegionCode8','CR2a', 'WghtUniversal_Game')
regions.to_clipboard()

regions=de.crosstab(de16[ninteldevs], de16_meta, 'RegionCode8','CR2a', 'WghtUniversal_Game')
regions.to_clipboard()

regions=de.crosstab(de16[amddevs], de16_meta, 'RegionCode8','CR2a', 'WghtUniversal_Game')
regions.to_clipboard()

    regions=de.crosstab(de16[nvdevs], de16_meta, 'RegionCode8','CR2a', 'WghtUniversal_Game')
    regions.to_clipboard()

# GAM1 - target device
gam1 = de.dist(de16[inteldevs], de16_meta, 'GAM1', 'WghtUniversal_Game')
gam1pc = de.calc_pct(gam1)
gam1pc.to_clipboard()

gam1 = de.dist(de16[ninteldevs], de16_meta, 'GAM1', 'WghtUniversal_Game')
gam1pc = de.calc_pct(gam1)
gam1pc.to_clipboard()

gam1 = de.dist(de16[amddevs], de16_meta, 'GAM1', 'WghtUniversal_Game')
gam1pc = de.calc_pct(gam1)
gam1pc.to_clipboard()

gam1 = de.dist(de16[nvdevs], de16_meta, 'GAM1', 'WghtUniversal_Game')
gam1pc = de.calc_pct(gam1)
gam1pc.to_clipboard()

gam1 = de.dist(de16[ndevs],de16_meta,'GAM1','WghtUniversal_Game')
gam1_pc=de.calc_pct(gam1)
gam1_pc.to_clipboard()


# CR6: experience levels
de16['GAMES']  = de16[['CR2b_8_1', 'CR2b_8_2', 'CR2b_8_3']].any(axis=1).astype(float).replace(0,np.nan)
game_dev=de16.GAMES==1

cr6 = de.dist(de16[inteldevs], de16_meta, 'CR6', 'WghtUniversal_Core')
cr6_pc = de.calc_pct(cr6, pct_type='row')
cr6_pc.to_clipboard()

cr6 = de.dist(de16[ndevs], de16_meta, 'CR6', 'WghtUniversal_Core')
cr6_pc = de.calc_pct(cr6, pct_type='row')
cr6_pc.to_clipboard()

#CR_DPB3
dpb3games = de.dist(de16[game_dev & inteldevs],de16_meta,'CR_DPB3','WghtUniversal_Core')
dpb3games_pc=de.calc_pct(dpb3games)
dpb3games_pc.to_clipboard()

dpb3games = de.dist(de16[game_dev & ndevs],de16_meta,'CR_DPB3','WghtUniversal_Core')
dpb3games_pc=de.calc_pct(dpb3games)
dpb3games_pc.to_clipboard()

dpb3games = de.dist(de16[game_dev & amddevs],de16_meta,'CR_DPB3','WghtUniversal_Core')
dpb3games_pc=de.calc_pct(dpb3games)
dpb3games_pc.to_clipboard()

dpb3games = de.dist(de16[game_dev & nvdevs],de16_meta,'CR_DPB3','WghtUniversal_Core')
dpb3games_pc=de.calc_pct(dpb3games)
dpb3games_pc.to_clipboard()

# GAM 7 - how do you make money
# Intel devs like advertising, NVIDIA devs like pay per download, similarly AMD (but equal on ads)
# Many more NVIDIA devs are making no monthly revenue than Intel devs. Intel devs do much better over 1000 USD per month. AMD and Intel about the same


gam7 = de.dist(de16[inteldevs], de16_meta, 'GAM7', 'WghtUniversal_Game')
gam7pc = de.calc_pct(gam7)
gam7pc.to_clipboard()

gam7 = de.dist(de16[ninteldevs], de16_meta, 'GAM7', 'WghtUniversal_Game')
gam7pc = de.calc_pct(gam7)
gam7pc.to_clipboard()

gam7 = de.dist(de16[amddevs], de16_meta, 'GAM7', 'WghtUniversal_Game')
gam7pc = de.calc_pct(gam7)
gam7pc.to_clipboard()

gam7 = de.dist(de16[nvdevs], de16_meta, 'GAM7', 'WghtUniversal_Game')
gam7pc = de.calc_pct(gam7)
gam7pc.to_clipboard()


# GAM 8 - how much money
gam8 = de.dist(de16[inteldevs], de16_meta, 'GAM8', 'WghtUniversal_Game')
gam8pc = de.calc_pct(gam8)
gam8pc.to_clipboard()

gam8 = de.dist(de16[ninteldevs], de16_meta, 'GAM8', 'WghtUniversal_Game')
gam8pc = de.calc_pct(gam8)
gam8pc.to_clipboard()

gam8 = de.dist(de16[amddevs], de16_meta, 'GAM8', 'WghtUniversal_Game')
gam8pc = de.calc_pct(gam8)
gam8pc.to_clipboard()

gam8 = de.dist(de16[nvdevs], de16_meta, 'GAM8', 'WghtUniversal_Game')
gam8pc = de.calc_pct(gam8)
gam8pc.to_clipboard()



# GAM_PA - which technologies
gam_pa = de.dist(de16[inteldevs], de16_meta, 'GAM_PA', 'WghtUniversal_Game')
gam_papc = de.calc_pct(gam_pa)
gam_papc.to_clipboard()

gam_pa = de.dist(de16[ninteldevs], de16_meta, 'GAM_PA', 'WghtUniversal_Game')
gam_papc = de.calc_pct(gam_pa)
gam_papc.to_clipboard()

gam_pa = de.dist(de16[amddevs], de16_meta, 'GAM_PA', 'WghtUniversal_Game')
gam_papc = de.calc_pct(gam_pa)
gam_papc.to_clipboard()

gam_pa = de.dist(de16[nvdevs], de16_meta, 'GAM_PA', 'WghtUniversal_Game')
gam_papc = de.calc_pct(gam_pa)
gam_papc.to_clipboard()



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

gam5 = de.dist(de14, de14_meta, 'GAM5', 'WghtUniversal_Game')
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


