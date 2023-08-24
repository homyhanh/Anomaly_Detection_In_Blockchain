import streamlit as st

option_method = st.radio(
    "What\'s your choice?",
    ('Without handling imbalanced data method', 'Cost-sensitive learning', 'Resampling'))

if option_method == 'Without handling imbalanced data method':
    col1,col2=st.columns(2)
    with col1:
        st.image("https://github.com/homyhanh/Anomaly_Detection_In_Blockchain/assets/79818022/6aee06e4-a5d3-4a6e-a490-6578bb1809b9", use_column_width='always')
    with col2:
        st.image("https://github.com/homyhanh/Anomaly_Detection_In_Blockchain/assets/79818022/ecbeb94e-ddd0-4ceb-98b1-163cca377a76", use_column_width='always')
    st.write('\n')
    col3,col4=st.columns(2)
    
    with col3:
        st.image("https://github.com/homyhanh/Anomaly_Detection_In_Blockchain/assets/79818022/e7e5571d-e296-4df8-aa0b-178570f0b846", use_column_width='always')
    
    with col4:
        st.image("https://github.com/homyhanh/Anomaly_Detection_In_Blockchain/assets/79818022/4fb5f5ce-ea8e-4e9f-a8a7-a5770f346c7a", use_column_width=True)

    
        
    st.write('All three supervised models can not predict the anomalous class. Since the machine learning algorithm tries to optimize the loss, it quickly realizes that, if so many targets are normal transactions, the outputs should most likely be normal transactions to achieve a great result. And therefore, it comes up with the same prediction at all times.')
    st.write('Besides, KMeans is ')
elif option_method == 'Cost-sensitive learning':
    col1,col2, col3 =st.columns(3)
    with col1:
        st.image("https://github.com/homyhanh/Anomaly_Detection_In_Blockchain/assets/79818022/a28e9bf5-8ec8-4f86-b2c8-a97188fe3591", use_column_width='always')
    with col2:
        st.image("https://github.com/homyhanh/Anomaly_Detection_In_Blockchain/assets/79818022/c99c0268-8381-4998-bdb3-f49cf356b585", use_column_width='always')

    with col3:
        st.image("https://github.com/homyhanh/Anomaly_Detection_In_Blockchain/assets/79818022/c0f45851-7ac9-4ff6-95f7-832a2a87e086", use_column_width='always')

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
        