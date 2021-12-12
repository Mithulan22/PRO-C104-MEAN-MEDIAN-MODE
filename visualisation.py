import pandas as pd 
import csv
import plotly.graph_objects as go 
df = pd.read_csv("reader.csv")
student_df = df.loc[df["student_id"]== "TRL_987"]
print(student_df("level")["attempt"].mean())
fig = go.Figure(go.Bar(
        x = student_df.groupby("level")["attempt"].mean(),
        y = ["level 1", "level 2", "level 3", "level 4"],orintation = "h"
))
fig.show()