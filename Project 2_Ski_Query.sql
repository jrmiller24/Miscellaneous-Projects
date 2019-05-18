-- Query to check successful load
SELECT * FROM snowfall_df;

SELECT * FROM visits_df;

-- Join tables on Resort_Name
select *
from snowfall_df as s
join visits_df as v
ON s.Resort_Name = v.Resort_Name;
