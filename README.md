# TP Virtualisation - Traefik

## Création du cluster swarm

Etat du cluster swarm, avec 2 workers (-40 et -37) et 1 manager (-245) :

![swarm](/assets/nodes.png)

## Création d'un réseau overlay (traefik-net)

Création du réseau overlay traefik-net :

```bash
docker network create --driver=overlay traefik-net
```

![traefik-replicas](/assets/traefik_replicas.png)

## Services

### Mysql

Création du service mysql :

```yml
mysql-db:
  image: mysql:latest
  environment:
    MYSQL_ROOT_PASSWORD: root
    MYSQL_DATABASE: test
    MYSQL_USER: test
    MYSQL_PASSWORD: test
  deploy:
    replicas: 3
    placement:
      constraints:
        - node.role == manager
```

Remplir la base de donnée :

```bash
docker exec -it mysql-db mysql -u root -p
```

```sql
    CREATE DATABASE ma_base_de_donnees;

    USE ma_base_de_donnees;

    CREATE TABLE utilisateurs (
id INT AUTO_INCREMENT PRIMARY KEY,
nom VARCHAR(100) NOT NULL,
email VARCHAR(100) NOT NULL UNIQUE
    );


    INSERT INTO utilisateurs (nom, email) VALUES ('Alice', 'alice@example.com');
    INSERT INTO utilisateurs (nom, email) VALUES ('Bob', 'bob@example.com');


    SELECT * FROM utilisateurs;


    SELECT * FROM utilisateurs WHERE id = 1;


    UPDATE utilisateurs SET email = 'alice_new@example.com' WHERE id = 1;

    DELETE FROM utilisateurs WHERE id = 2;


    SHOW TABLES;
```
