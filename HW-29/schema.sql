PRAGMA foreign_keys = ON;

-- ძველი ცხრილების წაშლა
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;

-- 1. დეპარტამენტები (departments)
CREATE TABLE departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL,
    location VARCHAR(50) NOT NULL
);

-- 2. თანამშრომლები (employees)
CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL,
    department_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES departments(id) ON DELETE SET NULL
);

-- =============================================
-- სატესტო მონაცემები
-- =============================================

INSERT INTO departments (name, location) VALUES
('IT', 'New York'),
('Marketing', 'New York'),
('Sales', 'Los Angeles'),
('Finance', 'Los Angeles'),
('HR', 'Chicago'); -- ცარიელი დეპარტამენტი EXISTS-ის ტესტირებისთვის

INSERT INTO employees (name, salary, department_id) VALUES
('John Doe', 5000.00, 1),
('Jane Smith', 4500.00, 1),
('David Miller', 6000.00, 1),
('Emily Davis', 3000.00, 2),
('Michael Brown', 3500.00, 2),
('Sarah Wilson', 4000.00, 3),
('James Taylor', 3200.00, 3),
('Anna White', 4800.00, 4);

-- =============================================
-- SQL მოთხოვნები (QUERIES)
-- =============================================

-- 1. საშუალოზე მეტი ხელფასის მქონე თანამშრომლები (Subquery)
SELECT name, salary 
FROM employees 
WHERE salary > (SELECT AVG(salary) FROM employees);

-- 2. თანამშრომლის სახელი, ხელფასი და დეპარტამენტის სახელი (JOIN-ის გარეშე, Subquery)
SELECT name, salary, 
       (SELECT name FROM departments WHERE departments.id = employees.department_id) AS department_name 
FROM employees;

-- 3. თანამშრომლები New York-ის დეპარტამენტებიდან (IN ოპერატორით)
SELECT * 
FROM employees 
WHERE department_id IN (SELECT id FROM departments WHERE location = 'New York');

-- 4. დეპარტამენტები, სადაც მინიმუმ 1 თანამშრომელია (EXISTS ოპერატორით)
SELECT * 
FROM departments d 
WHERE EXISTS (SELECT 1 FROM employees e WHERE e.department_id = d.id);

-- 5. ხელფასი მეტია Marketing-ის ნებისმიერ (მინიმალურ) ხელფასზე (> ANY / > MIN)
-- სტანდარტულ SQL-ში: WHERE salary > ANY (SELECT salary FROM employees WHERE department_id = 2)
SELECT * 
FROM employees 
WHERE salary > (SELECT MIN(salary) FROM employees WHERE department_id = (SELECT id FROM departments WHERE name = 'Marketing'));

-- 6. ხელფასი მეტია IT-ის ყველა (მაქსიმალურ) ხელფასზე (> ALL / > MAX)
-- სტანდარტულ SQL-ში: WHERE salary > ALL (SELECT salary FROM employees WHERE department_id = 1)
SELECT * 
FROM employees 
WHERE salary > (SELECT MAX(salary) FROM employees WHERE department_id = (SELECT id FROM departments WHERE name = 'IT'));

-- 7. თანამშრომლები New York ან Los Angeles ლოკაციიდან დუბლიკატების გარეშე (UNION)
SELECT e.name, e.salary, d.location 
FROM employees e JOIN departments d ON e.department_id = d.id 
WHERE d.location = 'New York'
UNION
SELECT e.name, e.salary, d.location 
FROM employees e JOIN departments d ON e.department_id = d.id 
WHERE d.location = 'Los Angeles';

-- 8. იგივე მოთხოვნა დუბლიკატებით (UNION ALL)
SELECT e.name, e.salary, d.location 
FROM employees e JOIN departments d ON e.department_id = d.id 
WHERE d.location = 'New York'
UNION ALL
SELECT e.name, e.salary, d.location 
FROM employees e JOIN departments d ON e.department_id = d.id 
WHERE d.location = 'Los Angeles';
