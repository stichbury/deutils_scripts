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



# CR_DEVCNT2 for DE16
cr_devcnt2_16 =  de.dist(de16, de16_meta, 'CR_DEVCNT2', 'WghtUniversal_Core')
cr_devcnt2_16.to_clipboard()

# Professionals - what do you think?
# Filter on any dev who is professional in at least one sector

de16['Prof']  = (de16[['CR2b_1_1', 'CR2b_2_1', 'CR2b_3_1','CR2b_4_1','CR2b_5_1','CR2b_6_1','CR2b_7_1','CR2b_8_1','CR2b_9_1','CR2b_10_1']].any(axis=1)).astype(float).replace(0,2)

pros_only = de.dist(de16[de16.Prof==1], de16_meta, 'CR_DEVCNT2', 'WghtUniversal_Core')
pros_only.to_clipboard()

# Filter on any dev who is not professional in any sector
non_pros_only = de.dist(de16[de16.Prof==2], de16_meta, 'CR_DEVCNT2', 'WghtUniversal_Core')
non_pros_only.to_clipboard()


# CR_DEVCNT2 for DE16
cr_devcnt2_16 =  de.dist(de16, de16_meta, 'CR_DEVCNT2', 'WghtUniversal_Core')
cr_devcnt2_16.to_clipboard()

# What do machine learning devs think?
# Filter on any dev who is working on ML/AI (pro or non-pro)

de16['ML']  = (de16[['CR2b_10_1', 'CR2b_10_2', 'CR2b_10_3']].any(axis=1)).astype(float).replace(0,2)

ml_only = de.dist(de16[de16.ML==1], de16_meta, 'CR_DEVCNT2', 'WghtUniversal_Core')
ml_only.to_clipboard()

# What do mobile  devs think?
# Filter on any dev who is working on mobile (pro or non-pro)

de16['Mobile']  = (de16[['CR2b_2_1', 'CR2b_2_2', 'CR2b_2_3']].any(axis=1)).astype(float).replace(0,2)

mobile_only = de.dist(de16[de16.Mobile==1], de16_meta, 'CR_DEVCNT2', 'WghtUniversal_Core')
mobile_only.to_clipboard()


# What do IoT devs think?
# Filter on any dev who is working on IoT (pro or non-pro)

de16['IoT']  = (de16[['CR2b_5_1', 'CR2b_5_2', 'CR2b_5_3']].any(axis=1)).astype(float).replace(0,2)

IoT_only = de.dist(de16[de16.IoT==1], de16_meta, 'CR_DEVCNT2', 'WghtUniversal_Core')
IoT_only.to_clipboard()







# Now read DE15 data
de15 = de.read_sparta_survey(6)
de15_meta = de.meta(6)


# CR_DEVCNT2 for DE15
cr_devcnt2_15 =  de.dist(de15, de15_meta, 'CR_DEVCNT2', 'WghtUniversal_Core')
cr_devcnt2_15.to_clipboard()
