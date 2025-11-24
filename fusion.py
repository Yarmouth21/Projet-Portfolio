import pandas as pd

tab1 = pd.read_csv('Tableau_trié.csv')
tab2 = pd.read_csv('Tableau2_trié.csv')

tab = pd.merge(tab1,tab2, on="date")

print(tab.head())