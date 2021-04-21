# %%
import numpy as np
import pandas as pd
import os

import plotly.graph_objects as go


# %%
df_RP=pd.read_csv('RPResultsForPython.csv', sep=';',header=0)

# %%

fig=go.Figure()

fig.add_trace(go.Histogram2dContour(x =df_RP[df_RP["COLL"]==1]['AI_XW'], 
                                    y = df_RP[df_RP["COLL"]==1]['VPVS_XW'], 
                                    colorscale = 'Blues',
                                    zmin=10,
                                    zmax=150, 
                                    line=dict(color='green',width=1),
                                    name='Коллектор',
                                    contours=dict(coloring="none",
                                                  start=10, end=150, 
                                                  size=10, showlabels = True)))
fig.add_trace(go.Histogram2dContour(x =df_RP[df_RP["COLL"]==0]['AI_XW'], 
                                    y = df_RP[df_RP["COLL"]==0]['VPVS_XW'], 
                                    colorscale = 'Blues',
                                    zmin=50,
                                    zmax=3000, 
                                    line=dict(color='red', width=1),
                                    name='Неколлектор',
                                    contours=dict(coloring="none",
                                                  start=50, end=3000, 
                                                  size=50,showlabels = True)))

fig.update_layout(height=600, width=600, 
                 legend=dict(yanchor="top",y=0.99,xanchor="right", x=0.99),
                 template='plotly_white')
fig.update_xaxes(title='AI, kPa*s/m',showline=True, linewidth=2, 
                 titlefont=dict(size=20),
                 linecolor='black',range=[7000,11000])
fig.update_yaxes(title='VPVS',showline=True, linewidth=2, 
                 titlefont=dict(size=20),
                 linecolor='black',range=[1.6,2.2])
fig.show()     
# %%
