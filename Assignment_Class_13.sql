USE hr_db;

-- Problem 1
# Write a query to select first 10 records from a table.
SELECT *
FROM employees
LIMIT 10;

-- Problem 2
# Write a query to display the names (first_name, last_name) using alias name "First Name", "Last Name"
SELECT 
	first_name AS 'First Name',
    last_name AS 'Last Name'
FROM employees;

-- Problem 3
# Get unique department id list
SELECT 
	DISTINCT department_id
FROM employees;

-- Problem 4
# Write a query to get all employee details from the employee table order by first name, descending.
SELECT *
FROM employees
ORDER BY first_name DESC;

-- Problem 5
# Write a query to display fullname and salary
SELECT 
	CONCAT(first_name, ' ', last_name) AS full_name,
    salary
FROM employees;

-- Problem 6
# display all employee salary wise from lowest to highest
SELECT *
FROM employees
ORDER BY salary;

-- Problem 7
# how much money the company is spending on employees on salary
SELECT SUM(salary) 'Total Spendings on Salary'
FROM employees;

-- Problem 8
# show min, max and avg salary of comapny staff
SELECT
	MIN(salary) AS 'min_salary',
    MAX(salary) AS 'max_salary',
    AVG(salary) AS 'average_salary'
FROM employees;

-- Problem 9
# show employee name, their salary and the avg salary of all staff
SELECT
	CONCAT(first_name, ' ', last_name) AS full_name,
    salary,
    AVG(salary) AS 'average_salary'
FROM employees;
	
-- Problem 10
# how many emplyee does the company have, display the count
SELECT COUNT(employee_id) AS 'Total Employees'
FROM employees;

-- Problem 11
# show the number of employees in the company and the avg salary of all staff
SELECT 
	COUNT(employee_id) AS 'Total Employees',
    AVG(salary) AS 'Average Salary'
FROM employees;

-- Problem 12
# Write a query to get the number of jobs available in the employees table.
SELECT 
	COUNT(DISTINCT job_id) AS 'Number of Jobs'
FROM employees;

-- Problem 13
# Write a query get all first name from employees table in upper case.
SELECT UPPER(first_name)
FROM employees;

-- Problem 14
# Write a query to get first name from employees table after removing white spaces from both side.
SELECT TRIM(first_name)
FROM employees;

-- Problem 15
# Write a query to get monthly salary (round 2 decimal places) of each and every employee
# Note : Assume the salary field provides the 'annual salary' information.
SELECT TRUNCATE(salary / 12, 2)
FROM employees;

-- Problem 16
# find the 3rd highest paid employee
# NOTE: the query should return 1 row only
SELECT * 
FROM (
	SELECT *
    FROM employees
    ORDER BY salary DESC
    LIMIT 3
) as e
ORDER BY e.salary
LIMIT 1;

-- Problem 17
# Write a query to display the fullname (first_name, last_name) and salary for all employees whose salary is in the range $10,000 through $15,000.
SELECT 
	CONCAT(first_name, ' ', last_name) AS full_name,
    salary
FROM employees
WHERE salary BETWEEN 10000 AND 15000;

-- Problem 18
# Write a query to display the fullname (first_name, last_name) and department ID of all employees in departments 30 or 100. sort the resulting data in ascending order department wise.
SELECT 
	CONCAT(first_name, ' ', last_name) AS full_name,
    department_id
FROM employees
WHERE department_id BETWEEN 30 AND 100
ORDER BY department_id;

-- Problem 19
# Write a query to display the fullname (first_name, last_name) and salary for all employees whose salary is in the range $10,000 through $15,000 and are in department 30 or 100.
SELECT 
	CONCAT(first_name, ' ', last_name) AS full_name,
    salary
FROM employees
WHERE (salary BETWEEN 10000 AND 15000) AND (department_id BETWEEN 30 AND 100);

-- Problem 20
# Write a query to display the fullname (first_name, last_name) and hire date for all employees who were hired in 1987.
SELECT 
	CONCAT(first_name, ' ', last_name) AS full_name,
    hire_date
FROM employees
WHERE YEAR(hire_date) = 1987;

-- Problem 21
# Write a query to display the last name, job, and salary for all employees whose job is that of a Programmer or a Shipping Clerk, and whose salary is not equal to $4,500, $10,000, or $15,000.
SELECT
	last_name,
    job_id,
    salary
FROM employees e
WHERE salary NOT IN (4500, 10000, 15000) AND job_ID NOT IN ('IT_Prog', 'SH_CLERK');

-- Problem 22
# Write a query to select all record from employees where last name in 'BLAKE', 'SCOTT', 'KING' and 'FORD'.
SELECT *
FROM employees
WHERE last_name IN ('BLAKE', 'SCOTT', 'KING', 'FORD');


## Datetime
-- Problem 23
# Write a query to get the first name and hire date from employees table where hire date between '1987-06-01' and '1987-07-30'
SELECT 
	first_name,
    hire_date
FROM employees
WHERE hire_date BETWEEN '1987-06-01' AND '1987-07-30';

-- Problem 24
# Write a query to get first name of employees who joined in 1987.
SELECT 
	first_name
FROM employees
WHERE YEAR(hire_date) = 1987;

-- Problem 25
# Write a query to get the firstname, lastname who joined in the month of June.
SELECT
	first_name,
    last_name
FROM employees
WHERE MONTHNAME(hire_date) = 'June';

-- Problem 26
# Write a query to get the years in which more than 10 employees joined.
SELECT DATE_FORMAT(hire_date, '%Y') AS year_hired_more_than_10_emp
FROM employees
GROUP BY DATE_FORMAT(hire_date, '%Y')
HAVING COUNT(employee_id) > 10;

-- Problem 27
# Write a query to get department name, manager name, and salary of the manager for all managers whose experience is more than 5 years.
SELECT * FROM employees;
SELECT * FROM departments;
SELECT 
	d.department_name,
	CONCAT(m.first_name, ' ', m.last_name) AS manager_name,
    m.salary AS manager_salary
FROM employees e
LEFT JOIN departments d
	USING (department_id)
LEFT JOIN employees m
	ON e.manager_id = m.EMPLOYEE_ID
WHERE YEAR(NOW()) - YEAR(m.hire_date) > 5;

## Aggregate 1 (Functions only)
-- Problem 28
# Fetch the name of jobs the company have using table employees
SELECT DISTINCT job_id
FROM employees;

-- Problem 29
# Write down the query to show how much company spend on salaries also display the count. Use table employees.
SELECT
	SUM(salary) AS total_spend_on_salaries,
    COUNT(salary) AS total_salary_count
FROM employees;

-- Problem 30
# Write down the query to display the minimum salary that a company is giving also display the count. Use table employees.
SELECT
	MIN(salary) AS min_salary,
    COUNT(salary) AS total_salary_count
FROM employees;

-- Problem 31
# Write down the query to display the maximum salary that a company is giving also display the count. Use table employees.
SELECT
	MAX(salary) AS max_salary,
    COUNT(salary) AS total_salary_count
FROM employees;

-- Problem 32
# Write a query to get the highest, lowest, sum, and average salary among all employees.
SELECT
	MAX(salary) AS max_salary,
	MIN(salary) AS min_salary,
    AVG(salary) AS average_salary
FROM employees;

-- Problem 33
# Write down the query to display the maximum salary that a company is giving in the department IT_PROG
SELECT
	MAX(salary) AS max_salary_in_it_prog
FROM employees
WHERE job_id = 'IT_PROG';