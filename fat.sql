
\connect fitness;

CREATE TABLE fat(
  category TEXT,
  gender TEXT,
  low FLOAT,
  high FLOAT
  );

  \copy fat FROM 'data/fat.csv' DELIMITER ',' CSV HEADER;
