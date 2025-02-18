from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily
import streamlit as st 
st.title("Meteo Bologna")

# Set time period
start = datetime(2019, 1, 1)
end = datetime(2025, 1, 21) # fa una settimana di forecasting

cities = {'Andria':[41.2311700,16.2979700]}


# Create Point for Vancouver, BC
city = Point(list(cities.values())[0][0],list(cities.values())[0][1], 20)

# Get daily data for 2018
data = Daily(city, start, end)
data = data.fetch()
data
import plotly.express as px
import pandas as pd

# Create the base figure with the first line
fig = px.line(data,
              x=data.index,
              y='tavg',
              title="Titolo",
              width=1500,
              height=700)

# Add the second line
fig.add_scatter(x=data.index,
                y=data['tmax'],
                name="Predicted",
                line_color='#ff8c00')

# Update the first trace's properties
fig.data[0].update(name="Actual",
                   line_color='#0000FF')

# Update axis labels
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales"
)

# Add rangeslider and range selector
fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(count=2, label="3y", step="year", stepmode="backward"),
            dict(count=3, label="5y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
st.title("temperature")

st.plotly_chart(fig)





