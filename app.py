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

#Sidebar

st.sidebar.header("Please Filter it here")
job=st.sidebar.multiset(
    "Select the job:",
    options=df["job"].unique(),
    default=df["job"].unique()
)

loan=st.sidebar.multiset(
    "Select the entries with loan:",
    options=df["loan"].unique(),
    default=df["loan"].unique()
)

month=st.sidebar.multiset(
    "Select the entries with specific month",
    options=df["month"].unique(),
    default=df["month"].unique()
)





