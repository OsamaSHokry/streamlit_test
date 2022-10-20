import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px
my_var = " my variable says Hello"

def main():
    st.title("Streamlit Muli-Page")
    st.subheader("Main Page")
    st.write(my_var)

    choice = st.sidebar.selectbox("SubMenu",["Pandas","Tenserflow"])
    if choice == "Pandas":
        st.subheader("Pandas")

if __name__ == '__main__':
    main()
