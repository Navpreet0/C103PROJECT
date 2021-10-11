import pandas as pd
import plotly.express as px

sg = pd.read_csv("Covid.csv")

fig = px.scatter(sg, x = "date", y = "cases", color="country")
fig.show()
