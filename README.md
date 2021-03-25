## Enviame Challenge

# Ejercicios 3-4-5-7 del challenge

# requerimientos

Tener instalado 
* **python3**
* **node**
* **npm**

# Ejercicio 3

para ejecutar el ejercicio 3 debera correr en la raiz del proyecto

```bash
    python3 Ejercicio3.py
```

esto retornara la respuesta a cuantas palabras iguales al derecho y al reves hay en el string 

# Ejercicio 4 

para ejecutar este ejercicio primero se deben cargar las dependencias del mismo

```bash
    npm install
```

luego ejecutar el script para hacer la peticion y almacenarla en u archivo .json


```bash
    node Ejercicio4.js
```
y este dara como resultado un archivo 'enviameApiResponse.json'  con la respuesta a la peticion de la aip de enviame

# Ejercicio 5

para ejecutar el ejercicio 3 debera correr en la raiz del proyecto

```bash
    python3 Ejercicio5.py
```

esto retorna la respuesta a cual es el primer numero en la sucesion de fibonacci que tiene mas de 1000 divisores 

# Ejercicio 6

Se genero una funcion 'calcularDias' que retorna los dias de demora en la entrega con respecto a una distancia 
se generan 10 numeros de forma random y se imprime los dias de demora


```bash
    python3 Ejercicio6.py
```

# Ejercicio 7

cuenta con la consulta para resolver el problema planteado en este ejercicio

```bash
    mysql
```

```sql
create database enviame7

``` 
   
```bash

mysql enviame7
```
```sql
CREATE TABLE `countries` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `continent_id` int(11) NOT NULL,
  `name` varchar(25) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `continents` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(25) NOT NULL,
  `anual_adjustment` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `employees` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `country_id` int(11) NOT NULL,
  `first_name` varchar(25) NOT NULL,
  `last_name` varchar(25) NOT NULL,
  `salary` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);

insert into continents values (null, 'América', 4);
insert into continents values (null, 'Europa', 5);
insert into continents values (null, 'Asia', 6);
insert into continents values (null, 'Oceanía', 6);
insert into continents values (null, 'Africa', 5);

insert into countries values (null, 1, 'Chile');
insert into countries values (null, 1, 'Argentina');
insert into countries values (null, 1, 'Canadá');
insert into countries values (null, 1, 'Colombia');
insert into countries values (null, 2, 'Alemania');
insert into countries values (null, 2, 'Francia');
insert into countries values (null, 2, 'España');
insert into countries values (null, 2, 'Grecia');
insert into countries values (null, 3, 'India');
insert into countries values (null, 3, 'Japón');
insert into countries values (null, 3, 'Corea del Sur');
insert into countries values (null, 4, 'Australia');

insert into employees values (null, 1, 'Pedro', 'Rojas', 2000);
insert into employees values (null, 2, 'Luciano', 'Alessandri', 2100);
insert into employees values (null, 3, 'John', 'Carter', 3050);
insert into employees values (null, 4, 'Alejandra', 'Benavides', 2150);
insert into employees values (null, 5, 'Moritz', 'Baring', 6000);
insert into employees values (null, 6, 'Thierry', 'Henry', 5900);
insert into employees values (null, 7, 'Sergio', 'Ramos', 6200);
insert into employees values (null, 8, 'Nikoleta', 'Kyriakopulu', 7000);
insert into employees values (null, 9, 'Aamir', 'Khan', 2000);
insert into employees values (null, 10, 'Takumi', 'Fujiwara', 5000);
insert into employees values (null, 11, 'Heung-min', 'Son', 5100);
insert into employees values (null, 12, 'Peter', 'Johnson', 6100);

UPDATE employees e     
inner join countries c  on e.country_id = c.id      
inner join continents cn on cn.id = c.continent_id
        set e.salary = e.salary + e.salary * cn.anual_adjustment/100
where e.salary <= 5000;

```