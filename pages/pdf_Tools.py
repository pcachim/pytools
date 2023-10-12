import streamlit as st
import pypdf
import os
from io import BytesIO
from pathlib import Path
from pypdf import PdfReader, PdfWriter


def reduce_file_size(input_path):
    reader = PdfReader(input_path)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.add_metadata(reader.metadata)

    output = BytesIO()
    writer.write(output)
    writer.close()
    return output


def merge_pdfs(*input_files, list_input_files = []):
    pdf_writer = PdfWriter()
    
    for path in input_files:
        # print(f"Added: {path}")
        pdf_writer.append(path)

    for path in list_input_files:
        # print(f"Added: {path}")
        pdf_writer.append(path)

    output = BytesIO()
    pdf_writer.write(output)
    pdf_writer.close()
    return output


def remove_images(input_path, output_path):
    reader = PdfReader(input_path)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.remove_images()

    with open(output_path, "wb") as f:
        writer.write(f)


def reduce_image_quality(input_path, output_path, quality=80):
    reader = PdfReader(input_path)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    for page in writer.pages:
        for img in page.images:
            img.replace(img.image, quality)

    with open(output_path, "wb") as f:
        writer.write(f)
        


st.title("PDF Tools")

# Allow the user to upload a PDF file
uploaded_file = st.file_uploader("Choose input PDF file (s)", type="pdf", accept_multiple_files=True)
filename = st.text_input("Output filename", value="")

# Write in two columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("Merge PDF files")
    mergepdf_button = st.button("Merge PDF files")

    if mergepdf_button and len(uploaded_file) > 1:
        # Generate the PDF
        pdf_file = merge_pdfs(*uploaded_file)
        if filename == "":
            filename = "merged"

        # Provide a download button for the PDF
        st.download_button(
            label="Download merged PDF",
            data=pdf_file,
            key="pdf_download",
            on_click=None,
            args=None,
            file_name=filename + ".pdf"
        )


with col2:
    st.subheader("Reduce file size")
    reducepdf_button = st.button("Reduce size")

    if reducepdf_button and len(uploaded_file) > 0:
        # Generate the PDF
        pdf_file = reduce_file_size(*uploaded_file)
        path = Path(uploaded_file[0].name)
        if filename == "":
            filename = path.stem + "_reduced"

        # Provide a download button for the PDF
        st.download_button(
            label="Download merged PDF",
            data=pdf_file,
            key="pdf_download",
            on_click=None,
            args=None,
            file_name=filename + ".pdf"
        )
