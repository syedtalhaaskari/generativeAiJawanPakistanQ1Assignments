-- https://github.com/mdanish0320/teaching-class/blob/master/JP-BE-PY-batch-1/mysql-class/sample-databases/hr_db/db.sql

-- Group BY

-- Write a query to get the number of employees who has the same job title.
SELECT 
	COUNT(job_id) as job_count,
    job_id
FROM employees
GROUP BY job_id;

-- list down the lowest salary of the employee of every manager and also display the manager_id.
SELECT 
	MIN(salary) as min_salary,
    manager_id
FROM employees
GROUP BY manager_id;

-- list down the total salaries of every deparment # NOTE: salary should be in ascending order
SELECT 
	SUM(salary) as total_salary,
    department_id
FROM employees
GROUP BY department_id;

-- list down the average salaries of every department exluding IT Deparment
SELECT 
	SUM(salary) as total_salary,
    department_id
FROM employees
WHERE job_id != 'IT_PROG'
GROUP BY department_id;

-- fetch the top 3 department who is taking the highest salary among all other deparment
SELECT 
	SUM(salary) as total_salary,
    MAX(salary) as max_salary,
    AVG(salary) as average_salary,
    department_id
FROM employees
GROUP BY department_id
ORDER BY SUM(salary) DESC
LIMIT 3;

-- ignore this
-- list down all the department (job_id) whose avg salary is more than overall avg salary of the whole company
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

-- Write a query to get employee ID, last name, and date of first department (where he was working in, table name "job_history") of the employees.
SELECT
	employee_id,
    last_name,
    hire_date,
	ADDDATE(LAST_DAY(hire_date), INTERVAL 1 DAY) AS date_of_first_salary
FROM employees;

-- find the department that contains more than 10 employees
SELECT 
	department_id,
    COUNT(employee_id) AS employee_count
FROM employees
GROUP BY department_id
HAVING COUNT(employee_id) > 10;

-- Write a query to get the years in which more than 10 employees joined.
SELECT
    DATE_FORMAT(hire_date, '%Y') as hiring_year,
    COUNT(hire_date) as total_hirings
FROM employees
GROUP BY DATE_FORMAT(hire_date, '%Y')
HAVING COUNT(hire_date) > 10;

-- Find the number of employees in each department.
SELECT
    department_id,
    COUNT(department_id) AS total_employees
FROM employees
GROUP BY department_id;

-- Calculate the average salary for each job title.
SELECT
    job_id,
    AVG(salary) AS average_salary
FROM employees
GROUP BY job_id;

-- List the total salary expenditure for each department.
SELECT
    department_id,
    SUM(salary) as total_salary_expenditure
FROM employees
GROUP BY department_id;

-- Find the maximum salary in each department.
SELECT
    department_id,
    MAX(salary) as max_salary
FROM employees
GROUP BY department_id;

-- Count the number of employees hired in each year.
SELECT
    DATE_FORMAT(hire_date, '%Y') AS hiring_year,
    COUNT(hire_date) AS total_hirings
FROM employees
GROUP BY DATE_FORMAT(hire_date, '%Y');

-- Determine the number of employees with the same manager.
SELECT
	CONCAT(m.FIRST_NAME, ' ', m.last_name) AS full_name,
    e.manager_id,
    COUNT(e.manager_id) AS total_managed_emp
FROM employees e
JOIN employees m
	ON e.manager_id = m.EMPLOYEE_ID
GROUP BY e.manager_id;

-- Find the average commission percentage for each department.
SELECT
    e.DEPARTMENT_ID,
    AVG(e.COMMISSION_PCT) AS avg_commission
FROM employees e
GROUP BY e.DEPARTMENT_ID;

-- Calculate the total duration (in days) that each employee spent in their job(s) from the `job_history` table.
SELECT
    DATEDIFF(jh.END_DATE, jh.START_DATE) AS total_days,
    jh.EMPLOYEE_ID
FROM job_history jh;

-- Find the highest salary offered for each job title.
SELECT
    MAX(e.salary) AS max_salary_offered,
    e.JOB_ID
FROM employees e
GROUP BY e.JOB_ID;

-- JOIN

-- List all employees along with their department names.
SELECT
	e.EMPLOYEE_ID,
    e.DEPARTMENT_ID,
    d.DEPARTMENT_NAME
FROM employees e
JOIN departments d
	USING (DEPARTMENT_ID);

-- Find all employees and their job titles.
SELECT
	e.EMPLOYEE_ID,
    e.JOB_ID,
    j.JOB_TITLE
FROM employees e
JOIN jobs j
	USING (JOB_ID);

-- Retrieve the job history of each employee along with the department name they worked in
SELECT
	jh.*,
    d.DEPARTMENT_NAME
FROM job_history jh
JOIN departments d
	USING (DEPARTMENT_ID);

-- List the employees who are currently working under the same manager, displaying the manager's name.
SELECT
	CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
	CONCAT(m.first_name, ' ', m.last_name) AS manager_name
FROM employees e
JOIN employees m
	ON e.MANAGER_ID = m.EMPLOYEE_ID;

-- Retrieve the details of all departments located in a specific city i.e "Tokyo".
SELECT
	d.*,
    l.CITY
FROM departments d
JOIN locations l
	USING (LOCATION_ID)
WHERE l.CITY = 'Seattle';

-- Retrieve the details of all departments located in a specific cities i.e "Sydney" and "Toronto".
SELECT
	d.*,
    l.CITY
FROM departments d
JOIN locations l
	USING (LOCATION_ID)
WHERE l.CITY IN ('Sydney', 'Seattle', 'Toronto');

-- LEFT JOIN

-- List all employees and their managers, including those without managers
SELECT
	CONCAT(m.FIRST_NAME, ' ', m.LAST_NAME) AS manager_name,
	e.*
FROM employees e
LEFT JOIN employees m
	ON e.MANAGER_ID = m.EMPLOYEE_ID;

-- Find all departments and their employees, including departments with no employees.
SELECT
	e.EMPLOYEE_ID,
	d.*
FROM departments d
LEFT JOIN employees e
	USING (DEPARTMENT_ID);

-- Retrieve a list of all job titles and the employees who have that job, including job titles with no employees.
SELECT
	j.JOB_TITLE,
	e.EMPLOYEE_ID
FROM jobs j
LEFT JOIN employees e
	USING (JOB_ID);

-- RIGHT JOIN Assignments
-- Find all employees and the locations they are working in, including locations without any employees.
SELECT
	e.EMPLOYEE_ID,
    l.*
FROM employees e
RIGHT JOIN departments d
	USING (DEPARTMENT_ID)
RIGHT JOIN locations l
	USING (LOCATION_ID);

-- List all countries and the regions they belong to, including regions without any countries.
SELECT 
	c.COUNTRY_NAME,
    c.COUNTRY_ID,
    r.REGION_NAME,
    r.REGION_ID
FROM countries c
RIGHT JOIN regions r
	USING (REGION_ID);

-- JOIN + Group BY

-- List the number of employees working in each city. 
SELECT
	COUNT(e.EMPLOYEE_ID) AS total_employees,
    l.CITY
FROM employees e
RIGHT JOIN departments d
	USING (DEPARTMENT_ID)
RIGHT JOIN locations l
	USING (LOCATION_ID)
GROUP BY l.CITY;

-- List the total salary expenditure for each department, along with the department name.
SELECT
	SUM(e.salary) AS total_salary_expenditure,
    d.DEPARTMENT_NAME
FROM employees e
RIGHT JOIN departments d
	USING (DEPARTMENT_ID)
GROUP BY d.DEPARTMENT_ID;

-- Count the number of employees in each city.
SELECT
	COUNT(e.EMPLOYEE_ID) AS total_employees,
    l.CITY
FROM employees e
RIGHT JOIN departments d
	USING (DEPARTMENT_ID)
RIGHT JOIN locations l
	USING (LOCATION_ID)
GROUP BY l.CITY;

-- Calculate the average salary for each job title within each department.
SELECT
	AVG(e.salary) AS average_salary,
    j.JOB_TITLE,
    e.JOB_ID,
    e.DEPARTMENT_ID
FROM employees e
LEFT JOIN jobs j
	USING (JOB_ID)
GROUP BY e.DEPARTMENT_ID, e.JOB_ID;

-- List the number of employees hired in each year for each job title.
SELECT
	COUNT(e.EMPLOYEE_ID) AS employee_count,
    j.JOB_TITLE,
    e.JOB_ID,
    DATE_FORMAT(e.hire_date, '%Y') AS hiring_year
FROM employees e
LEFT JOIN jobs j
	USING (JOB_ID)
GROUP BY DATE_FORMAT(e.hire_date, '%Y');

-- Find the highest salary paid in each region.
SELECT
	MAX(e.salary) as max_salary,
    r.REGION_NAME,
    r.REGION_ID
FROM employees e
JOIN departments d
	USING (DEPARTMENT_ID)
JOIN locations l
	USING (LOCATION_ID)
JOIN countries c
	USING (COUNTRY_ID)
JOIN regions r
	USING (REGION_ID)
GROUP BY r.REGION_NAME;

-- Count the number of employees in each country.
SELECT
	COUNT(e.EMPLOYEE_ID) as emp_count,
    c.COUNTRY_NAME
FROM employees e
JOIN departments d
	USING (DEPARTMENT_ID)
JOIN locations l
	USING (LOCATION_ID)
RIGHT JOIN countries c
	USING (COUNTRY_ID)
GROUP BY c.COUNTRY_NAME;

-- Calculate the average salary and the number of employees for each department located in a specific region.
SELECT
	AVG(e.salary) as avg_salary,
    COUNT(e.EMPLOYEE_ID) as emp_count,
    e.DEPARTMENT_ID,
    d.DEPARTMENT_NAME,
    r.REGION_NAME,
    r.REGION_ID
FROM employees e
RIGHT JOIN departments d
	USING (DEPARTMENT_ID)
LEFT JOIN locations l
	USING (LOCATION_ID)
JOIN countries c
	USING (COUNTRY_ID)
JOIN regions r
	USING (REGION_ID)
GROUP BY e.DEPARTMENT_ID, r.REGION_NAME
HAVING r.REGION_NAME = 'Europe';

-- Calculate the average salary and the number of employees for each department located in a specific region.
SELECT
	AVG(e.salary) as avg_salary,
    COUNT(e.EMPLOYEE_ID) as emp_count,
    d.DEPARTMENT_ID,
    d.DEPARTMENT_NAME
FROM employees e
RIGHT JOIN departments d
	USING (DEPARTMENT_ID)
LEFT JOIN locations l
	USING (LOCATION_ID)
JOIN countries c
	USING (COUNTRY_ID)
JOIN regions r
	USING (REGION_ID)
WHERE r.REGION_ID = 1
GROUP BY e.DEPARTMENT_ID, r.REGION_ID;

SELECT
    AVG(e.salary) as avg_salary,
    COUNT(e.EMPLOYEE_ID) as emp_count,
    e.DEPARTMENT_ID,
    d.DEPARTMENT_NAME,
    r.REGION_NAME,
    r.REGION_ID
FROM employees e
JOIN departments d ON e.DEPARTMENT_ID = d.DEPARTMENT_ID
JOIN locations l ON d.LOCATION_ID = l.LOCATION_ID
JOIN countries c ON l.COUNTRY_ID = c.COUNTRY_ID
JOIN regions r ON c.REGION_ID = r.REGION_ID
WHERE r.REGION_ID = 1
GROUP BY e.DEPARTMENT_ID, d.DEPARTMENT_NAME, r.REGION_NAME, r.REGION_ID;