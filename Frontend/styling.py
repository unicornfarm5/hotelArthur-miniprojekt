# styling.py
import streamlit as st

def use_styling():
    st.markdown("""
        <style>
        .stApp {
            background-color: #f4efeb;
        }
        </style>
    """, unsafe_allow_html=True)
