# TP Virtualisation - Traefik

## Création du cluster swarm

Etat du cluster swarm, avec 2 workers (-40 et -37) et 1 manager (-245) :

![swarm](/assets/nodes.png)

## Construction des images des services

<!-- TODO -->

## Création d'un réseau overlay (traefik-net)

Création du réseau overlay traefik-net :

```bash
docker network create --driver overlay traefik-public
docker network create --driver overlay app-utilisateurs
docker network create --driver overlay app-flask
```

## Déploiement du service Trafefik

Déploiement du service Traefik :

```bash
docker stack deploy -c docker-compose.yml traefik
```

![traefik-replicas](/assets/traefik_replicas.png)

## Nettoyer le déploiement

```bash
docker stack rm traefik
```