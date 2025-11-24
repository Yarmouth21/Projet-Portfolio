import pandas as pd

def ouverture(files):
    df = pd.read_csv(files, sep=",",header=0)
    return df

file = ouverture('data.csv')

file["date"] = pd.to_datetime(file["date"])

# df_filtre = file[file["date"].dt.year<1985]
# print(df_filtre.head())

tab_trier = file.sort_values(by="date")
tab_trier = tab_trier[tab_trier["EXCHCD"]<4.0]
tab_trier["PRC"] = abs(tab_trier["PRC"])
tab_trier = tab_trier[tab_trier["PRC"]>1]
tab_trier = tab_trier[(tab_trier["SHRCD"] == 10) | (tab_trier["SHRCD"] == 11)]
tab_trier["date"] = tab_trier["date"].dt.to_period("M")
print(tab_trier.head())

tab_trier.to_csv("Tableau_trié.csv")