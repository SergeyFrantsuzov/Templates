# %%
import pandas as pd


# %%
df = pd.read_csv('Data.csv', sep=';', header=0)
# %%
df.rename(columns={"Porosity": "Parameter A", 
                   "Permeability_Kl": "Parameter B",
                   'Wells':'Classes_1',
                   'Zones':'Classes_2'}, 
                   inplace=True)

# %%         
filterDataDict={'Classes_1':'Class1_',
                'Classes_2':'Class2_'}

for f in filterDataDict.keys():
    for i, c in enumerate (df[f].unique()):
        
        df[f]=df[f].replace([str(c)],filterDataDict[f]+str(i))
# %%
df.to_csv('Data_clear.csv', index=False, encoding='utf-8-sig', sep=';')

# %%
