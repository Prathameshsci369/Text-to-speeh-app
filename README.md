# Text-to-Speech Application

This is a simple Text-to-Speech (TTS) application built using Streamlit, gTTS, PyPDF2, python-docx, and pydub. 
The application allows users to upload PDF, DOCX, or TXT files, extract text from them, and convert the text to speech. 


## Features

- Upload PDF, DOCX, or TXT files and extract text from them.
- Customize the text area size.
- Convert the extracted text to speech using Google Text-to-Speech (gTTS).


## Installation

1. Clone the repository or download the `voice2.py` file.

2. Install the required dependencies using pip:

    
    pip install -r requirements.txt
    



## Usage

1. Run the Streamlit application:

   
    streamlit run voice2.py
    

2. Open your web browser and go to `http://localhost:8501`.

3. Upload a PDF, DOCX, or TXT file using the sidebar.

4. If uploading a PDF, specify the start and end pages for text extraction.

5. Customize the text area size using the slider.

6. Click the "Convert to Speech" button to generate the audio.

7. Download the audio in your preferred format using the provided download link.

## Dependencies

- streamlit
- gtts
- PyPDF2
- python-docx
- pydub





## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [gTTS](https://gtts.readthedocs.io/)
- [PyPDF2](https://pypdf2.readthedocs.io/)
- [python-docx](https://python-docx.readthedocs.io/)
- [pydub](https://pydub.com/)
- [ffmpeg](https://ffmpeg.org/)
