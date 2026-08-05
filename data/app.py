import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html, Input, Output

# Load and prepare data
df = pd.read_csv("processed_sales.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Initialize Dash app
app = dash.Dash(__name__)

# Layout with radio buttons + styling
app.layout = html.Div(
    style={"fontFamily": "Arial", "padding": "20px", "backgroundColor": "#f9f9f9"},
    children=[
        html.H1("Soul Foods Sales Visualiser",
                style={"textAlign": "center", "color": "#2c3e50"}),

        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
                {"label": "All", "value": "all"}
            ],
            value="all",
            inline=True,
            style={"margin": "20px", "fontSize": "18px"}
        ),

        dcc.Graph(id="sales-chart")
    ]
)

# Callback for interactive filtering
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="Sales",
        title=f"Pink Morsel Sales ({selected_region.capitalize()})",
        labels={"date": "Date", "Sales": "Sales"},
        template="plotly_white"
    )
    fig.update_traces(mode="lines+markers", line=dict(color="#3498db", width=2))
    return fig

if __name__ == "__main__":
    app.run(debug=True)
