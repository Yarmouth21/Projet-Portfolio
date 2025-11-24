import pandas as pd

tab1 = pd.read_csv('Tableau_trié.csv')
tab2 = pd.read_csv('Tableau2_trié.csv')

tab = pd.merge(tab1,tab2, on="date")

tab = tab.drop(columns=["Unnamed: 0_x", "Unnamed: 0_y"])

print(tab.head())

tab["RET"] = pd.to_numeric(tab["RET"], errors="coerce")

filtre1 = tab[tab["RET"]>0.08]
prop = len(filtre1)/len(tab)
print("Pourcentage d'actions de la base avec un retour supérieur à 8% : "+ str(prop))

tab.to_csv("Fusionné.csv")