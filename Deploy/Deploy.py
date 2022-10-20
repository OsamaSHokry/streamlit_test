import streamlit as st
import pandas as pd
import numpy as np

my_var = " my variable says Hello"

def main():
    st.title("Streamlit Muli-Page")
    st.subheader("Main Page")
    st.write(my_var)
    
if __name__ == '__main__':
    main()
