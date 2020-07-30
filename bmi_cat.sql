\connect fitness;

CREATE TABLE bmi_cat(
  BMI_category TEXT,
  low FLOAT,
  high FLOAT
  );

  \copy bmi_cat FROM 'data/bmi_cat.csv' DELIMITER ',' CSV HEADER;
