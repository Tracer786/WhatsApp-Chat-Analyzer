import streamlit as st
import preprocessor
st.sidebar.title("WhatsApp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")  # code to convert to string data
    # st.text(data)  # this will print the data of the file
    df = preprocessor.preprocess(data)

    st.dataframe(df)  # to display the dataframe
# abhi ye file ek byte data ka stream hai
# hme ise string data me convert krna pdega

    # fetch unique users
    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")

    st.sidebar.selectbox("Show Analysis wrt",user_list)

    if st.sidebar.button("Show Analysis"):
        pass





