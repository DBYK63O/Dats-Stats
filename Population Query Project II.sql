SELECT *
FROM countries
LIMIT 5;

SELECT COUNT(*)
FROM countries
WHERE continent = "Africa";

SELECT ROUND(SUM(population), 2) as "Total_Population", continent
FROM population_years
LEFT JOIN countries ON countries.id = population_years.country_id 
GROUP BY 2
ORDER BY 1 DESC;

SELECT ROUND(SUM(population), 2) as "Total_Population", continent
FROM population_years
LEFT JOIN countries ON countries.id = population_years.country_id
WHERE year = 2010 
GROUP BY 2
ORDER BY 1 DESC;

SELECT ROUND(SUM(population), 2) FROM population_years
LEFT JOIN countries ON countries.id = population_years.country_id
WHERE continent = "Oceania" AND year = 2000;

SELECT ROUND(AVG(population), 2) AS "Average Population in (millions)" FROM population_years
LEFT JOIN countries ON countries.id = population_years.country_id
WHERE year = 2003
AND continent = "South America";

SELECT name, ROUND(MIN(population), 5) AS "Smallest population" FROM population_years
INNER JOIN countries ON
countries.id = population_years.country_id
WHERE year = 2007;

SELECT ROUND(AVG(population), 2) AS "Poland's Avg pop in 2000's"
FROM population_years
INNER JOIN countries ON
countries.id = population_years.country_id
WHERE name = "Poland";

SELECT name
FROM countries
WHERE name LIKE "%The%";


SELECT ROUND(SUM(population), 2) AS "Continental population (milllions), 2010", continent
FROM population_years
INNER JOIN countries ON
countries.id = population_years.country_id
WHERE year = 2010
GROUP BY 2
ORDER BY 1 DESC;