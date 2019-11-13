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

:pushpin: block : Indentation de 3 espaces

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


## :two: Variables

##### :m: declaration :

```python
>>> x = 3
```

##### :m: types :

```python
>>> type(x)
<class 'int'>
```

| Type                 |  Python               | Format                   |
|----------------------|-----------------------|--------------------------|
| Nombre               | int, float            | 1 - 10, 1.0 - 10.0       |  
| Bouléen              | bool                  | True, False              |
| Chaine de caracteres | str                   | '1', "2.6", '2009-12-02' |

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



## :o2: git Commands

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
