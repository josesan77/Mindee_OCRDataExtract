# -*- coding: utf-8 -*-
"""
PDF scraping/data extraction using AI based services of Mindee through API.
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
jpg and pdf sample file from Mindee website for invoice API (in test folder)
see forther information here: https://developers.mindee.com/docs/invoice-ocr?utm_source=sendgrid.com&utm_medium=email&utm_campaign=website#set-up-the-api
    https://files.readme.io/a74eaa5-c8e283b-sample_invoice.jpeg

API builder https://platform.mindee.com/api-builder

https://developers.mindee.com/docs/python-invoice-ocr

@author: josesan77
Created on Sat Dec 2 11:58:18 2023
"""

from mindee import Client, PredictResponse, product

# Init a new client
mindee_client = Client(api_key= "18761de7672ca8e48625b4aeb7dd0349") #"my-api-key")

# Load a file from disk
input_doc = mindee_client.source_from_path('D:\\Jozsi\\datasci\\default_sample.jpg')

# Load a file from disk and parse it.
# The endpoint name must be specified since it cannot be determined from the class.
result: PredictResponse = mindee_client.parse(product.InvoiceV4, input_doc)

# Print a summary of the API result
print(result.document)

# Print the document-level summary
print(result.document.inference.prediction)