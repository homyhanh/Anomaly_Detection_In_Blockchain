import streamlit as st
import pandas as pd

st.header('Visualize evaluation metrics')
option_result = st.radio(
    "What\'s your choice?",
    ('Without handling imbalanced data method', 'Cost-sensitive learning', 'Resampling'))
if option_result == 'Without handling imbalanced data method':
    df_without_method= {
    'accuracy': [0.9999950410165783, 0.9999915697281833, 0.9999950410165783, 0.9999950410165783],
    'balanced_accuracy': [0.5, 0.49999826434719535, 0.5, 0.5],
    'macro_precision': [0.49999752050828916, 0.4999975204996821, 0.49999752050828916, 0.49999752050828916],
    'macro_recall': [0.5, 0.49999826434719535, 0.5, 0.5],
    'macro_f1': [0.49999876025107065, 0.49999789242316206, 0.49999876025107065, 0.49999876025107065],
    'time_to_train': [71.00356984138489, 272.9703857898712, 41.757519483566284, 1151.973237991333],
    'time_to_test': [0.16847920417785645, 0.3677794933319092, 0.10965180397033691, 5.395903587341309]
    }
    
    st.dataframe(pd.DataFrame(df_without_method, index = ['LR_original', 'DT_original', 'SGD_original','MLP_original']).style.format({"E": "{:.6f}"}))
    st.image('https://github.com/homyhanh/Anomaly_Detection_In_Blockchain/assets/79818022/ac7bcf46-e0d7-470d-90f3-a089ca1665f2')
elif option_result == 'Cost-sensitive learning':
    df_with_cost_sensitive= {
    'accuracy': [0.863451911993913, 0.9995155073197075, 0.8720982301884067],
    'balanced_accuracy': [0.8650592813592928, 0.4997602319625588, 0.8860490459116532],
    'macro_precision': [0.8650592813592928, 0.4997602319625588, 0.8860490459116532],
    'macro_recall': [0.8650592813592928, 0.4997602319625588, 0.8860490459116532],
    'macro_f1': [0.463392824397565, 0.49987884748117256, 0.46587472431914567],
    'time_to_train': [179.57120084762573, 386.8996367454529, 326.85084891319275], 
    'time_to_test': [0.47850704193115234, 0.9061334133148193, 0.3892531394958496]
}
    
    st.dataframe(pd.DataFrame(df_with_cost_sensitive, index = ['LR_cost-sensitive', 'DT_cost-sensitive', 'SGD_cost-sensitive']).style.format({"E": "{:.3f}"}))
    st.image('https://github.com/homyhanh/Anomaly_Detection_In_Blockchain/assets/79818022/0885fc09-b307-4ffc-ab6f-6f242f9008a0')
elif option_result == 'Resampling':
    df_with_resampling= {
    'accuracy': [0.8340712576163787, 0.46848723070033904, 0.8635360494126332, 0.7473943434859703],
    'balanced_accuracy': [0.8003691292714761, 0.4842435372141318, 0.7817684301946064, 0.6903641212243834],
    'macro_precision': [0.5000107625572853, 0.4999996862109603, 0.5000118571170682, 0.5000050001291034],
    'macro_recall': [0.8003691292714761, 0.4842435372141318, 0.7817684301946064, 0.6903641212243834],
    'macro_f1': [0.4547876381154346, 0.3190311593100342, 0.4634110494353418, 0.427731506263604],
    'time_to_train': [77.78949475288391, 606.819638967514, 29.48581600189209, 7722.717522144318], 
    'time_to_test': [0.11585426330566406, 1.0158424377441406, 0.10912299156188965, 6.7545390129089355]
}
    
    st.dataframe(pd.DataFrame(df_with_resampling, index = ['LR_resampling', 'DT_resampling', 'SGD_resampling','MLP_resampling']).style.format({"E": "{:.3f}"}))
    st.image('https://github.com/homyhanh/Anomaly_Detection_In_Blockchain/assets/79818022/fb68f8e6-4a31-4b2e-9b69-7ed4867cce37')
