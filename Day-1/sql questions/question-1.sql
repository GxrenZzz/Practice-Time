-- Write an Sql Query to 
-- 1 - crete a database company
-- 2 - create table employee in it 
-- 3 - delete/drop the Database

CREATE DATABASE company;

-- use the database

USE company;

-- create a table employee

CREATE TABLE employee(
  employee_id INT PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50)
);


-- show the table 

SELECT * FROM employee

-- Drop the Database

DROP DATABASE company;