# Mindee_OCRDataExtract
Python3 code samples for Mindee AI based OCR (API) services to extract data from pdf files 

PDF/image scraping/data extraction using AI based services of Mindee through API.
API services require a profile (user account, including username and API key).
Pricing: free below a certain amount of usage per month, see Mindee website for details!

**1) Simple code API usage: mindee_invoice.py **
Using the "off-the-shelf" invoice scraping API of Mindee, a simple python code is presented. This is a good start to use Mindee services. Details are given in the code or a short description here: https://d4e1.blogspot.com/2023/12/mindee-simple-invoice-data-extractor.html 

**2) A customized model based API: mindee_CADread_cycle.py** was trained on approximately 70 PDF to get better results on finding the spot and extracting the text precisely to be acceptable. Precision could be further increased by adding new documents for training. The next remarkable quality step would have required some hundreds of new files.
Such amount was not available in this project and also the targeted precision and reliability of the model was reached.

After training, Mindee website offers application codes in the following languages:

- Python3
- Node.js
- Ruby
- Java
- .NET
- PHP

# Further information, Links
Mindee website: https://www.mindee.com/
code created based on https://developers.mindee.com/docs/python-sdk

Pandas module: https://pandas.pydata.org/docs/index.html

**Test case files**

not added for the case of custom designed CAD file scratcher API model (due to confidentiality)

jpg and pdf sample file from Mindee website for invoice API (in test folder)
see forther information here: https://developers.mindee.com/docs/invoice-ocr?utm_source=sendgrid.com&utm_medium=email&utm_campaign=website#set-up-the-api

API builder https://platform.mindee.com/api-builder

https://developers.mindee.com/docs/python-invoice-ocr
