import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="Anomaly Detection In Blockchain",
    page_icon=":coin:",
)

st.write("# Anomaly Detection In Blockchain")
st.sidebar.success("Select a page above")

st.header('Introduction')
st.subheader('Bitcoin')
st.image('https://github.com/homyhanh/Anomaly_Detection_In_Blockchain/assets/79818022/f7f20a8f-66a8-4dc6-bd02-bc320725e12b')
st.write('Bitcoin is a cryptocurrency, which is used and distributed electronically. Bitcoin is also a decentralized and peer-to-peer (P2P) system. Bitcoin serves a public ledger for all transactions of the network and is capable of representing currency digitally so working as electronic cash.')
st.write('One of the key characteristics of Bitcoin is anonymity. So this type of transaction is one of the methods used by drug criminals, terrorists or money launderers')
st.subheader('Anomaly Detection')
st.image('https://sdcastillo.github.io/assets/css/anomaly_detection/bitcoin_app_screenshot.PNG')
st.write('Anomaly detection has been popular research for a long time. Its applications in the financial sector have greatly aided in identifying suspicious activities of hackers. Despite the advancements in the financial sector such as blockchain and artificial intelligence, many cases of fraud still appear. This thesis aims to solve the binary classification problem to determine if a Bitcoin transaction is an anomalous transaction.')

st.subheader('Datasets')
st.image('https://github.com/homyhanh/Anomaly_Detection_In_Blockchain/assets/79818022/fe8a97cd-3b29-407a-a7a9-08a2130f7b6b')
st.write('The Bitcoin transaction network metadata dataset is published in the master thesis “Anomaly detection in blockchain” by Shafiq, Omer. Raw data from bitcoin blockchain are used to generate this dataset. The dataset used is bitcoin blockchain data from 2011 to 2013.')
st.write('The dataset consists of 30248134 samples and 13 features.')
st.write(pd.read_csv('C:/Users/hanhm/Anomaly_Detection_In_Blockchain/streamlit/data/data_original.csv'))

st.header('Method')
method = '''The problem-solving methods used are:

- Techniques for handling imbalanced data including Cost-sensitive learning, Resampling.
- Models to train and classify transactions including Logistic Regression (LR), DecisionTree (DT), Stochastic Gradient Descent (SGD), Multi-layer Perceptron (MLP) will be compared and evaluated.'''

st.write(method)