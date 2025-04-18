# Pull inventory data from Snowflake and write to Databricks Catalog

sf_options = {
    "sfURL": "your_account.snowflakecomputing.com",
    "sfDatabase": "PROD_DB",
    "sfSchema": "METRICS",
    "sfWarehouse": "COMPUTE_WH",
    "sfRole": "SYSADMIN",
    "sfUser": "nkv1408",
    "sfPassword": "xxxxx"
}

df_inventory = spark.read     .format("snowflake")     .options(**sf_options)     .option("dbtable", "INVENTORY_METRICS")     .load()

df_inventory.write     .format("delta")     .mode("overwrite")     .saveAsTable("main.analytics.inventory_metrics_silver")
