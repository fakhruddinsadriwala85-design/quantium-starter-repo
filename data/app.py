import dash
from dash import html

app = dash.Dash(__name__)
app.layout = html.Div("Setup Successful!")

if __name__ == "__main__":
    app.run(debug=True)
