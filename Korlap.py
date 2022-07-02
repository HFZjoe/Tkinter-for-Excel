import pandas as pd
import numpy as np

# MEMBACA FILE 

df1 = pd.read_excel('Input.xlsx')   # FILE INPUT
df2 = pd.read_excel('New1.xlsx')     # FILE FIX INPUT AGENT / FILE KORLAP
df3 = pd.read_excel('Output.xlsx')  # FILE AKHIR / OUTPUT

# MENDAPAT NILAI KORLAP

df4 = pd.merge(df1, df2[['AGENT_ID', 'Korlap_10%']], on='AGENT_ID', how='left')

# MENGINPUT KE FILE OUTPUT

df5 = pd.merge(df3, df4[['MASTER_AGENT_ID', 'Korlap_10%']], on='MASTER_AGENT_ID', how='left')
df6 = np.floor(df5.groupby(by="MASTER_AGENT_ID").sum()[["Korlap_10%"]])
df6.reset_index(inplace=True)

df7 = pd.merge(df3, df6[['MASTER_AGENT_ID', 'Korlap_10%']], on='MASTER_AGENT_ID', how='left')

df3["TRANSFER_VALUE"] = df7['Korlap_10%']

df3.to_excel("New3.xlsx",index=False)

# df3