from matplotlib.pyplot import axis
import pandas as pd
import csv
df = pd.read_csv("total_stars.csv")
del df["Distance1"]
del df["Mass1"]
del df["Radius1"]
del df["Luminosity"]
del df["Star_name1"]

df.to_csv('pmain.csv')