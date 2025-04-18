-- Snowflake

CREATE TABLE PROD_DB.RAW.PRODUCT_STAGE (
    ProductID INT,
    ProductName STRING,
    Category STRING,
    Price DOUBLE
);

CREATE TABLE PROD_DB.DIM.PRODUCT_DIM (
    ProductID INT,
    ProductName STRING,
    Category STRING,
    Price DOUBLE
);

-- Databricks

CREATE TABLE raw.analytics.product_master_raw (
    ProductID INT,
    ProductName STRING,
    Category STRING,
    Price DOUBLE
)
USING DELTA;

CREATE TABLE main.analytics.inventory_metrics_silver (
    ProductID INT,
    StockAvailable INT,
    ReorderLevel INT,
    LastRestocked DATE
)
USING DELTA;
