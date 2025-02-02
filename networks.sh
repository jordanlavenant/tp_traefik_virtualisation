# Réseau pour Traefik
docker network create --driver overlay traefik-public

# Réseaux des services
docker network create --driver overlay app-utilisateurs
docker network create --driver overlay app-clusterswarm
docker network create --driver overlay app-fortune
docker network create --driver overlay app-flask