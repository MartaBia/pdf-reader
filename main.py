import pyttsx3  # module - text to speech coversion library
import PyPDF2  # Library - used to perform major tasks on PDF files


def read_pdf(pdf):
    pdf_reader = PyPDF2.PdfFileReader(open(pdf, 'rb'))
    speaker = pyttsx3.init()

    for page_num in range(pdf_reader.numPages):
        text = pdf_reader.getPage(page_num).extractText()
        clean_text = text.strip().replace('\n', ' ')
        print(clean_text)

    speaker.save_to_file(clean_text, 'pdf_audio.mp3')
    speaker.runAndWait

    speaker.stop


read_pdf('file.pdf')
