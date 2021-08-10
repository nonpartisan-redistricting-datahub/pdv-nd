import pandas as pd
import geopandas as gp
import numpy as np 
import os
import fiona
from statistics import mean, median
import string
import sys

df = []
f = "./raw-from-source/Election_Results/Statewide_Precinct_Results_Auditor.xlsx/"
numberOfSheets = 53

for i in range(1, numberOfSheets+1):
    data = pd.read_excel(f)
    df.append(data)
final = "./raw_from_source/Election_Results/merged.xlsx"
df = pd.concat(df)
df.to_excel(final)
