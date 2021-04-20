# %%
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
# %%
df = pd.read_csv('Data.csv', sep=';', header=0)
# %%


fig = px.scatter(df, 
                x="Porosity", 
                y="Permeability_Kl",
                log_y=True,
                range_x=[0,30], 
                range_y=[0.001,10000], 
                color="Wells")

fig.update_layout(height=600, width=600, 
                 legend=dict(yanchor="top",y=0.99,xanchor="right", x=0.99))
fig.update_xaxes(title='AI, kPa*s/m',showline=True, linewidth=2, 
                 titlefont=dict(size=20),
                 linecolor='black',range=[7000,11000])
fig.update_yaxes(title='VPVS',showline=True, linewidth=2, 
                 titlefont=dict(size=20),
                 linecolor='black',range=[1.6,2.2])


fig.show()

# def perm_calc(*args):
#     x, a, f, s = args
#     return np.exp(a*x**f-s)
# x = np.linspace(0.01,30,100)
# y = perm_calc( x, 0.01, 2.2, 4.5)
# fig.add_trace(go.Scatter(x=x,
#                         y=y,
#                         mode='lines',
#                         name='function'
# ))

# %%
