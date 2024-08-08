# ## Aggregate 2 (Group By) 
-- Problem 1
# Write a query to get the number of employees who has the same job title.
SELECT 
	COUNT(job_id) as job_count,
    job_id
FROM employees
GROUP BY job_id;

-- Problem 2
# list down the lowest salary of the employee of every manager and also display the manager_id.
SELECT 
	MIN(salary) as min_salary,
    manager_id
FROM employees
GROUP BY manager_id;

-- Problem 3
# list down the total salaries of every deparment # NOTE: salary should be in ascending 
SELECT 
	SUM(salary) as total_salary,
    department_id
FROM employees
GROUP BY department_id;

-- Problem 4
# list down the average salaries of every department exluding IT Deparment
SELECT 
	SUM(salary) as total_salary,
    department_id
FROM employees
WHERE job_id != 'IT_PROG'
GROUP BY department_id;

-- Problem 5
# fetch the top 3 department who is taking the highest salary among all other deparment
SELECT 
	SUM(salary) as total_salary,
    MAX(salary) as max_salary,
    AVG(salary) as average_salary,
    department_id
FROM employees
GROUP BY department_id
ORDER BY SUM(salary) DESC
LIMIT 3;

-- Problem 6
# list down all the department (job_id) whose avg salary is more than overall avg salary of the whole company
SELECT 
    job_id,
    AVG(salary) AS average_salary,
    (SELECT AVG(salary) FROM employees) AS company_average_salary
FROM employees
GROUP BY job_id
HAVING AVG(salary) > (
	SELECT AVG(salary)
    FROM employees
);

SELECT DATE_FORMAT(hire_date, '%Y') AS year_hired_more_than_10_emp
FROM employees
GROUP BY DATE_FORMAT(hire_date, '%Y')
HAVING COUNT(employee_id) > 10;

-- Problem 7
# Write a query to get employee ID, last name, and date of first salary of the employees.
SELECT
	employee_id,
    last_name,
    hire_date,
	ADDDATE(LAST_DAY(hire_date), INTERVAL 1 DAY) AS date_of_first_salary
FROM employees;

-- Problem 8
# find the department that contains more than 10 employees
SELECT 
	department_id,
    COUNT(employee_id) AS employee_count
FROM employees
GROUP BY department_id
HAVING COUNT(employee_id) > 10;