-- Write your query below
select name from customers where id not in (select t1.customer_id from orders as t1 join customers as t2 on t1.customer_id = t2.id);