-- Snowflake Snowpipe and Stage Setup

CREATE STAGE prod_stage
  URL='s3://your-bucket/staged-data/'
  STORAGE_INTEGRATION = your_s3_integration;

CREATE FILE FORMAT csv_format
  TYPE = 'CSV'
  FIELD_OPTIONALLY_ENCLOSED_BY = '"'
  SKIP_HEADER = 1;

CREATE OR REPLACE PIPE prod_pipe
  AUTO_INGEST = TRUE
  AS
  COPY INTO PROD_DB.RAW.PRODUCT_STAGE
  FROM @prod_stage
  FILE_FORMAT = csv_format;
