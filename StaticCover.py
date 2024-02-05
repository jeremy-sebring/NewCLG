from JobInput import getRole, Title, Company

from PyPDF2 import PdfReader
from pathlib import Path
import shutil


# Input Resume Path
inputResume = Path("inputs/")






'''
Start with you Cover header 
Name
Number
Email

Then the body, Use {Title}, {company}, and {Role}. 

The Values are set in job input

'''
html_template = '''
<Name>
<email>
<Link to site> 

lorem ipsum {Title}
{Company}
{Role}

'''

# format the template with the variables
formatted_template = html_template.format(
    Title=Title,
    Company=Company,
    Role= getRole()
    )



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
