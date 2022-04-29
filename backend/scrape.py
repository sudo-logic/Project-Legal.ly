# Extract text from PDFs and run them through a NLP pipeline


import os
import numpy as np
import pandas as pd

# Download PDF from link
def download_pdf(url):
    """Download a PDF from a URL and save it to a file."""
    import urllib.request

    filename = url.split('/')[-1]
    if not os.path.exists(filename):
        urllib.request.urlretrieve(url, filename)



# Extract bold text from PDF
def extract_data(pdf_path):
    """Extract data from the PDF"""

    path = pdf_path[:-4] + '.csv'
    print(path)
    # check if pdfname.csv exists
    if os.path.exists(path):
        # read using pandas
        df = pd.read_csv(path)
        return df

    else:
        import re
        import pandas

        text = open('a.txt', 'r').read()

        topics = re.findall(r"\b(\d+)\.\s*([\w\d\s]+).—([\w\W]*?)(?=\d+.\s*[\w\d\s]+.—)", text)

        df = pandas.DataFrame(topics, columns=['topic', 'title', 'text'])

        df.to_csv(path, index=False)

        return df


download_pdf("https://legislative.gov.in/sites/default/files/A2015-22.pdf")

txt = extract_data("A2015-22.pdf")

print(txt)