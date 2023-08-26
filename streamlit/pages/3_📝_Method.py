import streamlit as st

st.header('Visualize confusion matrix')
option_method = st.radio(
    "What\'s your choice?",
    ('Without handling imbalanced data method', 'Cost-sensitive learning', 'Resampling'))

if option_method == 'Without handling imbalanced data method':
    col1,col2=st.columns(2)
    with col1:
        st.image("https://github.com/homyhanh/Anomaly_Detection_In_Blockchain/assets/79818022/6aee06e4-a5d3-4a6e-a490-6578bb1809b9", use_column_width='always')
    with col2:
        st.image("https://github.com/homyhanh/Anomaly_Detection_In_Blockchain/assets/79818022/7986cd76-4545-4a44-8f41-5f2871fb9347", use_column_width='always')
    st.write('\n')
    col3,col4=st.columns(2)
    
    with col3:
        st.image("https://github.com/homyhanh/Anomaly_Detection_In_Blockchain/assets/79818022/1508b63a-8cef-42d8-ad69-eae8690320d8", use_column_width='always')
    
    with col4:
        st.image("https://github.com/homyhanh/Anomaly_Detection_In_Blockchain/assets/79818022/6fc2722b-e66e-4180-b468-b56169725551", use_column_width=True)

    
        
    st.write('All models can not predict the anomalous class. Since the machine learning algorithm tries to optimize the loss, it quickly realizes that, if so many targets are normal transactions, the outputs should most likely be normal transactions to achieve a great result. And therefore, it comes up with the same prediction at all times.')
elif option_method == 'Cost-sensitive learning':
    col1,col2 =st.columns(2)
    with col1:
        st.image("https://github.com/homyhanh/Anomaly_Detection_In_Blockchain/assets/79818022/a28e9bf5-8ec8-4f86-b2c8-a97188fe3591", use_column_width='always')
    with col2:
        st.image("https://github.com/homyhanh/Anomaly_Detection_In_Blockchain/assets/79818022/c99c0268-8381-4998-bdb3-f49cf356b585", use_column_width='always')
    col3 = st.columns(1)
    
    st.image("https://github.com/homyhanh/Anomaly_Detection_In_Blockchain/assets/79818022/c0f45851-7ac9-4ff6-95f7-832a2a87e086", width=350)
    st.write('Using cost-sensitive learning give result better than not handling imbalanced data. All models tend to predict outliers instead of normal transitions at all times. Linear regression and SGD work well when predicting a lot of anomalous transactions correctly (26/30 and 27/30).')
else:
    col1,col2=st.columns(2)
    with col1:
        st.image("https://github.com/homyhanh/Anomaly_Detection_In_Blockchain/assets/79818022/b030461c-6016-48fc-a1d4-92021a8134a5", use_column_width='always')

    with col2:
        st.image("https://github.com/homyhanh/Anomaly_Detection_In_Blockchain/assets/79818022/785a1152-ccf5-4ca7-8783-5e767ab81e43", use_column_width='always')
    st.write('\n')
    col3,col4=st.columns(2)
    with col3:
        st.image("https://github.com/homyhanh/Anomaly_Detection_In_Blockchain/assets/79818022/81b8fecf-5e3f-47db-a6e6-5e8864799d65", use_column_width=True)

    with col4:
        st.image("https://github.com/homyhanh/Anomaly_Detection_In_Blockchain/assets/79818022/29446137-7a34-40c9-8014-5a3cb3240e35", use_column_width='always')
        
    st.write('Like cost-sensitive learning, applying resampling also helps the model avoid predicting all transactions is normal. Furthermore, the false positive increase to millions to predict a few anomalous transactions. That leads to reduce evaluation metrics.  However, using resampling is better than training without handling imbalanced data.  ')