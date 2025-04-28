# product_master to Snowflake (with enhancements)

from pyspark.sql.functions import col, when, lower

df = spark.read.csv("dbfs:/mnt/data/project2/data/product_master.csv", header=True, inferSchema=True)

# Merge of main + dev logic
df_transformed = df.dropDuplicates(["ProductID"]).withColumn("Price", when(col("Price") < 0, 0).otherwise(col("Price"))).withColumn("Category", lower(col("Category"))).withColumn("IsPremium", when(col("Price") > 1000, "Yes").otherwise("No")).withColumn("PriceBucket", when(col("Price") < 200, "Low")
                              .when(col("Price") < 700, "Medium").otherwise("High"))

# Write as Parquet to external stage
df_transformed.write.mode("overwrite").parquet("dbfs:/mnt/staged-data/product_master/")
