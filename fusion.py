import pandas as pd

tab1 = pd.read_csv('Tableau_trié.csv')
tab2 = pd.read_csv('Tableau2_trié.csv')

tab = pd.merge(tab1,tab2, on="date")

tab = tab.drop(columns=["Unnamed: 0_x", "Unnamed: 0_y"])

print(tab.head())