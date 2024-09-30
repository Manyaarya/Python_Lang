import streamlit as st
import pandas as pd
import numpy as np

## Title of the application
st.title("My First Streamlit App")

## Display a Simple text
st.write("Hello World!")

## Create a simple Dataframe

df = pd.DataFrame({
    'first column' : [1,2,3,4],
    'second column' : [10,20,30,40]
})

##Display the dataframe

st.write("Here is the dataframe")
st.write(df)

## Create a line chart
chart_data=pd.DataFrame(
    np.random.randn(20,3), columns=['a','b','c']
)
st.line_chart(chart_data)