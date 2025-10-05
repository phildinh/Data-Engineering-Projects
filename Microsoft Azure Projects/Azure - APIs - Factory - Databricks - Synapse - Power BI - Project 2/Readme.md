# Azure project, copy dataset via HTTP from Github in Data Factory, then create connection and transform data in Databricks, following 3 layers bronze, silver and gold. THen load data to data warehouse (Synapse Analytics) and connect to power bi for reporting

## Creating pipeline in Data Factory to pull data from Github
- Use json to store all HTTP related to file's link. The pipeline is look up the json file within folder in datastorage (HTTP create as parameter folder to store dynamic files)
<img width="966" height="698" alt="image" src="https://github.com/user-attachments/assets/82050fbf-da90-4599-a144-9047a4ac6247" />

- Use loop to go through all http link and copy csv file to bronze folder
<img width="660" height="289" alt="image" src="https://github.com/user-attachments/assets/2cb99a2c-a885-406d-8d14-6039a16160c2" />

