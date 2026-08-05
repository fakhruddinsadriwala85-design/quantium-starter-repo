import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html

df = pd.read_csv("processed_sales.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

fig = px.line(
    df,
    x="date",
    y="Sales",
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "Sales": "Sales"},
    template="plotly_white"
)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Sales Visualiser"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)
