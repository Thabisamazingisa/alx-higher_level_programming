-- List all records with score >= 10 in 'second_table' of db 'hbtn_0c_0'
-- Should display both score and name order by score
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
