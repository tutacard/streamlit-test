import pandas as pd
import altair as alt
import streamlit as st  


st.title("My title")

"# Markdown title"


"*format*"

car_url = "https://raw.githubusercontent.com/altair-viz/vega_datasets/master/vega_datasets/_data/cars.json"
cars = pd.read_json(car_url)

cars

y_axis_options = ["Acceleration", "Miles_per_Gallon", "Displacement"]
y_axis_select = st.selectbox(label="Select y", options=y_axis_options)

hp_mpg=alt.Chart(cars).mark_circle(size=80, opacity=0.6).encode(
	x='Horsepower:Q',
	y=y_axis_select,
	color='Origin'
)

hp_mpg

st.sidebar.title("Sidebar title")

st.sidebar.write("stuff")

