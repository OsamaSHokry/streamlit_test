import streamlit as st
from Deploy import my_var
from Deplou import data


st.subheader("Home Page")
st.write(my_var)
st.write(data.head())


test_var = 'Test Var'
