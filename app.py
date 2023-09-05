import streamlit as st
import numpy as np
import pandas as pd  #import libraries
import time
import plotly.express as px


st.set_page_config(  # setup the webpage 
    page_title="Bank Data Management",
    page_icon=":bar_chart:",
    layout="wide"
)

#read the file

df=pd.read_csv("https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv")

st.dataframe(df)

#Sidebar

st.sidebar.header("Please Filter it here")
Job=st.sidebar.multiselect(
    "Select the job:",
    options=df["job"].unique(),
    default=df["job"].unique()
)

Loan=st.sidebar.multiselect(
    "Select the entries with loan:",
    options=df["loan"].unique(),
    default=df["loan"].unique()
)

Month=st.sidebar.multiselect(  # we filter the data on basis of month ,loan and job by pandas library
    "Select the entries with specific month",
    options=df["month"].unique(),
    default=df["month"].unique()
)


df['job']=='Job'
df['month']=='Month'
df['loan']=='Loan'









