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
    (rating * 10) AS percent
FROM movies
INNER JOIN boxoffice
    ON id = movie_id;

-- List all movies that were released on even number years
SELECT title 
FROM movies 
WHERE year % 2 = 0;


-- TASK 10

-- Find the longest time that an employee has been at the studio.
SELECT Role, Name, MAX(years_employed) AS Years_employed 
FROM employees;

-- For each role, find the average number of years employed by employees in that role
SELECT role, AVG(years_employed) AS Average_years_employed
FROM employees
GROUP BY role;

-- Find the total number of employee years worked in each building
SELECT building, SUM(years_employed)  AS Total_years_worked
FROM employees 
GROUP BY building

-- TASK 11

-- Find the number of Artists in the studio (without a HAVING clause)
SELECT COUNT(*) 
FROM employees 
role = 'Artist'

-- Find the number of Employees of each role in the studio
SELECT role, COUNT(Name) AS Number_of_employees
FROM employees 
GROUP BY role;

-- Find the total number of years employed by all Engineers
SELECT role, SUM(years_employed) AS sum_years_employed
FROM employees 
WHERE role = 'Engineer';

-- TASK 12

-- Find the number of movies each director has directed
SELECT director, COUNT(*) AS movies_directed
FROM movies 
GROUP BY director;

-- Find the total domestic and international sales that can be attributed to each director
SELECT director, SUM(domestic_sales) + SUM(international_sales) AS Total_sales
FROM movies 
INNER JOIN boxoffice ON id = movie_id 
GROUP BY director;

-- TASK 13

-- Add the studio's new production, Toy Story 4 to the list of movies (you can use any director)
INSERT INTO movies (title, director, year, length_minutes) 
VALUES ('Toy Story 4', 'Brad Bird', 2019, 100);

-- Toy Story 4 has been released to critical acclaim! It had a rating of 8.7, and made 340 million domestically and 270 million internationally. Add the record to the BoxOffice table. 
INSERT INTO boxoffice (movie_id, rating, domestic_sales, international_sales) 
VALUES (15, 8.7, 340000000, 270000000);


-- TASK 14

-- The director for A Bug's Life is incorrect, it was actually directed by John Lasseter
UPDATE movies
SET director = "John Lasseter"
WHERE title = "A Bug's Life";

-- The year that Toy Story 2 was released is incorrect, it was actually released in 1999
UPDATE movies
SET year = 1999
WHERE title = "Toy Story 2";

-- Both the title and director for Toy Story 8 is incorrect! The title should be "Toy Story 3" and it was directed by Lee Unkrich

UPDATE movies
SET title = "Toy Story 3",
    director = "Lee Unkrich"
WHERE title = "Toy Story 8";

-- TASK 15

-- This database is getting too big, lets remove all movies that were released before 2005.

-- the select statement
SELECT * FROM movies
WHERE year < 2005

DELETE FROM movies
WHERE year < 2005;

-- Andrew Stanton has also left the studio, so please remove all movies directed by him.

-- the select statement
SELECT * FROM movies
WHERE director = "Andrew Stanton";

DELETE FROM movies
WHERE director = "Andrew Stanton";


-- TASK 16

-- Create a new table named Database with the following columns:
-- – Name A string (text) describing the name of the database
-- – Version A number (floating point) of the latest version of this database
-- – Download_count An integer count of the number of times this database was downloaded
-- This table has no constraints.

CREATE TABLE Database (
    name TEXT,
    version FLOAT, 
    download_count INTEGER
);


-- TASK 17
-- Altering table name
ALTER TABLE mytable
RENAME TO new_table_name;

-- Altering table to add new column(s)
ALTER TABLE mytable
ADD column_name DataType OptionalTableConstraint 
    DEFAULT default_value;

-- Altering table to remove column(s)
ALTER TABLE mytable
DROP column_to_be_deleted;

-- Add a column named Aspect_ratio with a FLOAT data type to store the aspect-ratio each movie was released in.
ALTER TABLE movies
ADD Aspect_ratio FLOAT;

-- Add another column named Language with a TEXT data type to store the language that the movie was released in. Ensure that the default for this language is English.
ALTER TABLE movies
ADD Language TEXT 
    DEFAULT "English";


-- TASK 18
-- Drop table statement
DROP TABLE IF EXISTS mytable;

--We've sadly reached the end of our lessons, lets clean up by removing the Movies table
DROP TABLE IF EXISTS movies;

-- And drop the BoxOffice table as well
DROP TABLE IF EXISTS BoxOffice;