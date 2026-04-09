# Write your MySQL query statement below
SELECT name as Customers
FROM Customers x
WHERE x.id NOT IN(
    SELECT c.id 
    FROM Customers c
    JOIN Orders o 
    ON c.id = o.customerId
)

