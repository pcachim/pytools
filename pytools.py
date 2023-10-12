import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.title("PyTools v0.1")


want_to_contribute = st.button("pdf Tools")
if want_to_contribute:
    switch_page("pdf Tools")


