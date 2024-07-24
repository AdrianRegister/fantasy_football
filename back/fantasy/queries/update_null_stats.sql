-- SQLite
UPDATE fantasy_player
SET 
blocks = CASE WHEN blocks IS NULL THEN 0 ELSE blocks END,
dribblessuccess = CASE WHEN dribblessuccess IS NULL THEN 0 ELSE dribblessuccess END;
