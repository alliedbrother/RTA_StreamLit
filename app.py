import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import sklearn
from process_csv_file import preprocess_csv

st.set_page_config(page_title="Accident Severity Prediction App",
                   page_icon="🚧", layout="wide")

#creating option list for dropdown menu
options_day = ['Sunday', "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
options_age = ['18-30', '31-50', 'Over 51', 'Unknown', 'Under 18']

def main():
    with st.form('prediction_form'):

        st.subheader("Enter the input for following features:")
        
        hour = st.slider("Pickup Hour: ", 0, 23, value=0, format="%d")
        day_of_week = st.selectbox("Select Day of the Week: ", options=options_day)
        driver_age = st.selectbox("Select Driver Age: ", options=options_age)
        submit = st.form_submit_button("Predict")

    if submit:
        st.write(f"{hour} {day_of_week} {driver_age}")


    data_file = st.file_uploader("Upload the csv file",type=["csv"])
    
    if data_file is not None:
        #st.write(type(data_file))
        df = pd.read_csv(data_file)
        st.markdown("<h2 style='text-align: center;'>Your uploaded file looks as follows</h2>"
                    , unsafe_allow_html=True)
        st.dataframe(df[0:10])
        preprocess_csv(df)
        


if __name__ == '__main__':
    main()