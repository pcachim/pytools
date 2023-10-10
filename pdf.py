import streamlit as st
import PyPDF2

st.title("PDF Viewer")

# Allow the user to upload a PDF file
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Read the contents of the PDF file
    pdf_reader = PyPDF2.PdfFileReader(uploaded_file)
    num_pages = pdf_reader.getNumPages()
    page_number = st.number_input("Enter a page number (1 - {})".format(num_pages), min_value=1, max_value=num_pages, value=1)
    page = pdf_reader.getPage(page_number - 1)
    text = page.extractText()

    # Display the contents of the selected page
    st.write(text)
