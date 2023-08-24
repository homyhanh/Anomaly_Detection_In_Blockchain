import streamlit as st
import pandas as pd

option = st.radio(
    "What\'s your option?",
    ('Remove unnecessary attributes', 'Analyze and normalize data'))

if option == 'Remove unnecessary attributes':
    st.write(pd.read_csv('C:/Users/hanhm/Anomaly_Detection_In_Blockchain/streamlit/data/data.csv'))
else:
    st.image('https://github.com/homyhanh/Anomaly_Detection_In_Blockchain/assets/79818022/af2fa59d-cd46-40ab-8e1c-8000c564d93d')
    st.caption('<div style="text-align: center;"><i>Figure 1. Bitcoin transaction data distribution chart</i></div>', unsafe_allow_html=True)
    st.write('\n')
    st.write('The class distribution of the dataset is highly imbalanced with 30,248,026 non-malicious data points and only 108 malicious transactions, make malicious transactions to be only approximately 0.00035% of whole data. ')
    unstranformed_data = pd.read_csv('C:/Users/hanhm/Anomaly_Detection_In_Blockchain/streamlit/data/untransformed_data.csv')
    unstranformed_data.index = ['count', 'mean', 'std','min', '25%', '50%', '75%', 'max']
    st.write(unstranformed_data)
    st.caption('<div style="text-align: center;"><i>Table 1. Untransformed data statistics.</i></div>', unsafe_allow_html=True)
    st.write('\n')
    st.image('https://github.com/homyhanh/Anomaly_Detection_In_Blockchain/assets/79818022/1dc9a309-df00-4cc2-822b-40da900e0593')
    st.caption('<div style="text-align: center;"><i>Figure 2. A frequency histogram of the extracted bitcoin transactional data representing distribution of malicious and non-malicious transactions in the dataset</i></div>', unsafe_allow_html=True)
    st.write('\n')
    st.write('We can see in Figure 2 that the original dataset distribute unevenly, the values ​​of the attributes are mainly concentrated on the left of the chart. All variables of the data highly follow a right-skewed distribution. This skewness of data can cause difficulty in the modeling process.')
    st.write('To reduce the right-skewness of the data, log function transformation seems to have a positive effect on the data. However, according to the table 5.1, our data contains of zero values, and standard log transformation cannot be applied to it. Therefore, a log(x+1) transformation was applied along with "Robust Scaler" transformation. ')
    st.image('https://github.com/homyhanh/Anomaly_Detection_In_Blockchain/assets/79818022/986b40bf-e89f-47a1-8829-03671d11f224')
    st.caption('<div style="text-align: center;"><i>Figure 2. Frequency distribution histograms of the transformed data.</i></div>', unsafe_allow_html=True)
    st.write('\n')
    st.write('After the normalization and standardization transformations have been applied, the features of the data are observed to be less skewed than before. ')