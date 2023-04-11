import pyttsx3  # module - text to speech coversion library
import PyPDF2  # Library - used to perform major tasks on PDF files


def read_pdf(pdf):
    pdf_reader = PyPDF2.PdfReader(open(pdf, 'rb'))
    speaker = pyttsx3.init()

    # Selecting different voices
    # voices = speaker.getProperty('voices')
    # speaker.setProperty('voice', voices[1].id)

    # Changing the rate
    rate = speaker.getProperty('rate')
    speaker.setProperty('rate', 175)

    text = ''
    for page_num in range(len(pdf_reader.pages)):
        page_text = pdf_reader.pages[page_num].extract_text()

        text += page_text

    # Clean up te text
    clean_text = text.strip().replace('\n', ' ')

    speaker.say(clean_text)
    speaker.runAndWait()
    speaker.stop


pdf = input('Please, insert the pdf title and press enter:\n')
read_pdf(pdf)
