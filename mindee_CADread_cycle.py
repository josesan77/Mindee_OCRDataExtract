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
from os import startfile

def create_pd_DF():
    #function to create Pandas dataframe (df) to store and save data
    #predefine column names, the latter three are for predefined values 
    # and must be positioned at the end not to be overwritten by extracted values:
    colname_list = ['doc_ver', 'other', 'printDate', 'verDate', 'productCode',\
                    'productName', 'productVer', 'itemcode', 'originalName', 'filepath' ]
    df_CAD = pd.DataFrame(columns = colname_list)   
    return df_CAD, colname_list

def save_DF(df_CAD):
    #save gathered data stored in pandas dataframe -> given filepath (xlsx!)
    cad_filepath = 'FILEPATH_HERE'
    writer_CADinfo = pd.ExcelWriter(cad_filepath, engine='openpyxl') # other option engine='xlsxwriter')
    df_CAD.to_excel(writer_CADinfo, header= True) 
    # further excel write options: sheet_name='Work1', startrow= 0, startcol = 0, index=False 
    writer_CADinfo.close() # close file to release
    print('Data has been saved to ' + cad_filepath)
    startfile(cad_filepath) #open the xlsx by default viewer (if there is any installed)

# START ------------------------------------------------------------------
# Init a new client
# receive API key and trained model ENDPOINT_NAME, USERNAME on Mindee website
mindee_client = Client(api_key='32CHARACTER_API_KEY_HERE')
custom_endpoint = mindee_client.create_endpoint("ENDPOINT_NAME", "USERNAME")

# It is important to match the element number of the following lists! Order is important!
itemcode_list = [ "itemcode1", "itemcode2" ] #insert known names in order
itemNames = [ "itemname1", "itemname2"]     #insert itemnames in order 
fileList = ['PATH1/file1.pdf', 'PATH2/file2.pdf'] #insert full filepaths in order

df_CAD, colname_list = create_pd_DF()
rowindex = 0 #counter of file processed -> pandas datframe row number
for index, file in enumerate(fileList):
    print('Processing: ' + itemcode_list[index])
    full_path =  fileList[index]
    df_CAD.at[rowindex,'itemcode'] = itemcode_list[index]
    df_CAD.at[rowindex,'path'] = full_path
    df_CAD.at[rowindex,'originalName'] = itemNames[index]

    try:                        #to avoid loss of extraction due to wrong file(path) 
        input_doc = mindee_client.source_from_path(full_path)
        # Load a file from disk and parse it.
        # The endpoint name must be specified since it cannot be determined from the class.
        result: PredictResponse = mindee_client.parse(product.CustomV1, input_doc, endpoint=custom_endpoint)
        
        # Print a brief summary of the parsed data - if needed
        print(result.document)
           
        # # Iterate over all the fields in the document
        index = 0
        for field_name, field_values in result.document.inference.prediction.fields.items():
            #to avoid overwriting with second page empty predicted values, insert data only in empty case
            if df_CAD.iloc[rowindex].isnull()[colname_list[index]]: 
                df_CAD.at[rowindex, colname_list[index]] =\
                    str(result.document.inference.prediction.fields[field_name])
                index += 1
        
        #to limit processed files (keeping the 250 free pages limit in mind)
        #recommended steps of 20
        if rowindex > 1 and not rowindex%20:
            print('Processing end #' + str(rowindex))
            break
    except:
        df_CAD.at[rowindex,'docver'] = 'FILE NOT FOUND ERROR'
    rowindex += 1
    
save_DF(df_CAD)
        
