-- Exercises

-- Find the movie with a row id of 6 
SELECT * FROM movies
WHERE id = 6;

-- 
SELECT * FROM movies
WHERE Year BETWEEN 2000 AND 2010;

-- Opposite
SELECT * FROM movies
WHERE Year NOT BETWEEN 2000 AND 2010;

-- Get the top 5 movies
SELECT * FROM movies
LIMIT 5;

--
SELECT * FROM movies
WHERE title like "Toy Story%"

-- Find all the movies directed by John Lasseter
SELECT * FROM movies
WHERE director = "John Lasseter";

-- Find all the movies (and director) not directed by John Lasseter

SELECT * FROM movies
WHERE director != "John Lasseter";

-- Find all the WALL-* movies

SELECT * FROM movies
WHERE title LIKE "WALL-%";

-- TASK 3

-- List all directors of Pixar movies (alphabetically), without duplicates
SELECT DISTINCT directors FROM movies
ORDER BY director ASC;

-- List the last four Pixar movies released (ordered from most recent to least)
SELECT * FROM movies
ORDER BY year DESC
LIMIT 4

-- List the first five Pixar movies sorted alphabetically
SELECT * FROM movies
ORDER BY title ASC
LIMIT 5;

-- List the next five Pixar movies sorted alphabetically
SELECT * FROM movies
ORDER BY title ASC
LIMIT 5 OFFSET 5;

-- TASK 4
-- Longitude values increase as you go to east -> vertical direction from north to south
-- latitude values increases as you go to north -> horizontal direction from west to east

-- List all the Canadian cities and their populations
SELECT city, population FROM north_american_cities
WHERE country = 'Canada'

-- Order all the cities in the United States by their latitude from north to south
SELECT * FROM north_american_cities
WHERE country = 'United States'
ORDER BY latitude DESC

-- List all the cities west of Chicago, ordered from west to east
-- decrease in longitude
SELECT city
FROM north_american_cities
WHERE longitude < (SELECT longitude FROM north_american_cities WHERE city = "Chicago" )
ORDER BY longitude;

-- List the two largest cities in Mexico (by population) 
SELECT city FROM north_american_cities
WHERE country = 'Mexico'
ORDER BY population DESC
LIMIT 2

-- List the third and fourth largest cities (by population) in the United States and their population
SELECT city FROM north_american_cities
WHERE country = 'United States'
ORDER BY population DESC
LIMIT 2 OFFSET 2

-- TASK 6
-- Find the domestic and international sales for each movie
SELECT * FROM movies
INNER JOIN boxoffice
    ON movies.id = boxoffice.movie_id;

-- Show the sales numbers for each movie that did better internationally rather than domestically 
SELECT *
FROM movies
INNER JOIN boxoffice
    ON movies.id = boxoffice.movie_id
WHERE International_sales > Domestic_sales;

-- List all the movies by their ratings in descending order
SELECT *
FROM movies
INNER JOIN boxoffice
    ON movies.id = boxoffice.movie_id
ORDER BY rating DESC

-- TASK 7

-- Find the list of all buildings that have employees
SELECT DISTINCT building FROM employees;

-- Find the list of all buildings and their capacity
SELECT * FROM Buildings;

-- List all buildings and the distinct employee roles in each building (including empty buildings)
SELECT DISTINCT building_name, role  FROM Buildings
LEFT JOIN Employees ON Building_name = Building;


-- TASK 8

-- Find the name and role of all employees who have not been assigned to a building
SELECT * FROM employees
WHERE Building IS NULL;

-- Find the names of the buildings that hold no employees
SELECT DISTINCT building_name
FROM buildings
LEFT JOIN employees
    ON building_name = employees.building
WHERE employees.building IS NULL;


-- TASK 9

-- List all movies and their combined sales in millions of dollars
SELECT DISTINCT
    title,
    (domestic_sales + international_sales) / 1000000 AS sales
FROM movies
INNER JOIN boxoffice
    ON movies.id = boxoffice.movie_id;

-- List all movies and their ratings in percent
SELECT DISTINCT
    title,
    (rating * 10) AS rate_percent
FROM movies
INNER JOIN boxoffice
    ON movies.id = boxoffice.movie_id;

-- List all movies that were released on even number years
SELECT title FROM movies WHERE year % 2 = 0;

-- TASK 10

-- Find the longest time that an employee has been at the studio.
SELECT name, MAX(years_employed) FROM employees;

-- For each role, find the average number of years employed by employees in that role
SELECT role, AVG(years_employed) as Average_years_employed
FROM employees
GROUP BY role;

-- Find the total number of employee years worked in each building
SELECT building, SUM(years_employed) FROM employees GROUP BY building

-- TASK 11

-- Find the number of Artists in the studio (without a HAVING clause)
SELECT COUNT(*) FROM employees WHERE role LIKE 'artist';

-- Find the number of Employees of each role in the studio
SELECT role, COUNT(Name) FROM employees GROUP BY role;

-- Find the total number of years employed by all Engineers
SELECT role, SUM(years_employed) FROM employees 
GROUP BY role HAVING role LIKE 'engineer';

-- TASK 12

-- Find the number of movies each director has directed
SELECT director, COUNT(*) FROM movies GROUP BY director;

-- Find the total domestic and international sales that can be attributed to each director
SELECT director, SUM(domestic_sales) + SUM(international_sales) AS Total
FROM movies 
LEFT JOIN boxoffice ON movies.id = boxoffice.movie_id 
GROUP BY director;

