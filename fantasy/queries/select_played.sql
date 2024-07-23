-- SQLite
SELECT *
FROM fantasy_player
WHERE g_minutes NOTNULL 
AND g_minutes <> '0'
ORDER BY goals DESC;