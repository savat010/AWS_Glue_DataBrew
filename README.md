![1](https://user-images.githubusercontent.com/15683958/167124431-271bab41-1545-4421-b201-1b339e402c40.png)

## What is AWS Glue DataBrew?

AWS Glue DataBrew is a new visual data preparation tool that makes it easy for data analysts and data scientists to clean and normalize data to prepare it for analytics and machine learning. You can choose from over 250 pre-built transformations to automate data preparation tasks, all without the need to write any code. This reduces the time it takes to prepare data for analytics and ML by up to 80% compared to traditional approaches to data preparation.
 
You can automate filtering anomalies, converting data to standard formats, and correcting invalid values, and other tasks. After your data is ready, you can immediately use it for analytics and machine learning projects. Furthermore, you only pay for what you use - no upfront commitment.
 
Some of it's key features are:-
1. **Over 250 transformations**: Visualize, clean, and normalize data directly from your data lake, data warehouses, and database including Amazon S3, Amazon Redshift, Amazon Aurora, and Amazon RDS

2. **Evaluate data quality**: Evaluate the quality of your data by profiling it to understand data patterns and detect anomalies

3. **Visually map data lineage**: Visually map the lineage of your data to understand the various data sources and transformation steps that the data has been through

4. **Automate at scale**: Automate data cleaning and normalization tasks by applying saved transformation directly to new data as it comes into your source system

## Architecture overview
To demonstrate the solution, we prepare and transform the publicly available New Your Citi Bike trip data to analyze bike riding patterns. The dataset has the following attributes.

We use DataBrew to prepare and clean the most recent data and then use Step Functions for advanced transformation in AWS Glue ETL. For the DataBrew steps, we clean up the dataset and remove invalid trips where either the start time or stop time is missing, or the rider’s gender isn’t specified. After DataBrew prepares the data, we use AWS Glue ETL tasks to add a new column tripduration and populate it with values by subtracting starttime from endtime.

After we perform the ETL transforms and store the data in our Amazon Simple Storage Service (Amazon S3) target location, we use Amazon Athena to run interactive queries on the data to find the most used bikes to schedule maintenance, and the start stations with the most trips to make sure enough bikes are available at these stations. We also create an interactive dashboard using Amazon QuickSight to gain insights and visualize the data to compare trip count by different rider age groups and user type.

![4](https://user-images.githubusercontent.com/15683958/167124389-4c1dc462-9cba-4aa0-b502-6999593feeb4.png)

## Use Case 1: Enrich datasets for descriptive analytics with AWS Glue DataBrew

We will demonstrate how AWS Glue DataBrew can help businesses of all sizes to get started with data analytics with no prior coding knowledge. The architecture will use DataBrew for data preparation and transformation, Amazon Simple Storage Service (Amazon S3) as the storage layer of the entire data pipeline, and the AWS Glue Data Catalog for storing the dataset’s business and technical metadata. Alos, to gain the benefits of granular access control and easily visualize data from Amazon S3, we take the advantage of seamless integration between Amazon Athena and Amazon QuickSight. This provides a SQL interface to query all the information we need from the curated dataset stored on Amazon S3 without the need to create and maintain manifest files. And finally, we will construct an interactive dashboard with QuickSight to depict the final curated dataset alongside our critical KPIs.

**Tools**: AWS Glue DataBrew, Amazon QuickSight, AWS Glue, Amazon Athena, Amazon Simple Storage Service (Amazon S3).
![2](https://user-images.githubusercontent.com/15683958/167124345-74b2eb03-7136-4dd3-a9e6-0871418ea638.png)



## Use Case 2: Build a data quality scorecard using AWS Glue DataBrew, Amazon Athena, and Amazon QuickSight

We will demonstrate a solution by applying various business rules to determine the quality of incoming data and separate good and bad records to create a data quality scorecard using DataBrew, Athena queries, and QuickSight. This provides flexibility for any business to use this solution with their datasets and apply various business rules to build a complete data quality framework to monitor issues within their datasets.
 
Our architecture will utilize DataBrew for data preparation and building key KPIs, Amazon Athena for data analysis with standard SQL, and QuickSight for building the data quality scorecard.
 
**Tools**: AWS Glue DataBrew, Amazon Athena, Amazon Simple Storage Service (Amazon S3), Amazon QuickSight
DataBrew provides the ability to prepare and transform your dataset using over 250 transforms. In this section, we discuss some of the most commonly used transformations:
![5](https://user-images.githubusercontent.com/15683958/167124323-1d0d1c40-e1d6-43f8-9ce1-d7d5f13c3809.png)


## Some of the transformations you can do using DataVrew:
1. **Combine datasets** – You can combine datasets in the following ways:
2. **Join** – Combine several datasets by joining them with other datasets using a join type like inner join, outer join, or excluding join.
3. **Union operation** – Combine several datasets using a union operation. Multiple files for input datasets – While creating a dataset, you can use a parameterized Amazon S3 path or a dynamic parameter and select multiple files.
4. **Aggregate data** – You can aggregate the dataset using a group by clause and use standard and advanced aggregation functions like Sum, Count, Min, Max, mode, standard deviation, variance, skewness, kurtosis, as well as cumulative functions like cumulative sum and cumulative count.
5. **Pivot a dataset** – You can pivot the dataset in the following ways:
6. **Pivot operation** – Convert all rows to columns.
7. **Unpivot operation** – Convert all columns to rows.
8. **Transpose operation** – Convert all selected rows to columns and columns to rows.
9. **Unnest top level value** – You can extract values from arrays into rows and columns into rows. This only operates on top-level values.
10. **Outlier detection and handling** – This transformation works with outliers in your data and performs advanced transformations on them like flag outliers, rescale outliers, and replace or remover outliers. You can use several strategies like ZScore, modified Z-score, and interquartile range (IQR) to detect outliers.
11. **Delete duplicate values** – You can delete any row that is an exact match to an earlier row in the dataset.
12. **Handle or impute missing values** – You have the following options:
13. **Remove invalid records** – Delete an entire row if an invalid value is encountered in a column of that row.
14. **Replace missing values** – Replace missing values with custom values, most frequent value, last valid value, or numeric aggregate values.
15. **Filter data** – You can filter the dataset based on a custom condition, validity of a column, or missing values.
16. **Split or merge columns** – You can split a column into multiple columns based on a custom delimiter, or merge multiple columns into a single column.
17. **Create columns based on functions** – You can create new columns using different functions like mathematical functions, aggregated functions, date functions, text functions, windows functions like next and previous, and rolling aggregation functions like rolling sum, rolling count, and rolling mean.
