import streamlit as st

#Presentation
st.title(":blue[Dynamic Data Ingestion and Storage in HDFS with Automated Hive Integration]")
st.header(":rainbow[Problem Statement]")
st.markdown("The task aims to fetch data from a specified link, store it in HDFS, and create a Hive table to visualize the data. Initially, ensuring access to the provided link and successful data retrieval is essential. Subsequently, determining the data format and schema, if structured, is pivotal. Utilizing tools like wget or curl for data retrieval and HDFS CLI for storage follows. Finally, creating a Hive table, loading data, and verifying correctness conclude the task, with an optional script for automation.")    
st.subheader(":orange[Technologies Used:]")
st.markdown("Python, API, HDFS, Hive, Shell scripting")    
st.subheader(":orange[Project Workflow:]")
st.markdown("Data retrieval from the specified link, storage in HDFS, and the creation of a Hive table for data visualization. Validation of data integrity within the Hive table ensures correctness.")   
st.subheader(":orange[Task performed to complete the project:]")
st.markdown("""
- **:green[Data Retrieval (from URL) and Determine Data Format & Schema]** - Use wget or curl to download the data.Once the data is retrieved, inspect it to determine the structure. If it's a CSV, TSV, or JSON, check the headers (schema) and data types.
- **:green[Store Data in HDFS]** - Use HDFS CLI or Hadoop commands. Create an HDFS directory and upload the file.
Ensure the table structure supports efficient querying of trending hashtags.
- **:green[Hive Table Creation and Data Loading]** - Define a schema for the data based on its format. Create a Hive table and Load the data into it.
- **:green[Verifying Data and Querying in Hive]** - After the data is loaded, run Hive queries to ensure the data has been ingested correctly.                                               
""")   
st.subheader(":orange[Task performed in Hadoop and Hive Environment:]")
st.markdown("""
**:red[1.Data Retrieval (from the given URL)]** \n
:green[code:] curl https://www2.census.gov/programs-surveys/popest/datasets/2020-2023/cities/totals/sub-est2023_32.csv \n
**:red[2.To save the fetched data from the URL in the linux terminal called data.csv file]** \n
:green[code:] cat > data.csv \n
**:red[3.Create directory in hadoop and copy the saved file(Data.csv) from terminal to HDFS]** \n
:green[code:] hdfs dfs -mkdir /me32p3 \n
hdfs dfs -put data.csv /me32p3/ \n
**:red[4.Create new database in Hive Environment]** \n
:green[code:] create database if not exists :orange[ME32]; \n     
**:red[5.Create new table within newly created database]** \n
:green[code:] CREATE TABLE :orange[census] (SUMLEV INT,STATE INT,COUNTY INT,PLACE INT,COUSUB INT,CONCIT INT,PRIMGEO_FLAG INT,FUNCSTAT STRING,NAME STRING,STNAME STRING,ESTIMATESBASE2020 INT,POPESTIMATE2020 INT,POPESTIMATE2021 INT,POPESTIMATE2022 INT,POPESTIMATE2023 INT)ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE; \n                                                        
**:red[6.Load data into table]** \n
:green[code:] load data inpath :orange['/me32p3/data.csv'] into table :orange[census]; \n
INSERT INTO TABLE :orange[census] values(040,32,000,00000,00000,00000,0,'A','Nevada','Nevada',3104617,311584
0,3146632,3177421,3194176); \n  
**:red[7.Query the table]** \n
:green[code:] Select * from :orange[census]; \n              
""") 
