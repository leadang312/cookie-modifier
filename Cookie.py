import streamlit as st
import pandas as pd

st.header("🍪 Cookie Modify")
st.caption(" ")

# Uploading a csv file
file = st.file_uploader("Upload file")

if file:
    df = pd.read_csv(file)
    st.write("File successfully uploaded!")

    df = st.experimental_data_editor(df)

    # Downloading a csv file
    @st.cache_data
    def convert_df(df):
        return df.to_csv().encode('utf-8')

    csv = convert_df(df)  
    st.download_button("Download file",  data=csv, file_name='mod.csv', mime='text/csv')