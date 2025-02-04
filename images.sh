# Création des images
docker build -t utilisateurs_web_image:latest ./services/utilisateurs/
docker build -t clusterswarm_web_image:latest ./services/clusterswarm/
docker build -t fortune_web_image:latest ./services/fortune/
docker build -t flask_web_image:latest ./services/flask/
docker build -t apache_web_image:latest ./services/apache/