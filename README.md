# TP Virtualisation - Traefik

LAVENANT Jordan - BUT Informatique - 31 - 2024-2025

Ce document expose ma démarche pour le TP de virtualisation, qui consiste à déployer un service Traefik sur un cluster Swarm, et à exposer des services web, en utilisant Traefik comme reverse proxy.

## Décomposition du projet

- `./assets` : Contient les images utilisées dans ce document.
- `./services` : Contient les services à déployer.
  - `./services/clusterswarm` : Site web de "Cluster Swarm".
  - `./services/flask` : Site web en flask pris dans la partie « Rappel de 2ième année… ».
  - `./services/fortune` : Application Fortune Images.
  - `./services/utilisateurs` : Site web de "Reprise de contact".
  - `./services/apache` : Site web apache (sous-domaine).

- `docker-compose.yml` : Docker compose pour le déploiement de Traefik et des services.

## Création du cluster swarm

```bash
docker swarm init
```

Etat du cluster swarm, avec 2 workers (-40 et -37) et 1 manager (-245) :

![swarm](/assets/nodes.png)

## Construction des images des services

Il nous faut créer les images des 4 services : 

### Site web de "Reprise de contact"

```bash
# ./services/utilisateurs/
docker build -t utilisateurs_web_image:latest .
```

### Site web de "Cluster Swarm"

```bash
# ./services/clusterswarm/
docker build -t clusterswarm_web_image:latest .
```

### Application Fortune Images

```bash
# ./services/fortune/
docker build -t fortune_web_image:latest .
```

### Site web en flask pris dans la partie « Rappel de 2ième année… »

```bash
# ./services/flask/
docker build -t flask_web_image:latest .
```

### Site web apache (sous-domaine)

```bash
# ./services/apache/
docker build -t apache_web_image:latest .
```

## Création des réseaux overlay pour les services

Une attention particulière a été portée à la création des réseaux overlay pour les services afin de les isoler les uns des autres.

Chaque service doit être accessible uniquement par Traefik et non par les autres services, garantissant ainsi leur indépendance. Cependant, chaque service doit également être accessible par Traefik pour pouvoir être exposé sur le web.

Pour cela, j'ai créé un réseau overlay pour chaque service, permettant une communication interne au sein de chaque service. De plus, un réseau dédié à Traefik a été mis en place pour permettre à Traefik de communiquer avec les services web **uniquement** pour les exposer. Cela permet de ne pas exposer les services de cache ou de bases de données sur le web, les gardant ainsi privés.

Cette configuration est illustrée dans le schéma suivant :

![escalidraw](/assets/escalidraw.png)

Création des réseaux :

```bash
sudo sh networks.sh
```

Ou manuellement :

```bash
# Réseau pour Traefik
docker network create --driver overlay traefik-public

# Réseaux des services
docker network create --driver overlay app-utilisateurs
docker network create --driver overlay app-clusterswarm
docker network create --driver overlay app-fortune
docker network create --driver overlay app-flask
docker network create --driver overlay app-apache
```

## Déploiement du service Traefik

Déploiement du service Traefik :

```bash
docker stack deploy -c docker-compose.yml traefik
```

![traefik-replicas](/assets/traefik_replicas.png)

## Nettoyer le déploiement

```bash
docker stack rm traefik
```

## Routes

| Service                                | URL                                             |
|----------------------------------------|-------------------------------------------------|
| Dashboard Traefik                      | [http://localhost:8080/dashboard/#/](http://localhost:8080/dashboard/#/) |
| Site web de "Reprise de contact"       | [http://utilisateurs.localhost](http://utilisateurs.localhost) |
| Site web de "Cluster Swarm"            | [http://clusterswarm.localhost](http://clusterswarm.localhost) |
| Application Fortune Images             | [http://fortune.localhost](http://fortune.localhost) |
| Site web en flask pris dans la partie « Rappel de 2ième année… » | [http://flask.localhost](http://flask.localhost) |
| Site web apache (sous-domaine)         | [http://localhost/chemin](http://localhost/chemin) |