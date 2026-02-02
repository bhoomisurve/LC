# Write your MySQL query statement below
select id,
sum(case when month = 'Jan' Then revenue end) as Jan_Revenue,
sum(case when month = 'Feb' Then revenue end) as Feb_Revenue,
sum(case when month = 'Mar' Then revenue end) as Mar_Revenue,
sum(case when month = 'Apr' Then revenue end) as Apr_Revenue,
sum(case when month = 'May' Then revenue end) as May_Revenue,
sum(case when month = 'Jun' Then revenue end) as Jun_Revenue,
sum(case when month = 'Jul' Then revenue end) as Jul_Revenue,
sum(case when month = 'Aug' Then revenue end) as Aug_Revenue,
sum(case when month = 'Sep' Then revenue end) as Sep_Revenue,
sum(case when month = 'Oct' Then revenue end) as Oct_Revenue,
sum(case when month = 'Nov' Then revenue end) as Nov_Revenue,
sum(case when month = 'Dec' Then revenue end) as Dec_Revenue

from Department 
group by id;