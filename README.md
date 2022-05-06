## What is AWS Glue DataBrew?

AWS Glue DataBrew is a new visual data preparation tool that makes it easy for data analysts and data scientists to clean and normalize data to prepare it for analytics and machine learning. You can choose from over 250 pre-built transformations to automate data preparation tasks, all without the need to write any code. This reduces the time it takes to prepare data for analytics and ML by up to 80% compared to traditional approaches to data preparation.
 
You can automate filtering anomalies, converting data to standard formats, and correcting invalid values, and other tasks. After your data is ready, you can immediately use it for analytics and machine learning projects. Furthermore, you only pay for what you use - no upfront commitment.
 

## Use Case 1: Enrich datasets for descriptive analytics with AWS Glue DataBrew

We will demonstrate how AWS Glue DataBrew can help businesses of all sizes to get started with data analytics with no prior coding knowledge. The architecture will use DataBrew for data preparation and transformation, Amazon Simple Storage Service (Amazon S3) as the storage layer of the entire data pipeline, and the AWS Glue Data Catalog for storing the dataset’s business and technical metadata. Alos, to gain the benefits of granular access control and easily visualize data from Amazon S3, we take the advantage of seamless integration between Amazon Athena and Amazon QuickSight. This provides a SQL interface to query all the information we need from the curated dataset stored on Amazon S3 without the need to create and maintain manifest files. And finally, we will construct an interactive dashboard with QuickSight to depict the final curated dataset alongside our critical KPIs.

**Tools**: AWS Glue DataBrew, Amazon QuickSight, AWS Glue, Amazon Athena, Amazon Simple Storage Service (Amazon S3).

## Use Case 2: Build a data quality scorecard using AWS Glue DataBrew, Amazon Athena, and Amazon QuickSight

We will demonstrate a solution by applying various business rules to determine the quality of incoming data and separate good and bad records to create a data quality scorecard using DataBrew, Athena queries, and QuickSight. This provides flexibility for any business to use this solution with their datasets and apply various business rules to build a complete data quality framework to monitor issues within their datasets.
 
Our architecture will utilize DataBrew for data preparation and building key KPIs, Amazon Athena for data analysis with standard SQL, and QuickSight for building the data quality scorecard.
 
**Tools**: AWS Glue DataBrew, Amazon Athena, Amazon Simple Storage Service (Amazon S3), Amazon QuickSight
