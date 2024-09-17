import streamlit as st
from gtts import gTTS
from io import BytesIO
import PyPDF2  # PyPDF2 for PDF text extraction
import docx

# Function to extract text from PDF
def extract_text_from_pdf(file, start_page=0, end_page=None):
    reader = PyPDF2.PdfReader(file)
    text = ""
    end_page = end_page or len(reader.pages)
    for page_num in range(start_page, end_page):
        page = reader.pages[page_num]
        text += page.extract_text()
    return text

# Function to extract text from DOCX
def extract_text_from_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

# Streamlit UI
st.title("Text-to-Speech Application")
st.sidebar.header("Text-to-Speech Settings")

# Language selection
language = st.sidebar.selectbox("Select language:", [
    'en', 'hi', 'mr', 'ta', 'te', 'bn', 'gu', 'pa', 'kn', 'ml', 'ur', 'as', 'or'
])

# File upload
uploaded_file = st.sidebar.file_uploader("Upload a PDF, DOCX, or TXT file:", type=["pdf", "docx", "txt"])

# Custom page extraction for PDFs
start_page = 0
end_page = 0
if uploaded_file and uploaded_file.type == "application/pdf":
    start_page = st.sidebar.number_input("Start Page", min_value=0, value=0)
    end_page = st.sidebar.number_input("End Page", min_value=0, value=0)

# Extract text from uploaded file
text_input = ""
if uploaded_file:
    if uploaded_file.type == "application/pdf":
        text_input = extract_text_from_pdf(uploaded_file, start_page, end_page if end_page > 0 else None)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        text_input = extract_text_from_docx(uploaded_file)
    elif uploaded_file.type == "text/plain":
        text_input = uploaded_file.read().decode("utf-8")

# Input text with customizable size
text_area_height = st.sidebar.slider("Text Area Height (px)", min_value=100, max_value=800, value=300)
text_input = st.text_area("Enter text to convert to speech:", value=text_input, height=text_area_height)

# Convert text to speech
if st.button("Convert to Speech"):
    if text_input:
        tts = gTTS(text=text_input, lang=language, slow=False)
        audio_buffer = BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)
        
        # Provide a download link
        st.audio(audio_buffer, format="audio/mp3")
        st.download_button(
            label="Download Audio",
            data=audio_buffer,
            file_name="converted_audio.mp3",
            mime="audio/mp3"
        )