
# coding: utf-8

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

traffic=pd.read_csv('../data/train_2.csv')

key=pd.read_csv('../data/key_2.csv')

sub=pd.read_csv('../data/sample_submission_2.csv')

names=traffic.Page.values

langs=[]
access=[]
vtype=[]
entity=[]
for n in names:
    elements=n.split('_')
    langs.append(elements[-3])
    access.append(elements[-2])
    vtype.append(elements[-1])
    entity.append(' '.join(elements[:-3]))


traffic['langs']=langs
traffic['vtype']=vtype
traffic['access']=access
traffic['entity']=entity
traffic.drop(['Page'],axis=1,inplace=True)

traffic.to_csv('../data/cl_traffic.csv',index=False)

