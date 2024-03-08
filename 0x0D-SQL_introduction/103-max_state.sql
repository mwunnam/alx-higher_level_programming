-- Displyas the maximum tempeature of each state in Alphabetical order
SELECT `state`, MAX(`value`) AS max_temp
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;
