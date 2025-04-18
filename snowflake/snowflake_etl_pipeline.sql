-- Snowflake ELT Logic

MERGE INTO PROD_DB.DIM.PRODUCT_DIM t
USING (
  SELECT * FROM PROD_DB.RAW.PRODUCT_STAGE
) s
ON t.ProductID = s.ProductID
WHEN MATCHED THEN
  UPDATE SET t.ProductName = s.ProductName, t.Price = s.Price, t.Category = s.Category
WHEN NOT MATCHED THEN
  INSERT (ProductID, ProductName, Price, Category)
  VALUES (s.ProductID, s.ProductName, s.Price, s.Category);
