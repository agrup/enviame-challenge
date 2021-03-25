 UPDATE employees e     
    inner join countries c  on e.country_id = c.id      
    inner join continents cn on cn.id = c.continent_id
          set e.salary = e.salary + e.salary * cn.anual_adjustment/100
    where e.salary <= 5000;