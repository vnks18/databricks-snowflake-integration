# Pull inventory data from Snowflake and write to Databricks Catalog (with enhancements)

from pyspark.sql.functions import col, when, datediff, current_date

sf_options = {
    "sfURL": "your_account.snowflakecomputing.com",
    "sfDatabase": "PROD_DB",
    "sfSchema": "METRICS",
    "sfWarehouse": "COMPUTE_WH",
    "sfRole": "SYSADMIN",
    "sfUser": "your_user",
    "sfPassword": "your_password"
}

df_inventory = spark.read.format("snowflake").options(**sf_options).option("dbtable", "INVENTORY_METRICS").load()

# Merge logic
df_enhanced = df_inventory.withColumn("DaysSinceRestocked", datediff(current_date(), col("LastRestocked"))).withColumn("StockStatus", when(col("StockAvailable") < col("ReorderLevel"), "Low").otherwise("OK")).withColumn("ValueTier", when(col("InventoryValue") < 1000, "Low")
                             .when(col("InventoryValue") < 3000, "Medium")
                             .otherwise("High"))

# Write to Unity Catalog - Silver layer
df_enhanced.write.format("delta").mode("overwrite").saveAsTable("main.analytics.inventory_metrics_silver")
