import streamlit as st 
import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

def preprocess_csv(df):
    local_df = df
    print("Entered Pre-Processing Stage")
    st.write("Please Wait we are Pre-Processing the data Frame")
    st.write("Writing size from another .py file :",local_df.size)
    st.write(local_df.columns)
    fig,axis = plt.subplots(figsize=(5,5))
    sns.countplot(x="Age_band_of_driver",data=local_df,hue="Age_band_of_driver")
    st.pyplot(fig)