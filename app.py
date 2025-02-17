import dash
import pandas as pd
from pathlib import Path
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

from pink_morsel_processing import get_pink_morsel_data

APP_COLORS = {
    "text": "#e8f2f2",
    "background": "#060a0a",
    "primary": "#9fcac6",
    "secondary": "#4e3764",
    "accent": "#b579ae",
}

# Retrieve pink morsel data and sum all sales on the same day
pink_morsel_df = get_pink_morsel_data()

def filter_pink_morsel_sales(region):
    filtered_df = pink_morsel_df
    if region != "all":
        filtered_df = filtered_df[filtered_df["region"] == region]
    return filtered_df.groupby("date", as_index=False)["sales"].sum()

def create_pink_morsel_graph(df):
    graph_fig = px.line(df, x="date", y="sales")
    graph_fig.update_layout({
        "paper_bgcolor": APP_COLORS["background"],
        "plot_bgcolor": APP_COLORS["background"],
        "font": {
            "color": APP_COLORS["text"]
        }
    })
    graph_fig.update_traces(
        line={
            "color": APP_COLORS["accent"]
        }
    )
    return graph_fig

# Create the app
app = Dash()

# Create the visible components
pink_morsel_graph = dcc.Graph(id="pink-morsel-graph")
region_filter = dcc.RadioItems(
    id="region-filter",

    value="all",
    options=[
        {"label": "North", "value": "north"},
        {"label": "East", "value": "east"},
        {"label": "South", "value": "south"},
        {"label": "West", "value": "west"},
        {"label": "All", "value": "all"},
    ],

    inline=True,
    style={
        "color": APP_COLORS["text"],
        "backgroundColor": APP_COLORS["secondary"],
        "padding": "10px 0",  # Add some padding for better alignment
        "borderRadius": "5px",  # Smooth the corners
        "fontWeight": "bold",  # Make text stand out more
        "fontSize": "16px",  # Slightly increase text size for better readability
        "width": "100%",  # Make it span the full width
        "display": "flex",
        "justifyContent": "space-around",  # Even spacing for the items
        "alignItems": "center"
    },
    labelStyle={
        "display": "inline-block",
        "padding": "8px 15px",  # More padding for clickable space
        "margin": "0 10px",  # Space between the items
        "borderRadius": "25px",  # Rounded item buttons
        "cursor": "pointer",  # Pointer cursor on hover
        "transition": "all 0.3s ease",  # Smooth transition on hover
    },
    inputStyle={
        "display": "none",  # Hide the default radio button circle
    },
)

# Add callback for region selection
@app.callback(
    Output("pink-morsel-graph", "figure"),
    Input("region-filter", "value")
)
def update_graph_region(region):
    return create_pink_morsel_graph(
        filter_pink_morsel_sales(region)
    )

# Define the layout of the app
app.layout = html.Div(
    children=[
        html.H1(
            children="Pink Morsel Sales",
            style={
                "textAlign": "center",
                "color": APP_COLORS["text"]
            }
        ),
        region_filter,
        pink_morsel_graph
    ],
    style={
        "backgroundColor": APP_COLORS["background"],
        "height": "100vh"
    }
)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)