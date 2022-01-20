import pyttsx3
import PyPDF2
ebook = open('AI.pdf', 'rb')
pdfreader = PyPDF2.PdfFileReader(ebook)
pages = pdfreader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(6, pages):
    page = pdfreader.getPage(6)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
