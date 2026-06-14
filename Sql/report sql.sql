use testd;

select * from churn;


select count(*) from Churn;

select
round(avg(Exited)*100,2) as churn_rate
from churn;

select geography,count(customerID),round(avg(Exited)*100,2) as churn_rate
from churn
group by geography;

select gender,count(gender),round(avg(Exited)*100,2) as churn_rate
from churn
group by gender;

select IsActiveMember,count(IsActiveMember),round(avg(Exited)*100,2) as churn_rate
from churn
group by IsActiveMember;

select Exited,round(avg(CreditScore),2) as avg_credit_score
from Churn 
group by Exited;

select Exited,round(avg(EstimatedSalary),2) as avg_salary
from Churn 
group by Exited;

select geography,gender,COUNT(*) customers,sum(exited),
round(avg(exited)*100,2) as churn_rate
from churn
group by geography,gender
order by churn_rate desc;


select NumOfProducts,count(*),round(avg(Exited)*100,2) as churn_rate from churn
group by NumOfProducts
order by churn_rate desc;

