# app.py

from dash import Dash
from dash import dcc
from dash import html
import pandas as pd

data = pd.read_csv("avacado.csv")
data = data.query("type == 'conventional' and region == 'Albany'")
data = ["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="Avacado Analytics",),
        html.P(
            children="Analyze the behavior of avacado prices"
            " and the number of avacados sold in the US"
            " between 2015 and 2018",
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data ["Date"],
                        "y": data["AveragePrice"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Average Price of Avacados"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["Total Volume"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Avacados Sold"},
            },
        ),

    ]
)

