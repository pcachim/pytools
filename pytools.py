import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.title("PyTools v0.1")


pdftools = st.button("pdf Tools")
gpxtools = st.button("gpx kml Tools")
if pdftools:
    switch_page("pdf Tools")
if gpxtools:
    switch_page("gpx kml Tools")


