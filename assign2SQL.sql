/* Assign 1 Create database and tables */

 CREATE database People;
 use People;
 
 CREATE TABLE person (
    id INTEGER PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INTEGER
);

CREATE TABLE pet (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50),
    breed VARCHAR(50),
    age INTEGER,
    dead INTEGER
);

CREATE TABLE person_pet (
    person_id INTEGER,
    pet_id INTEGER
);



/* Assign 2 Create a multi-table database */
/* 1. In these tables I made a 3rd relation table to link them. 
How would you get rid of this relation table person_pet 
and put that information right into person? 
What's the implication of this change? */

CREATE TABLE personAndPet (
    id INTEGER PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INTEGER,  
    name_pet VARCHAR(50),
    breed VARCHAR(50),
    age_pet INTEGER,
    dead_pet INTEGER
);

/*If you can put one row into person_pet, can you put 
more than one? How would you record a crazy cat lady with 50 cats? */
/* Answer: I can put more the one row, but there are more than one row if one person has 
more than one pet. There are 50 rows or records if  a crazy cat lady with 50 cats */

/* Create another table for the cars people might own. however table Person is already created before, 
and create its corresponding relation table.  */
 
CREATE TABLE car (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50),
    modle VARCHAR(50),
    year INTEGER,
    cost INTEGER
);

CREATE TABLE person_car (
    person_id INTEGER,
    car_id INTEGER
);

/* all of above are successfule to be excuted */

/* The following links cover the inofrmation about "oracle datatypes"
https://docs.oracle.com/cd/B28359_01/server.111/b28318/datatype.htm#CNCPT012
https://docs.oracle.com/cd/B28359_01/server.111/b28286/sql_elements001.htm#SQLRF0021
https://www.w3resource.com/oracle/oracle-data-types.php

I used the following types:
CHAR, VARCHAR, CLOB, DATE, BLOB, etc. 
*/


/* Assign 3 Example SQL Code for Person-Pet tables */
insert into person values (1,'Dave','wolf',99);
insert into person values (2, 'Bart', 'Simpson',10);
insert into person values (3, 'Crazy Cat Lady','', 99);
select * from person;

insert into pet values (10,'fifi', 'dog',4,1);
insert into pet values (11, 'toto', 'dog', 8, 1);
insert into pet values (12, 'cat1', 'cat', 5, 1);
insert into pet values (13, 'cat2', 'cat', 5, 1);
insert into pet values (14, 'cat3', 'cat', 6, 1);
insert into pet values (15, 'cat4', 'cat', 8, 1);
insert into pet values (16, 'cat5', 'cat', 3, 1);
select * from pet;

insert into person_pet values (1,10);
insert into person_pet values (2,11);
insert into person_pet values (2,10);
insert into person_pet values (3,12);
insert into person_pet values (3,13);
insert into person_pet values (3,14);
insert into person_pet values (3,15);
insert into person_pet values (3,16);

select * from person_pet;

update person_pet set person_id = 2 where pet_id = 16;    /* get error to run this */

select * from person inner join 
person_pet on person.id = person_pet.person_id
inner join pet on person_pet.pet_id = pet.id;

select first_name, last_name, name as 'Pet Name', pet.age as 'Pet Age'
from person inner join 
person_pet on person.id = person_pet.person_id
inner join pet on person_pet.pet_id = pet.id;


/* insert example */
INSERT INTO person (id, first_name, last_name, age)
    VALUES (0, 'Dave', 'Wolfe', 25);

INSERT INTO pet (id, name, breed, age, dead)
    VALUES (0, "Fluffy", "Unicorn", 1000, 0);

INSERT INTO pet VALUES (1, "Gigantor", "Robot", 1, 1);

/* Inserting Data
Insert yourself and your pets (or imaginary pets like I have). 
Insert the proper entries in the Person_Pet table to show ownership. */
INSERT INTO person (id, first_name, last_name, age)
    VALUES (4, 'Bob', 'Xr', 45);
    
INSERT INTO pet (id, name, breed, age, dead)
    VALUES (2, "Cute", "Wow", 700, 0);
    
INSERT INTO person_pet (person_id, pet_id)
    VALUES (0, 0);
      
INSERT INTO person_pet (person_id, pet_id)
    VALUES (4, 2);
/* Say I give you my dead unicorn. How do we execute that exchange? */
update person_pet set person_id = 4 where pet_id = 0; 
select * from person_pet;

/* What changes can we make to the tables to show that fluffy used to belong to me? -This is to change the ownership back to David */
INSERT INTO person_pet (person_id, pet_id)
    VALUES (0, 0);  
select * from person_pet;

/* Make those changes */
/* Add Mike with ID 5 */
INSERT INTO person (id, first_name, last_name, age)
    VALUES (5, 'Mike', 'White', 35);
select * from person;

INSERT INTO pet (id, name, breed, age, dead)
    VALUES (3, "Dog1", "Huskin", 10, 0);
select * from pet;


/* Inserting Referential Data */
INSERT INTO person_pet (person_id, pet_id) VALUES (0, 0);
INSERT INTO person_pet VALUES (0, 1);

/* Add the relationships for you and your pets */
INSERT INTO person_pet (person_id, pet_id)
    VALUES (4, 2);

/* Using this table, could a pet be owned by more than one person? Yes.
Is that logically possible? Could be
What about the family dog? Not logic
Wouldn't everyone in the family technically own it? Yes */

/* Given the above, and given that you have an alternative design 
that puts the pet_id in the person table, 
which design is better for this situation? The above design. */



/* Selecting Data */
SELECT * FROM person;
SELECT name, age FROM pet;
SELECT name, age FROM pet WHERE dead = 0;
SELECT * FROM person WHERE first_name != 'Dave';


SELECT * FROM pet where age >10;
SELECT * FROM person where age < 45;
SELECT * FROM person where age > 45;
SELECT * FROM person where first_name = "Dave" and age > 45;
SELECT first_name, last_name, age  FROM person where first_name = "Dave" and age < 45;
SELECT ID, first_name, age FROM person where first_name = "Mike" or age > 45;



/* Selecting Across Many Tables */
SELECT pet.id, pet.name, pet.age, pet.dead
    FROM pet, person_pet, person
    WHERE
    pet.id = person_pet.pet_id AND
    person_pet.person_id = person.id AND
    person.first_name = 'Dave';

/* This may be a mind blowing weird way to look at data if you already know a language like Python or Ruby. 
Take the time to model the same relationships using classes and objects then map it to this setup.
class Person:
  def __init__(self, id, first_name, last_name, age):
    self.id = id
    self.first_name = first_name
    self.last_name = last_name
    self.age = age

class Pet:
  def __init__(self, id, name, breed, age, dead):
    self.id = id
    self.name = name
    self.breed = breed
    self.age = age
    self.dead = dead
*/

/* Do a query that finds your pets you've added thus far. */
SELECT * FROM pet;


/* Change the queries to use your person.id instead of the person.name like I've been doing. */





























