import streamlit as st
import numpy as np
import pandas as pd
import time
import plotly.express as px


st.set_page_config(
    page_title="Bank Data Management",
    page_icon=":bar_chart:",
    layout="wide"
)

#read the file

df=pd.read_csv("https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv")

st.dataframe(df)





