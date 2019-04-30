-- 1a
SELECT first_name,last_name FROM sakila.actor;
-- alter table sakila.actor
-- add column Actor_Name VARCHAR (30) AFTER last_name;

-- 1b
select *, CONCAT (first_name, " " , last_name) as Actor_Name
from sakila.actor;
-- alter table sakila.actor drop column Actor_Name;

-- 2a
alter table sakila.actor drop column last_update;
select *
	from sakila.actor
    where first_name = 'Joe';
    
-- 2b    
select *
	from sakila.actor
    where last_name like '%Gen%';
    
-- 2c
select * 
	from sakila.actor
    where last_name like '%Li%';

-- 2d
select country_id, country 
	from sakila.country 
	where country in ('Afghanistan', 'Bangladesh', 'China');

-- 3a    
alter table sakila.actor add column description blob;
-- 3b
alter table sakila.actor drop column description;

-- 4a
select count(actor_id), last_name
	from sakila.actor
    group by last_name
    order by count(last_name) desc;
    
-- 4b
select last_name, count(*) as Number_Of_Actors
	from actor
	group by last_name
	having count(*) >= 2;    

-- 4c
update sakila.actor 
	set first_name = 'HARPO'
	where first_name = 'GROUCHO'
    and last_name = 'WILLIAMS';

-- 4d    
update sakila.actor 
	set first_name = 'GROUCHO'
	where first_name = 'HARPO'
    and last_name = 'WILLIAMS';

-- 5a
describe sakila.address;

-- 6a
use sakila;
select address.address, staff.first_name, staff.last_name
From address
Inner Join staff On address.address_id = staff.address_id;

-- 6b
use sakila;
select payment.amount, staff.first_name, staff.last_name, payment.payment_date
from payment
inner join staff on payment.payment_id = staff.address_id AND payment.payment_date like '%2005-08%';

-- 6c
use sakila;
select film.title as 'Film Title', count(film_actor.actor_id) as 'Number of Actors'
from film_actor
inner join film on film_actor.film_id = film.film_id
group by film.title;

-- 6d
use sakila;
SELECT film.title, (
SELECT COUNT(*) FROM inventory
WHERE film.film_id = inventory.film_id
) AS 'Number of Copies'
FROM film
WHERE title = "Hunchback Impossible";

-- 6e
use sakila;
select customer.first_name, customer.last_name, sum(payment.amount) AS 'Total Amount Paid'
from payment
inner join customer on payment.customer_id = customer.customer_id
group by customer.customer_id
order by customer.last_name asc;

-- 7a
use sakila;
select film.title 
from film
where title like 'Q%' or title like 'K%'
and language_id in (select language_id from language where name = 'English');

-- 7b
use sakila;
select actor.first_name, actor.last_name
from actor
where actor_id in (select actor_id from film_actor where film_id =
(select film_id from film where title = 'Alone Trip'));

-- 7c
use sakila;
select customer.email, customer.first_name, customer.last_name
from customer
inner join address on customer.address_id = address.address_id
inner join city on address.city_id = city.city_id
inner join country on city.country_id = country.country_id
where country.country = 'Canada';

-- 7d
use sakila;
select film.title, category.name
from category
inner join film_category on film_category.category_id = category.category_id
inner join film on film.film_id = film_category.film_id
where category.name = 'Family';

-- 7e
use sakila;
select film.title as 'Film_Title', count(rental.rental_id) as 'Number_Of_Rentals'
from rental
inner join inventory on rental.inventory_id = inventory.inventory_id
inner join film on film.film_id = inventory.film_id
group by film.title
order by Number_Of_Rentals desc;

-- 7f
use sakila;
select store.store_id, sum(payment.amount) as 'Total_Payment'
from store
inner join staff on staff.store_id = store.store_id
inner join payment on payment.staff_id = staff.staff_id
group by store.store_id;

-- 7g
use sakila;
select store.store_id, city.city, country.country
from store
inner join address on address.address_id = store.address_id
inner join city on city.city_id = address.city_id
inner join country on country.country_id = city.country_id;

-- 7h
use sakila;
select category.name as 'Genre', sum(payment.amount) as 'Gross_Revenue'
from category
inner join film_category on film_category.category_id = category.category_id
inner join inventory on inventory.film_id = film_category.film_id
inner join rental on rental.inventory_id = inventory.inventory_id
inner join payment on payment.rental_id = rental.rental_id
group by category.name
order by Gross_Revenue desc
limit 5;

-- 8a
use sakila;
create view revenue_by_genre as
select category.name as 'Genre', sum(payment.amount) as 'Gross_Revenue'
from category
inner join film_category on film_category.category_id = category.category_id
inner join inventory on inventory.film_id = film_category.film_id
inner join rental on rental.inventory_id = inventory.inventory_id
inner join payment on payment.rental_id = rental.rental_id
group by category.name
order by Gross_Revenue desc
limit 5;

-- 8b
use sakila;
select * from revenue_by_genre;

-- 8c
use sakila;
drop view revenue_by_genre;










    

    

    

    
    





