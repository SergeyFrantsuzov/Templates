# %%
import pandas as pd


# %%
df = pd.read_csv('Data.csv', sep=';', header=0)
# %%
filterDataDict={'Wells':'Well_',
                'Zones':'Zone_'}

for f in filterDataDict.keys():
    for i, w in enumerate (df[f].unique()):

        df[f]=df[f].replace([str(w)],filterDataDict[f]+str(i))
# %%
df.to_csv('Data_clear.csv', index=False, encoding='utf-8', sep=';')
