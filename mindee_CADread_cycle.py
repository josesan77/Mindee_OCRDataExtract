# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 15:50:26 2023
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

Test case files: not available due to confidentiality of the content of the pdf files

Created on Mon Dec 11 15:50:26 2023
@author: josesan77

install package: 
pip install mindee
"""

from mindee import Client, PredictResponse, product # data extraction (OCR)
import pandas as pd # data collection and saving

def create_pd_DF():
    #function to create Pandas dataframe (df) to store and save data
    #predefine column names:
    colname_list = ['doc_ver', 'other', 'printDate', 'verDate', 'productCode', 'productName', 'productVer' ]
    df_CAD = pd.DataFrame(columns = colname_list)   
    return df_CAD, colname_list

def save_DF(df_CAD):
    #save gathered data stored in pandas dataframe -> given filepath (xlsx!)
    cad_filepath = 'FILEPATH_HERE'
    writer_CADinfo = pd.ExcelWriter(cad_filepath, engine='openpyxl') # engine='xlsxwriter')
    df_CAD.to_excel(writer_CADinfo, header= True) 
    # further excel write options: sheet_name='Work1', startrow= 0, startcol = 0, index=False 
    writer_CADinfo.close() # close file to release

# START -------------------------
# Init a new client
# receive API key and trained model ENDPOINT_NAME, USERNAME on Mindee website
mindee_client = Client(api_key='32CHARACTER_API_KEY_HERE')
custom_endpoint = mindee_client.create_endpoint("ENDPOINT_NAME", "USERNAME")

# Load a file from network
folderPath = 'FOLDER_PATH'
fileList = ['file1.PDF', 'file2.PDF'] #insert filenames here

df_CAD, colname_list = create_pd_DF()
rowindex = 0 #counter of file processed -> pandas datframe row number
for index, file in enumerate(fileList):
    full_path = folderPath + fileList[index] # os.path.join() may be used
    input_doc = mindee_client.source_from_path(full_path)

    # Load a file from disk and parse it.
    # The endpoint name must be specified since it cannot be determined from the class.
    result: PredictResponse = mindee_client.parse(product.CustomV1, input_doc, endpoint=custom_endpoint)
    
    # Print a brief summary of the parsed data - if needed
    print(result.document)
       
    # # Iterate over all the fields in the document
    index = 0
    for field_name, field_values in result.document.inference.prediction.fields.items():       
        if index == 2:
            print(field_name, "=", field_values)    
        df_CAD.at[rowindex, colname_list[index]] =\
            str(result.document.inference.prediction.fields[field_name])
        index += 1
    rowindex += 1
    
save_DF(df_CAD)
        
