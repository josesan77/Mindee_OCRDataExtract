# Mindee_OCRDataExtract
Python3 code samples for Mindee AI based OCR (API) services to extract data from pdf files 

PDF/image scraping/data extraction using AI based services of Mindee through API.
API services require a profile (user account, including username and API key).
Pricing: free below a certain amount of usage per month, see Mindee website for details!

A customized model based API was trained on 2x 50 PDF to get better results on finding the spot and 
extracting the text more precisely. Precision could be further increased by 
adding new documents for training, but the next step required some hundreds of new files.
Such amount was not available in this project.
After training, Mindee website offers application codes in the following languages: 
    - Python3
    - Node.js
    - Ruby
    - Java
    - .NET
    - PHP
    
Mindee website: https://www.mindee.com/
code created based on https://developers.mindee.com/docs/python-sdk

Pandas module: https://pandas.pydata.org/docs/index.html

Test case files: 
not added for the case of custom designed CAD file scratcher API model (due to confidentiality)
jpg sample file from Mindee website for invoice API
see forther information here: https://developers.mindee.com/docs/invoice-ocr?utm_source=sendgrid.com&utm_medium=email&utm_campaign=website#set-up-the-api

API builder https://platform.mindee.com/api-builder

https://developers.mindee.com/docs/python-invoice-ocr
