# Capstone-Project-3
<h1>Dynamic Data Ingestion and Storage in HDFS with Automated Hive Integration<br/></h1>

**Problem Statement:** <br/> The task aims to fetch data from a specified link, store it in HDFS, and create a Hive table to visualize it. Initially, ensuring access to the provided link and successful data retrieval is essential. Subsequently, determining the data format and schema, if structured, is pivotal. Utilizing tools like wget or curl for data retrieval and HDFS CLI for storage follows. Finally, creating a Hive table, loading data, and verifying correctness conclude the task, with an optional script for automation.<br/>

**Technologies Used:** <br/> Python, API, HDFS, Hive, Shell scripting.<br/>

**Project Workflow:** <br/>Data retrieval from the specified link, storage in HDFS, and the creation of a Hive table for data visualization. Validation of data integrity within the Hive table ensures correctness.

**Task performed to complete the project:** <br/> **1. Data Retrieval (from URL) and Determine Data Format & Schema** - Tools: Use wget or curl to download the data.Once the data is retrieved, inspect it to determine the structure. If it's a CSV, TSV, or JSON, check the headers (schema) and data types.<br/>
**2. Store Data in HDFS** - Use HDFS CLI or Hadoop commands. Create an HDFS directory and upload the file. <br/>
**3. Hive Table Creation and Data Loading** - Define a schema for the data based on its format. Create a Hive table and Load the data into it. <br/>
**4. Verifying Data and Querying in Hive** - After the data is loaded, run Hive queries to ensure the data has been ingested correctly. <br/>


