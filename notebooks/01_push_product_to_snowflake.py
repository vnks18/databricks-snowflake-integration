# PySpark script to push data to Snowflake via external stage

df = spark.read.csv("dbfs:/mnt/data/project2/data/product_master.csv", header=True, inferSchema=True)

# Clean-up & transformation
df_clean = df.dropDuplicates(["ProductID"])     .withColumn("Price", when(col("Price") < 0, 0).otherwise(col("Price")))

# Write as Parquet to external stage
df_clean.write     .mode("overwrite")     .parquet("dbfs:/mnt/staged-data/product_master/")  # Synced to Snowflake external stage
