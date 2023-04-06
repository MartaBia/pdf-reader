import pyttsx3  # module - text to speech coversion library
import PyPDF2  # Library - used to perform major tasks on PDF files


def read_pdf(pdf):
    pdf_reader = PyPDF2.PdfReader(open(pdf, 'rb'))
    speaker = pyttsx3.init()

    for page_num in range(len(pdf_reader.pages)):
        text = pdf_reader.pages[page_num].extract_text()
        clean_text = text.strip().replace('\n', ' ')
        print(clean_text)

    speaker.save_to_file(clean_text, 'pdf_audio.mp3')
    speaker.runAndWait

    speaker.stop


read_pdf('cover_letter.pdf')
