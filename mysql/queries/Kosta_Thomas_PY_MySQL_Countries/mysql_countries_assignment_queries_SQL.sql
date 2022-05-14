-- #1
SELECT country.name, countrylanguage.Language, countrylanguage.Percentage 
FROM countrylanguage
LEFT JOIN country ON countrylanguage.CountryCode = country.code
WHERE countrylanguage.Language = 'Slovene'
ORDER BY countrylanguage.Percentage DESC;

-- #2
SELECT country.name, COUNT(*) AS cities 
FROM country
LEFT JOIN city ON country.code = city.CountryCode
GROUP BY country.name
ORDER BY cities DESC;

-- #3
SELECT city.name, city.Population
FROM country
LEFT JOIN city ON country.code = city.CountryCode
-- By country.code or country.name. Assignment did not specify
-- where country.code = 'MEX' and city.Population > 500000
WHERE country.name = 'Mexico' AND city.Population > 500000
ORDER BY city.Population DESC;

-- #4
SELECT country.name, countrylanguage.Language, countrylanguage.Percentage 
FROM countrylanguage
LEFT JOIN country ON countrylanguage.CountryCode = country.code
WHERE countrylanguage.Percentage > 89
ORDER BY countrylanguage.Percentage DESC;

-- #5
SELECT name, SurfaceArea, Population
FROM country
WHERE SurfaceArea < 501 AND Population > 100000
ORDER BY name ASC;

-- #6
SELECT name, GovernmentForm, Capital, LifeExpectancy
FROM country
WHERE GovernmentForm = 'Constitutional Monarchy' AND Capital > 200 AND LifeExpectancy > 75;

-- #7
SELECT country.Name, city.Name, city.District, city.Population
FROM country
JOIN city ON country.Code = city.CountryCode
WHERE country.Name = 'Argentina' AND city.District = 'Buenos Aires' AND city.Population > 500000;

-- #8
SELECT Region, COUNT(*) AS countries
FROM country
GROUP BY Region
ORDER BY countries DESC;