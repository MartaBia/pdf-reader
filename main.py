import pyttsx3  # module - text to speech coversion library
import PyPDF2  # Library - used to perform major tasks on PDF files


def read_pdf(pdf):
    pdf_reader = PyPDF2.PdfReader(open(pdf, 'rb'))
    speaker = pyttsx3.init()

    # Selecting female voice
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[1].id)

    text = ''
    for page_num in range(len(pdf_reader.pages)):
        page_text = pdf_reader.pages[page_num].extract_text()

        # Clean up te text
        page_text = page_text.strip().replace('\n', ' ')

        text += page_text

    print(text)
    # Save the audio file
    speaker.save_to_file(text, 'test.mp3')

    # speaker.say(clean_text)
    speaker.runAndWait()

    speaker.stop


read_pdf('cover_letter.pdf')
