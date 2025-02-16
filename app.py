import pandas as pd
from pathlib import Path
from dash import Dash, html, dcc
import plotly.express as px

from pink_morsel_processing import get_pink_morsel_data

# Retrieve pink morsel data and sum all sales on the same day
pink_morsel_df = get_pink_morsel_data()
graph_df = pink_morsel_df.groupby("date", as_index=False)["sales"].sum()

# Construct the Dash app
app = Dash()
app.layout = html.Div(children=[
    html.H1(children="Pink Morsel Sales"),
    dcc.Graph(
        id="pink-morsel-graph",
        figure=px.line(graph_df, x="date", y="sales")
    )
])

# Run the app
if __name__ == "__main__":
    app.run(debug=True)