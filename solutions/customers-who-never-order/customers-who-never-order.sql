# Write your MySQL query statement below
Select name as Customers from Customers
where id NOT in (select customerId from Orders);