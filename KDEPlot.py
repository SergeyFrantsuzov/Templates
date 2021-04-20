# %%

#import matplotlib.pyplot as plt
#%matplotlib inline
#%matplotlib notebook
import numpy as np
import scipy.stats as st
import pandas as pd
import os
import time
# import seaborn as sns

# plotly standard imports
import plotly.graph_objects as go
import plotly.express as px
import chart_studio.plotly as py
from plotly.subplots import make_subplots

# Cufflinks wrapper on plotly
# import cufflinks as cf
# cf.go_offline()
# Options for pandas
pd.options.display.max_columns = 30
# Display all cell outputs
#from IPython.core.interactiveshell import InteractiveShell
#InteractiveShell.ast_node_interactivity = 'all'
# %%
df_RP=pd.read_csv('RPResultsForPython.csv', sep=';',header=0)

# %%
x_line=np.linspace(7000,11000,100)
y_line=2.43-0.072*x_line*0.001

fig=go.Figure()


fig.add_trace(go.Histogram2dContour(x =df_RP[df_RP["COLL"]==1]['AI_XW'], y = df_RP[df_RP["COLL"]==1]['VPVS_XW'], 
                                    colorscale = 'Blues',xaxis = 'x', yaxis = 'y',zmin=10,zmax=150, line=dict(color='green',width=1),
                                    name='Коллектор',
                                     contours=dict(coloring="none",start=10, end=150, size=10, showlabels = True)))# ncontours=20,  nbinsx=50, nbinsy=50 )) #, reversescale = True, xaxis = 'x', yaxis = 'y'))
fig.add_trace(go.Histogram2dContour(x =df_RP[df_RP["COLL"]==0]['AI_XW'], y = df_RP[df_RP["COLL"]==0]['VPVS_XW'], 
                                    colorscale = 'Blues',xaxis = 'x', yaxis = 'y',zmin=50,zmax=3000, line=dict(color='red', width=1),
                                    name='Неколлектор',
                                     contours=dict(coloring="none",start=50, end=3000, size=50,showlabels = True)))
fig.add_trace(go.Scatter(x=x_line, y=y_line,
                        mode='lines', 
                        #marker_size=2,
                        line_color='black',
                         showlegend=False
                        ))

fig.update_layout(height=600, width=600, legend=dict(yanchor="top",y=0.99,xanchor="right", x=0.99))
fig.update_xaxes(title='AI, kPa*s/m',showline=True, linewidth=2, titlefont=dict(size=20),
                 linecolor='black',range=[7000,11000])
fig.update_yaxes(title='VPVS',showline=True, linewidth=2, titlefont=dict(size=20),
                 linecolor='black',range=[1.6,2.2])
fig.show()     
# %%
