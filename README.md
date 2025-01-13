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
