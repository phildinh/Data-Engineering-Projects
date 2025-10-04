# Data Engineering Project 3: Pulling data by APIs using Microsoft Azure, transforming data in Data Bricks then connect to Power BI for reporting.

<img width="1612" height="1016" alt="image" src="https://github.com/user-attachments/assets/098c6fe2-62b9-41a6-aeb8-6bb1cd6077be" />

Environment: Microsoft Azure (Resources group, storage account, Data Factory, DataBricks, Microsoft Entra ID)
Summary: Create resource within Microsoft Azure to have environment for working, using Data Factory to create pipeline pull data via Apis then load to Data Lake for storing in Bronze Layer. Then using Data Bricks (pyspark) to transform data and store in Silver layer, then create SQL database on the top of datalake and load data from silver layer to SQL database in gold layer by delta. Next connect to power BI for reporting.

## Step by Step
### Create resources
narrative (chat gpt help me)
<img width="1912" height="605" alt="image" src="https://github.com/user-attachments/assets/84dbe20d-b737-4f8e-a34e-240298f52483" />

### Create pipeline in Azure data factory
#### create linked service to connect ...
narrative (Chat gpt help me)
<img width="1915" height="530" alt="image" src="https://github.com/user-attachments/assets/300f2b9f-6155-4570-be02-730e35b9fb78" />
#### create pipeline to pull data from request by HTTP
narrative (Chat gpt help me)
<img width="1914" height="608" alt="image" src="https://github.com/user-attachments/assets/dae2ace1-f02b-40aa-a278-1489ae74fe90" />

### Using databricks to transform data
#### check bronze layer
narrative (Chat gpt help me) dataloading beyon parquet format
<img width="1916" height="816" alt="image" src="https://github.com/user-attachments/assets/743e5b7d-1e10-4ae5-b9c7-3f2c6d924dbf" />
#### Creating connection allow databrick access to datastorage and work
narrative (Chat gpt help me) create conection from microsoft entra id and storeageaccount IAM access control
<img width="1914" height="728" alt="image" src="https://github.com/user-attachments/assets/1bb98655-196c-4d62-a514-716bc7391b58" />
<img width="1906" height="654" alt="image" src="https://github.com/user-attachments/assets/92a3b96b-0458-4228-ad6d-1552d4656e2f" />
#### Working within databrick environment
narrative (chat gpt help me) create compute for working
<img width="1907" height="828" alt="image" src="https://github.com/user-attachments/assets/e8b6d02d-6ff8-468c-9c11-031c523d143e" />
Look at silver layer script
look at gold layer script

### Create connection within databrick to powerbi
narrative (Chat GPT help me)
