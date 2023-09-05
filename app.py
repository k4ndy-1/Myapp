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

df_selection=df.query(
    "job==@Job & loan==@Loan & month==@Month"
)

# ######MAINPAGE#########

st.title("💰Bank Retrieval Information💰")
st.markdown("##")

#KPI

left_col,mid_col,right_col=st.columns(3)

mean_balance=int(df_selection["balance"].mean())
median_balance=int(df_selection["balance"].median())
mean_to_med=round((mean_balance/median_balance),2)

with left_col:
    st.subheader("Mean Balance")
    st.subheader(f"INR {mean_balance:,}")
    

with mid_col:
    st.subheader("Median Balance")
    st.subheader(f"INR {median_balance:,}")
with right_col:
    st.subheader("Mean to Median Ratio")
    st.subheader(f"INR {mean_to_med:,}")

st.markdown("---") # divider


#bar chart job by balance

job_by_bal_line=(
    df.groupby(by=["job"]).sum()[["balance"]].sort_values(by="balance")
)

job_bal_chart= px.bar(
    job_by_bal_line,
    x="balance",
    y=job_by_bal_line.index,
    orientation="h",
    title="<b>Job & Balance Interrelation </b>",
    color_discrete_sequence=["#0083B8"] * len(job_by_bal_line),
    template="plotly_white",
)

job_bal_chart.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


st.plotly_chart(job_bal_chart)

#Job to duration chart

job_by_dur=df.groupby(by=["job"]).sum()[["duration"]].sort_values(by="duration")
job_dur_chart=px.density_heatmap(
    data_frame=job_by_dur,
    y="duration",
    x=job_by_dur.index,
    title="<b>Job & Duration of Loan Interrelation </b>",
)

st.plotly_chart(job_dur_chart)


st.dataframe(df)

#Hide Streamlit Styles

hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """

st.markdown(hide_st_style, unsafe_allow_html=True)












