import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

my_var = " my variable says Hello"
data_0 = pd.read_csv("owid-covid-data.csv")

def main():
    st.title("Streamlit Muli-Page test")
    st.subheader("Main Page")
    st.write(my_var)
    st.write(data.head())

    choice = st.sidebar.selectbox("SubMenu",["Pandas","Tenserflow"])
    if choice == "Pandas":
        st.subheader("Pandas")

if __name__ == '__main__':
    main()
