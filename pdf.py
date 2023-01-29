from PyPDF2 import PdfReader
from PyPDF2 import PdfFileWriter
import streamlit as st

document = PdfReader(open('rr2885trc.pdf', 'rb'))


pdftext = ""

pageObj = document.pages[0]
pdftext += pageObj.extract_text().replace('\n', '')

st.write(pageObj)
