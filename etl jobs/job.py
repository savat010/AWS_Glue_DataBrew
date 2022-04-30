import sys
import json
import boto3

from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.dynamicframe import DynamicFrame
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql import functions as F
from pyspark.sql.types import *
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv,
                          ['input_path', 'output_bucket', 's3_output_key'])
print(args)

glueContext = GlueContext(SparkContext.getOrCreate())
spark = glueContext.spark_session

citibike_data = glueContext.create_dynamic_frame_from_options(
        connection_type = "s3", 
        connection_options = {"paths": [args['input_path']]}, 
        format = "csv",
        format_options={
            "withHeader" : True
        }
    )

citibike_agg = citibike_data.\
    toDF().\
    withColumn('starttime_ts',to_timestamp(col('starttime'))).\
    withColumn('stoptime_ts',to_timestamp(col('stoptime'))).\
    withColumn('tripduration',round((col("stoptime_ts").cast("long") - col('starttime_ts').cast("long"))/60))

output_path = f"s3://{args['output_bucket']}/{args['s3_output_key']}"
print(f"output_path: {output_path}")
citibike_agg.coalesce(1).write.mode("overwrite").parquet(output_path)