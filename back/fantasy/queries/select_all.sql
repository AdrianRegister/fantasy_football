-- SQLite
SELECT id, playerid, name, firstname, lastname, age, birthdate, nationality, height, injured, photo, teamid, teamname, teamlogo, leagueseason, g_apps, g_starts, g_minutes, g_position, g_rating, shotstotal, shotsontarget, goals, goalsconceded, savesmade, assists, passestotal, passeskey, tackles, blocks, interceptions, duelstotal, duelswon, dribblesattempted, dribblessuccess, foulsagainst, foulscommitted, cardsyellow, cardsred, cardsyellowred, penaltieswon, penaltiesconceded, penaltiesscored, penaltiesmissed, penaltiessaved, weight
FROM fantasy_player
WHERE name IS 'K. De Bruyne';