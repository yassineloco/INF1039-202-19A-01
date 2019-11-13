# Quizz (2019-11-20)


## :o: Commentaires

```SQL
# Je suis un commentaire sur une seule ligne
# Je commence par un hashtag suivi d'UN ESPACE

"""
Je suis un bloc de commentaires
# Je commence et termine par TROIS double-quote 

@author je suis un decorateur pemettant de specifier le nom de l'auteur
"""

```

## :a: Structure d'un programme


:one: Entrée/Sortie

:pushpin: Entrée :

```python
>>> int(input(""))
```


:pushpin: Sortie :

```python
>>> print("")
```

:pushpin: block :

```python
>>>    print("Indentation")
```

:pushpin: Erreur :

```
>>>    print("Indentation");
  File "<stdin>", line 1
    print("Indentation");
    ^
IndentationError: unexpected indent
```


:one: Entrée/Sortie

| Type                 |  SQL                  | Format                   |
|----------------------|-----------------------|--------------------------|
| Nombre               |INT, DOUBLE, FLOAT     | 1 - 10, 1.0 - 10.0       |  
| Date                 | DATE                  | '1990-01-01'             |
| booleen              | BOOLEAN               | True, False              |
| Chaine de caracteres | VARCHAR(<size>), TEXT | '1', '2.6', '2009-12-02' |
  
:pushpin: Sortie: 

| Option             | Description                                                  | 
|--------------------|--------------------------------------------------------------|
| AUTO_INCREMENT     | Omettre (N'apparait pas) dans le INSERT statement            |
| NOT NULL           | Le champ ne peut etre nul sinon Erreur                       |
| PRIMARY KEY        | :bulb: Peut etre placé ailleurs                              |
| DEFAULT `<valeur>` | :question:                                                   |

##### :m: USER 

:pushpin: Adresse IP Locale

```SQL
> CREATE USER 'nom'@'localhost' IDENTIFIED BY 'passwd'; -- Utilisateur accedant a la machine locale
```

:pushpin: Adresse IP Distante (avec `wildcard` **%** )

```SQL
> CREATE USER 'nom'@'%' IDENTIFIED BY 'passwd'; -- Utilisateur accedant a la machine distante
```

:two: DROP {DATABASE/TABLE} <name>;

##### :m: DATABASE

```SQL
> DROP DATABASE <name>;
```

##### :m: TABLE 

```SQL
> DROP TABLE <name>;
```
##### :m: USER 

```SQL
> DROP USER <name>;
```

:three: Keys :key:
 
 ##### :m: [Primaire](http://www.mysqltutorial.org/mysql-primary-key/) 
     
```SQL
    CREATE TABLE CLIENTS ( ...
       client INT AUTO_INCREMENT,
    
    
    PRIMARY KEY(client)    
    );
``` 

##### :m: composite (Primaire) 

```SQL
    CREATE TABLE VENTES ( ...
       produit INT,
       client INT,
    
    
    PRIMARY KEY(produit, client)    
    );
``` 
 ##### :m: Etrangere
 
 
```SQL
    CREATE TABLE VILLES ( ...
       ville INT,
       pays INT,
    
    
    FOREIGN KEY(pays) REFERENCES PAYS(pays),
    );
``` 

<img src='images/quiz.png' width="400" height="220"></img>
 

## :b: DCL


:four: Permissions

##### :m: [GRANT](http://www.mysqltutorial.org/mysql-grant.aspx)

```
> GRANT <Privilege> ON <base de donnee>.<tables> (ou `*` wildcard) TO <USER>;  
```

##### :m: [REVOKE](http://www.mysqltutorial.org/mysql-revoke.aspx)

```
> REVOKE <Privilege> ON <base de donnee>.<tables> (ou `*` wildcard) TO <USER>;  
```

:pushpin: Privileges 

| Privileges | Description                   | 
|------------|-------------------------------|
| ALL        | Tous les privileges           |
| SELECT     | Lecture seulement             |
| INSERT     | Ajout uniquement              |


## :ab: DML

voir l'explication  [`INSERT AUTO_INCREMENT`](https://dev.mysql.com/doc/mysql-tutorial-excerpt/5.7/en/example-auto-increment.html)



## :o2: MySQL Admin Commands

##### :m: SHOW <artifacts>
    
```
mysql> SHOW DATABASES;
```

```
mysql> SHOW TABLES;
```

```
mysql> SHOW GRANTS FOR rfc@localhost;
```

##### :m: describe

```
mysql> DESCRIBE <nom de table>;
```


##### :m:  use

```
mysql> USE <database>;
```
