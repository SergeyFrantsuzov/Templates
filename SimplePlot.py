import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

df = pd.read_csv('Data.csv', sep=';', header=0)

fig = px.scatter(df, 
                x="Porosity", 
                y="Permeability_Kl",
                log_y=True,
                range_x=[0,30], 
                range_y=[0.001,10000], 
                color="Wells")
fig.show()

def perm_calc(*args):
    x, a, f, s = args
    return np.exp(a*x**f-s)
x = np.linspace(0.01,30,100)
y = perm_calc( x, 0.01, 2.2, 4.5)
fig.add_trace(go.Scatter(x=x,
                        y=y,
                        mode='lines',
                        name='function'
))
