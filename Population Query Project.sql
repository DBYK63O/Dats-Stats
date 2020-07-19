Select *
FROM population_years
LIMIT 5;

SELECT DISTINCT year
FROM population_years;

SELECT MAX(population)
FROM population_years
WHERE country = "Gabon";

SELECT country FROM population_years
WHERE year = 2005
ORDER BY population ASC
LIMIT 10;

SELECT DISTINCT country, population
FROM population_years
WHERE population > 100 AND year = 2010
GROUP BY 1
ORDER BY 2 DESC;

SELECT DISTINCT country
FROM population_years
Where country LIKE '%Islands%';

SELECT country, population
FROM population_years
WHERE country = "Indonesia" AND year = 2000 
OR country = "Indonesia" AND year = 2010
GROUP BY 2
ORDER BY 2;
