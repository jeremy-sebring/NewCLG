
Company = ""
Title = ""

#Not Needed if not using ChatGPT
description = """
"""


jobDesc = """
Company: {company}
Title: {title}

{description}
"""

def getJD():
    return jobDesc.format(company=Company,title=Title, description=description)

def getRole():
    return "{} at {}".format(Title, Company)