import numpy as np
import pandas as pd
import streamlit as st

st.title('ANOMALY DETECTION IN BLOCKCHAIN')
st.header('Description')
st.write('Anomaly detection has been popular research for a long time. Its applications in the financial sector have greatly aided in identifying suspicious activities of hackers. Despite the advancements in the financial sector such as blockchain and artificial intelligence, many cases of fraud still appear. ')
st.subheader('Bitcoin')
st.subheader('Problem')
st.write('This thesis aims to solve the binary classification problem to determine if a Bitcoin transaction is an anomalous transaction.')

st.header('Description')
data = pd.read_csv('streamlit/data/data.csv')
st.dataframe(data)