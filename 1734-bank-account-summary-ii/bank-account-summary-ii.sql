# Write your MySQL query statement below
select u.name,  COALESCE(SUM(t.amount), 0) as balance
from Users u
left join Transactions t
on u.account = t.account
group by u.account, t.account

having balance > 10000