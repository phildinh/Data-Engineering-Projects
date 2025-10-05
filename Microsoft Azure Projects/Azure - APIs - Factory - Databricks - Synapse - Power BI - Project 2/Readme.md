# Azure project, Pull dataset by APIS in Azure Factory then store in storage account follwing 3 layers (Bronze, Silver and Gold in Datawarehouse). Then use Databricks to transform and store data from bronze to silver layer. Create access for databricks and synapse analytics (data warehouse) to access datalake (storage account). Create view in datawarehouse for gold layer and connect to power bi.

<img width="1790" height="1003" alt="image" src="https://github.com/user-attachments/assets/7a79b56b-bbb0-4dad-9a3d-099d2a93ff5c" />


## Create environment for project
- Create Resources, storageaccount, azure factory, databricks, synapse analytics, access link to allow azure factory and synapse analytics to acess datalake (Storage account).
<img width="1890" height="643" alt="image" src="https://github.com/user-attachments/assets/4965f7f0-8023-4414-b42c-bec07328f01b" />

## Creating pipeline in Data Factory to pull data from Github
- Use json to store all HTTP related to file's link. The pipeline is look up the json file within folder in datastorage (HTTP create as parameter folder to store dynamic files)
<img width="966" height="698" alt="image" src="https://github.com/user-attachments/assets/82050fbf-da90-4599-a144-9047a4ac6247" />

- Use loop to go through all http link and copy csv file to bronze folder
<img width="660" height="289" alt="image" src="https://github.com/user-attachments/assets/2cb99a2c-a885-406d-8d14-6039a16160c2" />

## Using Databricks to transform data and store to silver layer
- Create access link by microsoft entra id
- Create compute cluster to get worker node
- Use Pyspark to transform and store data (silver_layer.jpny)

<img width="1869" height="771" alt="image" src="https://github.com/user-attachments/assets/7cae3d02-c585-49b9-8482-828efd7917a0" />

## Using synapse Analytics to create SQL database, view for gold layer and connect to power bi
- Use Synapse analytics to create SQL database and store view for gold layer (Create View.sql)

<img width="1430" height="702" alt="image" src="https://github.com/user-attachments/assets/34828276-cb49-4325-a6ab-f9ecb7380611" />

- Connect to Power BI to make a report

<img width="1351" height="736" alt="image" src="https://github.com/user-attachments/assets/8d431e37-4eff-43da-9898-1fe5b81022c8" />
