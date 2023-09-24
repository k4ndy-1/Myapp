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

#KPI or key performance indicator

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


st.dataframe(df_selection)

# Page 2 - Display high probability of defaulting entries
st.title("High Probability of Defaulting Entries")
st.markdown("##")

# Calculate the 'mean_to_median_ratio' and add it to the DataFrame
if 'balance' in df_selection.columns:
    df_selection['mean_to_median_ratio'] = df_selection['balance'] / df_selection['balance'].median()

# Define the calculate_default_probability function
def calculate_default_probability(row, mean_threshold, median_threshold, mean_to_median_ratio_threshold):
    # Calculate the probability of defaulting based on criteria
    probability = 0  # Initialize probability
    if 'balance' in row.index:
        if row['balance'] < mean_threshold:
            probability += 0.3
        if row['balance'] < median_threshold:
            probability += 0.3
    if 'mean_to_median_ratio' in row.index and row['mean_to_median_ratio'] > mean_to_median_ratio_threshold:
        probability += 0.4

    return probability

# Define threshold values
mean_threshold = 1000  # Adjust as needed
median_threshold = 800  # Adjust as needed
mean_to_median_ratio_threshold = 1.5  # Adjust as needed

# Calculate the probability of defaulting for each entry
df_selection['default_probability'] = df_selection.apply(lambda row: calculate_default_probability(row, mean_threshold, median_threshold, mean_to_median_ratio_threshold), axis=1)

# Filter entries with a high probability of defaulting (> 0.90)
high_default_prob_entries = df_selection[df_selection['default_probability'] > 0.90]

# Display the filtered entries
for index, row in high_default_prob_entries.iterrows():
    st.subheader(f"Entry {index + 1}")
    st.write(f"Job: {row['job']}")
    st.write(f"Loan: {row['loan']}")
    st.write(f"Month: {row['month']}")
    st.write(f"Balance: INR {row['balance']:,}")
    st.write(f"Age: {row['age']}")
    st.write(f"Default Probability: {row['default_probability']:.2f}")
    st.markdown("---")  # Add a divider between entries












