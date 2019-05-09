#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 17:19:49 2019

@author: stichbury
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
de12 = de.read_sparta_survey(3)
de12_meta = de.meta(3)
##################



# CR6: experience levels over survey
cr6 = de.dist(de12, de12_meta, 'CR6', 'WghtUniversal_Core')
cr6_pc = de.calc_pct(cr6, pct_type='row')
cr6_pc.to_clipboard()
