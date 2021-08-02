import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# import csvs and concatentane, adding a phase id column, sort heders, create markersize, invert depth

num_of_phases = 5
min_mag = -3.0

phases = []

for i in range(num_of_phases):
    df = pd.read_csv ('events/P{}-locations.csv'.format(i+1))
    df["Phase"] = "P{}".format(i+1)
    df= df.rename(columns={"      X     ":"X","      Y     ":"Y",'    Depth   ':"Depth", " MomMag":"MomMag" })
    df = df[df["MomMag"] >= min_mag]
    df["Depth"] = df["Depth"] * -1
    df["MarkerSize"] = 1 / (df["MomMag"]**2)
    phases.append(df)
    
# plot phase events into 3D psace

fig = go.Figure()

for idx, phase in enumerate(phases):

    m=phase["MarkerSize"]
    n = "Phase {}".format(idx+1)

    fig.add_trace(go.Scatter3d(x=phase["X"],
                               y=phase["Y"],
                               z=phase["Depth"],
                               mode='markers', 
                               marker=dict(size=40*m, line=dict(width=2, color='DarkSlateGrey')),
                               name=n
                              )
                 )

# add tunnnel and welltraks to fig

colnames=['id', 'X', 'Y', 'Z', 'MD']

df_tunnel = pd.read_csv ('welltraks/tunnel.csv', header=None, delimiter=r"\s+", names=colnames)
df_tunnel["Z"] = df_tunnel["Z"] * -1

df_st1 = pd.read_csv ('welltraks/ST1.csv', header=None, delimiter=r"\s+", names=colnames)
df_st1["Z"] = df_st1["Z"] * -1

df_st2 = pd.read_csv ('welltraks/ST2.csv', header=None, delimiter=r"\s+", names=colnames)
df_st2["Z"] = df_st2["Z"] * -1

df_mb5 = pd.read_csv ('welltraks/MB5.csv', header=None, delimiter=r"\s+", names=colnames)
df_mb5["Z"] = df_mb5["Z"] * -1

df_mb8 = pd.read_csv ('welltraks/MB8.csv', header=None, delimiter=r"\s+", names=colnames)
df_mb8["Z"] = df_mb8["Z"] * -1

# Add tunnel to plot
fig.add_trace(go.Scatter3d(x=df_tunnel["X"],
                           y=df_tunnel["Y"],
                           z=df_tunnel["Z"],
                           mode='markers',
                           marker=dict(size=3, color='DarkSlateGrey'),
                           name="Tunnel"
                          )
             )

# add ST1 welltrak
fig.add_trace(go.Scatter3d(x=df_st1["X"],
                           y=df_st1["Y"],
                           z=df_st1["Z"],
                           mode='markers',
                           marker=dict(size=3, color='rgb(160, 160, 160)'),
                           name="ST1"
                          )
             )

# add ST2 welltrak
fig.add_trace(go.Scatter3d(x=df_st2["X"],
                           y=df_st2["Y"],
                           z=df_st2["Z"],
                           mode='markers',
                           marker=dict(size=3, color='rgb(160, 160, 160)'),
                           name="ST2"
                          )
             )

# add MB5 welltrak
fig.add_trace(go.Scatter3d(x=df_mb5["X"],
                           y=df_mb5["Y"],
                           z=df_mb5["Z"],
                           mode='markers',
                           marker=dict(size=3, color='rgb(160, 160, 160)'),
                           name="MB5"
                          )
             )

# add MB8 welltrak
fig.add_trace(go.Scatter3d(x=df_mb8["X"],
                           y=df_mb8["Y"],
                           z=df_mb8["Z"],
                           mode='markers',
                           marker=dict(size=3, color='rgb(160, 160, 160)'),
                           name="MB8"
                          )
             )

fig.show()