# PYTHON
This folder contains all python-files whose objective is to create data tables based on the downloaded rawdata. The objective can be achieved by executing the **main.py** file.
 
## Extract & Transform Data
Each table has been created as dataframe in individual python-files:
- Extraction and Transformation of raw data in the [rawtables](https://github.com/frkroe/DataProject1/tree/main/python/rawtables) folder:
    - client data
    - products data
    - influencers data
- Creation of missing data in the [newtables](https://github.com/frkroe/DataProject1/tree/main/python/newtables) folder:
    - composition data
    - sales data
    - data relating compositions with products

## Export Data as csv
The dataframes have been exported as csv-files which can be found in the (with python created) [results](https://github.com/frkroe/DataProject1/tree/main/python/results) folder.

## Fill tables in POSTGRES
This folder contains the python-file (*alimentar_tablas.py*) whose objective is to fill the SQL data tables in postgres with the data that have been extracted and transformed in the previously explained folders before.