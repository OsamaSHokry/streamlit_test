import streamlit as st
from Deploy import my_var
from Deploy import data_0

st.subheader("Home Page")
st.write(my_var)
st.write(data_0.head())

test_var = 'Test Var'
