# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 13:34:49 2018

@author: Eliud Lelerai
"""

import numpy as pd
import pandas as pd
from scipy import stats
import math

mean1=100
stdev=15
mean2=108
n=36

# Testing the hypothesis

#Step-1: Stating the hypotheses( The population mean is 100)
   #H0: μ= 100
  #H1: μ > 100(108)
  
#step-2:Step-2: Setting up the significance level. 
   #It is not given in the problem so let’s assume it as 5% (0.05)
   
#Step-3: Computing the random chance probability using z score

z=(mean2-mean1)/(15/math.sqrt(36))

import scipy.stats as st

z_prob=st.norm.cdf(3.2)
significance_value=1-z_prob

#Step-4: It is less than 0.05 so we will reject the Null hypothesis

# Infrence:  raw cornstarch had an effect

