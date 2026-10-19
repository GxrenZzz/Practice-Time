USE company;

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    department VARCHAR(50),
    city VARCHAR(50),
    salary DECIMAL(10, 2)
);

INSERT INTO employees (id, name, age, department, city, salary)
VALUES
(1, 'Rahul', 25, 'IT', 'Mumbai', 1500),
(2, 'Afsara', 26, 'HR', 'Pune', 2000),
(3, 'Abhimanyu', 27, 'IT', 'Mumbai', 2500),
(4, 'Aditya', 25, 'Marketing', 'Surat', 2400),
(5, 'Raj', 24, 'Finance', 'Indore',  2000);



-- WRITE A QUERY TO FIND THE TOTAL NUMBER OF EMPLOYEES WORKING IN IT DEPARTMENT

SELECT COUNT(*) FROM employees
WHERE department = "IT";


-- ALL THE EMP names starting from r - like and wildcard operator

SELECT * FROM employees
WHERE name LIKE "R%";

-- Find Distict salries from the salray table 

SELECT DISTINCT salary FROM employees;

-- Find the second highest salary in the table - if all salaries are diff

SELECT salary AS second_highest_salary FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;

-- Find the second highest salary in the table - if all salaries are not diff


SELECT DISTINCT salary AS second_highest_salary FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;


-- another way 

SELECT MAX(salary) FROM employees
WHERE salary <> (SELECT MAX(salary) FROM employees);


-- NTH HIGHEST SALARY 


SELECT DISTINCT salary AS second_highest_salary FROM employees
ORDER BY salary DESC
LIMIT 2 OFFSET 1;


-- TOP 2 SALARIES FROM EMPLYESS

SELECT salary FROM employees
ORDER BY salary DESC
LIMIT 2;

-- QUERY TO CALCULATE THE TOTAL SALARY AND AVERGAE SALARY IN DEPARTMENT 

SELECT department,SUM(salary) AS TOTAL_SALARY , AVG(salary) AS AVG_SALARY FROM employees
GROUP BY department;


-- quey to find null vlaues in deparment

SELECT * FROM employees
WHERE DEPARTMENT IS NULL;

-- QUERY TO FIND DUPLICATE VALUES IN DEPARTMENT -> Group By + having COUNT(*) > 1

SELECT department , COUNT(*) AS TOTAL
FROM employees
GROUP BY department
HAVING COUNT(*)>1;