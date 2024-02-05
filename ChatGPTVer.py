from JobInput import getJD, getRole

from PyPDF2 import PdfReader
from pathlib import Path
import openai
import shutil


inputResume = Path("inputs/JSebringEng23.pdf")
openai.api_key = ""
  

pdfText = ""


# creating a pdf reader object
pdfReader = PdfReader(inputResume)

# creating a page object
pageObj = pdfReader.pages[0]

for page in pdfReader.pages:
    pdfText = pdfText + page.extract_text()


jobDescription = '''

'''    

prompt = """

Hi name is Jeremy Sebring!

This is my resume extracted from a PDF: 

{resume}


I'd like a cover letter for this job:

{job}

Can you generate one for me? 



"""

formatted_prompt = prompt.format(resume=pdfText, job=getJD())


messages = [ {"role": "system", "content": 
              "You are a intelligent career assistant."}, 
            {"role": "user", "content": formatted_prompt } ]


chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

reply = chat.choices[0].message.content




# define HTML template with placeholders for the variables
html_template = '''
Jeremy Sebring
(217) 851-2660
jeremy@sebringair.com

{CoverLetter}
'''

# format the template with the variables
formatted_template = html_template.format(CoverLetter=reply)



pdf_file = 'output.pdf'

# options for the PDF conversion
options = {
    'page-size': 'A4',
    'margin-top': '1cm',
    'margin-right': '1cm',
    'margin-bottom': '1cm',
    'margin-left': '1cm'
}

pathtext ="output/"+ getRole()
out = Path(pathtext)
out.mkdir(parents=True, exist_ok=True)

filename = getRole() + " Cover Letter.txt"
pdf_file = out / Path(filename)

with open(pdf_file, "w") as f: 
    f.write(formatted_template)


shutil.copy(inputResume, out)
