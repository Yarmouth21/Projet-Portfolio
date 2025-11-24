import pandas as pd

def ouverture(files):
    pf = pd.read_csv(files)
    return pf

file = ouverture('Factor_Data.csv')
file = file.drop(columns=["SMB"])
file["Date"] = pd.to_datetime(file["Date"], format="%Y%m")
file = file.rename(columns={'Date':'date'})
file["date"] = file["date"].dt.to_period("M")
print(file.head())

file.to_csv("Tableau2_trié.csv")