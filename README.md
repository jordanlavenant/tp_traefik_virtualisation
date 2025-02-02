# TP Virtualisation - Traefik

LAVENANT Jordan - BUT Informatique - 31 - 2024-2025

Ce document expose ma démarche pour le TP de virtualisation, qui consiste à déployer un service Traefik sur un cluster Swarm, et à exposer des services web, en utilisant Traefik comme reverse proxy.

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

## Création des réseaux overlay pour les services

Une attention particulière a été portée à la création des réseaux overlay pour les services, afin de les isoler les uns des autres.

En effet, chaque service doit être accessible uniquement par le service Traefik, et non pas par les autres services, afin d'être indépendant. Mais chaque service doit également être accessible par le service Traefik, pour pouvoir être exposé sur le web.

Ainsi, j'ai créer un réseau overlay pour chaque service, afin de naturellement pouvoir communiquer dans leur propre service, mais également un service Traefik, afin de permetre à Traefik de communiquer avec les services web **uniquement** pour les exposer. Cela permet notamment de ne pas exposer les services de caches ou de bases de données sur le web, et de les garder privés.

Cette configuration est illustrée dans le schéma suivant :

![escalidraw](/assets/escalidraw.png)

Création des réseaux :

```bash
# Réseau pour Traefik
docker network create --driver overlay traefik-public

# Réseaux des services
docker network create --driver overlay app-utilisateurs
docker network create --driver overlay app-clusterswarm
docker network create --driver overlay app-fortune
docker network create --driver overlay app-flask
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