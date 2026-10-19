-- Create a table named employee.
-- Insert data into the employee table.
-- Update the salary to 20000 for all employees in the HR department.
-- Delete the data for the employee having empId = 1.
-- Delete the entire table.


CREATE DATABASE IF NOT EXISTS company;

USE company;


-- CREATE A TABLE EMPLOYEE

CREATE TABLE IF NOT EXISTS employee(
  empId INT PRIMARY KEY,
  name VARCHAR(50),
  department VARCHAR(50),
  salary INT
);


-- SHOW THE TABLE 

SELECT * FROM employee;

-- INSERTION INTO THE TABLE 

INSERT INTO employee(empId,name,department,salary)
VALUES
(1,"Riti","IT",30000),
(2,"Rahul","HR",30000);

-- updating the salary of HR department

UPDATE employee 
SET salary = 20000
WHERE department = "HR";

-- DELETE DATA FOR EMP ID = 1

DELETE FROM employee
WHERE empId = 1;

-- DELETE THE ENTIRE TABLE 

DROP TABLE employee;

-- EITHER YOU CAN DO ( FOR DROPPIN ALL ROWS ) 

DELETE FROM employee;

-- OR

TRUNCATE TABLE employee;


